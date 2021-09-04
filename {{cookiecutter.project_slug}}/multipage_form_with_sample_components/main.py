import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import scrolledtext
from tkinter import messagebox
import webbrowser
LARGEFONT =("Verdana", 35)
  
class app(tk.Tk):
     
    # __init__ function for class app
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1, Page2 , Page3):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  
# first window frame startpage
  
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
         
        # label of frame Layout 2
        label = ttk.Label(self, text ="Startpage", font = LARGEFONT)
         
        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        button1 = ttk.Button(self, text ="Page 1",
        command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Page 2",
        command = lambda : controller.show_frame(Page2))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)



        button3 = ttk.Button(self, text ="Page 3",
        command = lambda : controller.show_frame(Page3))
     
        # putting the button in its place by
        # using grid
        button3.grid(row = 3, column = 1, padx = 10, pady = 10)
  
  
          
  
  
# second window frame page1
class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
      

        ## -------------------------------------Your Code-------------------------------------
        ## Heading
        label = ttk.Label(self, text ="Page 1", font = LARGEFONT)
        label.grid(row = 0, column = 0, padx = 10, pady = 10)

        ## Contnet
        text_area = scrolledtext.ScrolledText(self,
                            width = 50, 
                            height = 8, 
                            font = ("Times New Roman",
                                    15))
  
        text_area.grid(row = 1,column = 0, pady = 10, padx = 10)
        
        # Inserting Text which is read only
        text_area.insert(tk.INSERT,
        """\
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Etiam feugiat, nulla sed placerat sollicitudin , 
        tellus leo lobortis enim, quis dapibus eros lacus sed felis. 
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
         Etiam feugiat, nulla sed placerat sollicitudin,
        tellus leo lobortis enim, quis dapibus eros lacus sed felis.
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Etiam feugiat, nulla sed placerat sollicitudin , 
        tellus leo lobortis enim, quis dapibus eros lacus sed felis. 
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
         Etiam feugiat, nulla sed placerat sollicitudin,
        tellus leo lobortis enim, quis dapibus eros lacus sed felis.
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        Etiam feugiat, nulla sed placerat sollicitudin , 
        tellus leo lobortis enim, quis dapibus eros lacus sed felis. 
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
         Etiam feugiat, nulla sed placerat sollicitudin,
        tellus leo lobortis enim, quis dapibus eros lacus sed felis. 
        """)
        ##-------------------------------------------------------------------------------------


        ##---------------------Navigation Between Pages ---------------------------------------
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place
        # by using grid
        button1.grid(row =2, column = 0, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="Page 2",
                            command = lambda : controller.show_frame(Page2))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
  
  
  
# third window frame page2  
## WARNING : !Geometery manager is pack() not grid here......
class Page2(tk.Frame):
    def __init__(self, parent, controller):
       
            
        
        tk.Frame.__init__(self, parent)
        
        style = ttk.Style(self)
        style.configure('lefttab.TNotebook', tabposition='wn')   
       #-------------------TABS a.k.a Tkinter Notebook --------------------------------
        tabControl = ttk.Notebook(self , style='lefttab.TNotebook')
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tab3 = ttk.Frame(tabControl)
        tab4 = ttk.Frame(tabControl)

        tabControl.add(tab1, text ='Tab1')
        tabControl.add(tab2, text ='Tab2')
        tabControl.add(tab3, text ='Tab3')
        tabControl.add(tab4, text ='Confirm')
        tabControl.pack(expand = 1, fill ="both")
        ##-------------------------------Internal Functions Being used inside Tabs -------------------------
        def notification():
             messagebox.showinfo("ShowInfo", "Information")

        def error_notification():
             messagebox.showerror("Error", "demoError")
        
        def ask_notification():
             messagebox.askquestion("askquestion", "Are you sure?")

        
        #tab1 
        ## YOU can use anygeomtery manager inside notbook tab not necessarily the one used by parent
        ttk.Label(tab1,text = "Details in First page"
                
                 ).grid(column = 0, 
                                    row = 0,
                                    padx = 3,
                       
                                    pady = 3)  
        
    
       
        
        button_view = ttk.Button(tab1,text ="Info Message" , command = lambda: notification(), 
        )
        button_view.grid(
            column= 0 , 
            row= 2,
            padx= 5,
            pady= 5
        )
        


        #tab2 

        ttk.Label(tab2,

                text ="Details of secondpage").grid(column = 0,
                                            row = 0, 
                                            padx = 3,
                                            pady = 3)
        
        ttk.Button(tab2,text ="Err Message" , command = lambda: error_notification(), 
        ).grid(
            column= 0 , 
            row= 2,
            padx= 5,
            pady= 5
        )

        #tab3

        ttk.Label(tab3,

                text ="Details of 3rd page").grid(column = 0,
                                            row = 0, 
                                            padx = 3,
                                            pady = 3)
        
        ttk.Button(tab3,text ="Question Message" , command = lambda: ask_notification(), 
        ).grid(
            column= 0 , 
            row= 2,
            padx= 5,
            pady= 5
        )

        #tab4

        button_previousp1= ttk.Button(self, text =" << Previous Page",
                            command = lambda : controller.show_frame(Page1)).pack() #grid(column = 4,row = 1,padx=5,pady=5)
        
        button_something= ttk.Button(self, text ="Something",
                            command = lambda : notification()).pack()#grid(column = 5,row = 1,padx=20,pady=5)

        button_nextp1= ttk.Button(self, text ="Next Page >>",
                            command = lambda : controller.show_frame(Page3)).pack()#grid(column = 6,row = 1,padx=20,pady=5)
        
       
class Page3(tk.Frame):
     
    def __init__(self, parent, controller):

        def quit():
            self.destroy()
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 3", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Page2",
                            command = lambda : controller.show_frame(Page2))
     
        # putting the button in its place
        # by using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="Quit",
                            command =  lambda: quit())
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
  
  
  
  
# Driver Code
app = app()
def donothing():
            print("blah")
menubar = Menu(app)
#fileMenu with options New ,Open ,Save ,SaveAs , Close
filemenu = Menu(menubar,tearoff =0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=app.quit)
menubar.add_cascade(label="File", menu=filemenu)
#help menu with links to github ,about(ppl who worked on openCV360 ) and paper
helpmenu = Menu(menubar, tearoff=0)

new = 1
url ="https://github.com/AmolDerickSoans/cookiecutter-Tkinter"
def openweb():
    webbrowser.open(url,new = new)


helpmenu.add_command(label="Github", command=openweb)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

app.config(menu=menubar)
# app.iconbitmap(r'resources/favicon.ico')
app.title('{{cookiecutter.project_name}}')
app.mainloop()