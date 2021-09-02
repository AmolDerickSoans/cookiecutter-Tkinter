#!/usr/bin/env python

import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY,filepath))


if __name__ == "__main__":

    print(INFO + "Cleaning-up template..." + TERMINATOR)

    #Remove README
    if '{{cookie.cutter.create_author_file}}' != 'y':
        remove_file('README.md')

    # Remove other templates
    if 'Basic_Form' in '{{ cookiecutter.tkinter_project_type|lower }}':
        remove_file("Multipage_Form_with_sample_components.py" )
        remove_file()
        remove_file()
        remove_file()
        remove_file()
        remove_file()
    
    if 'Multipage_Form_with_sample_components' in '{{ cookiecutter.tkinter_project_type|lower }}':
        remove_file("Multipage_Form_with_sample_components.py" )
        remove_file()
        remove_file()
        remove_file()
        remove_file()
        remove_file()
    

        

    #Material Design
    if '{{cookie.cutter.use_material_design}}' != 'y':
        remove_file('static')


# finally
print(SUCCESS + "Project initialized, keep up the good work!" + TERMINATOR)
    
