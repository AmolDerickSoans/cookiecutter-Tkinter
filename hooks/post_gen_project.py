#!/usr/bin/env python

import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

def remove_file(dir):
    os.remove(os.path.join(PROJECT_DIRECTORY,dir))


if __name__ == "__main__":

    print(INFO + "Cleaning-up template..." + TERMINATOR)

    #Remove README
    if '{{cookie.cutter.create_author_file}}' != 'y':
        remove_file('README.md')

    # Remove other templates
    if 'basic_form' in '{{ cookiecutter.tkinter_project_type|lower }}':
        remove_file("multipage_form_with_sample_components" )
        remove_file("calculator")
        remove_file("database")
        remove_file("currency")

    if 'calculator' in '{{ cookiecutter.tkinter_project_type|lower }}':
        remove_file("multipage_form_with_sample_components" )
        remove_file("basic_form")
        remove_file("database")
        remove_file("currency")
    
    if 'currency' in '{{ cookiecutter.tkinter_project_type|lower }}':
        remove_file("multipage_form_with_sample_components" )
        remove_file("basic_form")
        remove_file("database")
        remove_file("calculator")
            
        

    #Material Design
    if '{{cookie.cutter.use_material_design}}' != 'y':
        remove_file('static')


# finally
print(SUCCESS + "Project initialized, keep up the good work!" + TERMINATOR)
    
