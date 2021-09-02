#!/usr/bin/env python

import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY,filepath))


if __name__ == "__main__":

    #Remove README
    if '{{cookie.cutter.create_author_file}}' != 'y':
        remove_file('README.md')

    
    if 'Basic_Form' in '{{ cookiecutter.tkinter_project_type|lower }}':
        remove_file("Multipage_Form_with_sample_components.py" )
        remove_file()
        remove_file()
        remove_file()
        remove_file()
        remove_file()
        

    #Material Design
    if '{{cookie.cutter.use_material_design}}' != 'y':
        remove_file('static')

    
