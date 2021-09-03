#!/usr/bin/env python

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

def remove_file(filepath):
    path = os.path.join(PROJECT_DIRECTORY,filepath)
    os.remove(path)

def remove_dir(dir):
    path = os.path.join(PROJECT_DIRECTORY,dir)
    shutil.rmtree(path)


if __name__ == "__main__":

    ## TO-DO: change to dictionary to make file names less cluttered
    dictemp = { "basic form" : "basic_form" ,
                "multipage form with sample components" : "multipage" ,
              }


    templates = ["basic_form","multipage_form_with_sample_components","text_editor" , "calculator" , "database" , "currency" , "file_search"]

    chosenTemplate =  '{{cookiecutter.tkinter_project_type|lower}}'

    print (INFO + "Creating template for {{cookiecutter.tkinter_project_type|lower}}..." + TERMINATOR)

    #Remove README

    if '{{cookiecutter.create_README_file}}' != 'y':
        remove_file('README.md')
        

    

    #Delete  templates

    #making new array as removing templates from orignial means you cannot re-use cached cookiecutter 

    deleteTemplates = templates
    i = 0
    
    for template in deleteTemplates:
        
        if(template != chosenTemplate):
            try:
                remove_dir(deleteTemplates[i])
                i += 1
                
            except FileNotFoundError:
                print(WARNING + str(FileNotFoundError)+ TERMINATOR)
                break
        else:
            i +=1

    #Material Design
    if '{{cookiecutter.use_material_design}}' != 'y':
        remove_dir('static')


# finally
print(SUCCESS + "Project initialized, keep up the good work!" + TERMINATOR)
    
