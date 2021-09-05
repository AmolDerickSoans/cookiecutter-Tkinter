![Python][python-shield]
![Contributors][contributors-shield]
![Stargazers][stars-shield]
![Forks][forks-shield]
![Issues][issues-shield]
![License][license-shield]

![Group 7284](https://user-images.githubusercontent.com/22007192/132085506-789ae19c-95c7-48ff-974c-09a0c222bade.png)
# Content

# About
CookiecutterTkinter offers multiple templates to build tkinter projects. 

` cookiecutter gh:AmolDerickSoans/cookiecutter-Tkinter `

# Features

- [ttktheme](https://ttkthemes.readthedocs.io/en/latest/) support
- Test Framework for project
- Built-in README file generator
- Built-in LICENSE file generator

# TEMPLATES AVAILABLE
## Basic single page form with multiple widgets
![basic_form](https://user-images.githubusercontent.com/22007192/132120557-a3637978-e2b7-4f0d-a73e-8d0a6a2155cc.PNG)

## Multipage form with widgets , notebooks.

## Single page with spalshscreen support
## Calculator Demo
## Text Editor Demo
## File Search Demo
![tempsnip](https://user-images.githubusercontent.com/22007192/132120523-217e505d-9711-4392-8f1a-3f5eef661f59.png)

#  ttk Themes

![Group 7287](https://user-images.githubusercontent.com/22007192/132086348-91be91b1-b4e4-4f29-ba23-595725b6dcb7.png)

**Know More** [TtkThemes](https://ttkthemes.readthedocs.io/en/latest/themes.html#)

# How to Use

# Contribute

This Project is looking for contributors , if you feel like making a template out of your tkinter code please follow these steps:
1. Fork this repository
2. Write well documented tkinter code that can be easily customisable 
3. Add theme support inside your code.
   ```python
    # pip install ttkthemes
    from ttkthemes import ThemedStyle 
    ##THEMES
    # "arc  ","plastik" , "adapta" , "yaru" , "radiance" , "breeze" ,"no-theme"
    if '{{ cookiecutter.ttkTheme|lower}}' == 'no-theme':
        print("no theme file selected ,Set to default")

    else:
        style = ThemedStyle()
        style.theme_use('{{ cookiecutter.ttkTheme|lower}}')

   ```
   
4. Add code  to `{{cookiecutter.project_slug}}` folder.
   ```bash
      +{{cookiecutter.project_slug}}
      |
      |- BasicForm
      |   |
      |   |- main.py
      |
      |- YourTemplate
          |- subDirs
          |-main.py
     ```
    
5. Add `YourTemplate` to  `cookiecutter.json`
6. Add `YourTemplate` to  the template list in `hooks\post_gen_project.py`

[contributors-shield]: https://img.shields.io/github/contributors/AmolDerickSoans/cookiecutter-Tkinter?style=for-the-badge

[forks-shield]: https://img.shields.io/github/forks/AmolDerickSoans/cookiecutter-Tkinter?style=for-the-badge

[stars-shield]: https://img.shields.io/github/stars/AmolDerickSoans/cookiecutter-Tkinter?style=for-the-badge

[issues-shield]: https://img.shields.io/github/issues/AmolDerickSoans/cookiecutter-Tkinter?style=for-the-badge

[python-shield]: 	https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white

[license-shield]: https://img.shields.io/github/license/AmolDerickSoans/cookiecutter-Tkinter?style=for-the-badge
