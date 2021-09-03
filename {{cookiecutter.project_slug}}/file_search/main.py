import pathlib
import tkinter as tk
from datetime import datetime
from queue import Queue
from threading import Thread
from tkinter import ttk
from tkinter.filedialog import askdirectory
import subprocess
import platform
import os

from ttkthemes import ThemedStyle
import ttkthemes

RUNNING = False


def browse_path():
    path = askdirectory(title='Directory')
    if path:
        path_var.set(path)
        root.update_idletasks()


def search_path():
    path = path_var.get()
    option = search_var.get()
    term = term_var.get()
    Thread(target=_search_thread, args=(path, option, term), daemon=True).start()
    toggle_running()


def _search_thread(path, option, term):
    # clear existing results
    result_tree.delete(*result_tree.get_children())

    if option == 'contains':
        find_contains(term, path)
    elif option == 'startswith':
        find_startswith(term, path)
    else:
        find_endswith(term, path)
    progress_bar.stop()


def find_contains(term, path):
    for path, _, files in pathlib.os.walk(path):
        if files:
            for file in files:
                if term in file:
                    result_queue.put(create_record(file, path))
    toggle_running()


def find_endswith(term, path):
    for path, _, files in pathlib.os.walk(path):
        if files:
            for file in files:
                if file.endswith(term):
                    result_queue.put(create_record(file, path))
    toggle_running()


def find_startswith(term, path):
    for path, _, files in pathlib.os.walk(path):
        if files:
            for file in files:
                if file.starswith(term):
                    result_queue.put(create_record(file, path))
    toggle_running()


def create_record(file, path):
    fileh = pathlib.Path(path) / file
    stats = fileh.stat()
    name = fileh.stem
    modified = datetime.fromtimestamp(stats.st_mtime).strftime("%Y-%m-%d %I:%M:%S%p")
    file_type = fileh.suffix.lower()
    size = f"{stats.st_size / 1000000:,.2f} MB"
    file_path = fileh.absolute()
    return name, modified, file_type, size, file_path


def toggle_running():
    global RUNNING
    if RUNNING:
        progress_bar.stop()
    RUNNING = not RUNNING
    check_for_records()
    progress_bar.start(50)
    print("running was toggled", RUNNING)


def check_for_records():
    if RUNNING and not result_queue.empty():
        print("Checking queue")
        record = result_queue.get()
        result_tree.insert('', 'end', values=record)
        root.after(1, lambda: check_for_records)
    else:
        while not result_queue.empty():
            result_tree.insert('', 'end', values=result_queue.get())


def reveal_in_explorer(id_):
    """Callback for double-click event on tree"""
    values = result_tree.item(id_, 'values')
    path = pathlib.Path(values[-1]).absolute().parent
    if platform.system() == "Darwin":
        subprocess.call(['open', path])
    elif platform.system() == "Windows":
        os.startfile(path)
    else:
        subprocess.call(['xdg-open', path])


def doubleclick_record(event=None):
    id_ = result_tree.selection()
    if id_:
        reveal_in_explorer(id_[0])


result_queue = Queue()  # for storing search results

root = tk.Tk()
root.title("File Search Engine")
frame = ttk.Frame(root, padding=(15, 0))

##THEMES
# "arc  ","plastik" , "adapta" , "yaru" , "radiance" , "breeze" ,"no-theme"
if '{{ cookiecutter.ttkTheme|lower}}' == 'no-theme':
    print("no theme file selected ,Set to default")

else:
    style = ThemedStyle()
    style.theme_use('{{ cookiecutter.ttkTheme|lower}}')







# ----- application options
option_frame = ttk.LabelFrame(frame, text="Complete the form to begin your search", padding=20)

# ----------- path and term entry
path_lbl = ttk.Label(option_frame, text="Path")
path_var = tk.StringVar()
path_input = ttk.Entry(option_frame, textvariable=path_var)
term_lbl = ttk.Label(option_frame, text="Term")
term_var = tk.StringVar()
term_input = ttk.Entry(option_frame, textvariable=term_var)
browse_btn = ttk.Button(option_frame, text="Browse", command=browse_path)
search_btn = ttk.Button(option_frame, text="Search", command=search_path)

# ----------- search type radio buttons
search_var = tk.StringVar()
search_var.set('contains')
search_type_group = ttk.Frame(option_frame, padding=10)
contains_radio = ttk.Radiobutton(search_type_group, text="Contains", variable=search_var, value="contains")
endswith_radio = ttk.Radiobutton(search_type_group, text="Ends With", variable=search_var, value="endswith")
startswith_radio = ttk.Radiobutton(search_type_group, text="Starts With", variable=search_var, value="startswith")

# ----- result tree view
result_frame = ttk.LabelFrame(frame, text="Results for this search", padding=20)
result_tree = ttk.Treeview(result_frame, columns=(1, 2, 3, 4, 5), show="headings", height=10, selectmode="browse")
result_tree.heading(1, text="Name")
result_tree.heading(2, text="Modified Date")
result_tree.heading(3, text="Type")
result_tree.heading(4, text="Size")
result_tree.heading(5, text="Path")

result_tree.column(1, stretch=True)
result_tree.column(2, width=200, anchor='center')
result_tree.column(3, width=60, anchor='center')
result_tree.column(4, width=60, anchor='center')

result_tree.bind("<Double-1>", doubleclick_record)

# ----- progress bar
progress_bar = ttk.Progressbar(frame, mode='indeterminate')

# ----- layout management
option_frame.columnconfigure(1, weight=1)
path_lbl.grid(row=0, column=0)
path_input.grid(row=0, column=1, sticky=tk.EW, padx=10)
term_lbl.grid(row=1, column=0)
term_input.grid(row=1, column=1, sticky=tk.EW, padx=10)
browse_btn.grid(row=0, column=2)
search_btn.grid(row=1, column=2)

contains_radio.pack(side=tk.TOP, expand='yes', fill='x')
endswith_radio.pack(side=tk.TOP, expand='yes', fill='x')
startswith_radio.pack(side=tk.TOP, expand='yes', fill='x')
search_type_group.grid(row=0, column=3, rowspan=2)

option_frame.pack(side=tk.TOP, expand='yes', fill='x', pady=15)
result_tree.pack(side=tk.TOP, expand='yes', fill='both')
result_frame.pack(expand='yes', fill='both')
progress_bar.pack(expand='yes', fill='x', padx=10, pady=10)
frame.pack(expand='yes', fill='both')

root.mainloop()