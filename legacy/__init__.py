from __PYSHA import *
import logging
from tkinter import *  # imports the Gui feature for the specified stuff

# TODO : http://scipy.github.io/old-wiki/pages/Tentative_NumPy_Tutorial   , Specific NUMPY TUTORIALS
# TODO : http://scipy.github.io/old-wiki/pages/Numpy_Example_List   , These are the numpy examples.

# Instructions are written in the readme.md
# Was not expecting errors from there. 
def About():
    pass


def closeAll():
    print("Closing the file")


def revertingall():
    print("Reverting all the changes ")


def addimage():
    print("image added")


def launch_pysha():
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
    logging.info("Creating and Fetching all the classes and dependencies")
    M_Obj = Main_Call()  # Class Object
    M_Obj.main()  # Calling the main Function .!!


if __name__ == '__main__':
    root = Tk()
    frame = Frame(root)  # Creates the frame
    # ---------------------MAIN MENU ------------------------#
    menu = Menu(root)  # This created the menu
    root.config(menu=menu)  # Configuring the main
    subMenu = Menu(menu)  # Creating the menu , since the Menu is another menu
    menu.add_cascade(label="Options", menu=subMenu)  # Cascade is the drop down menu
    subMenu.add_command(label="About", command=About)  # This is the labeled new project with do nothing command
    subMenu.add_command(label="Purpose", command=closeAll)  # This is the labeled new project with do nothing command
    subMenu.add_separator()  # this splits the thing , for seperating the menus
    subMenu.add_command(label="Exit", command=root.quit)

    editMenu = Menu(menu)  # Since the parent is now the menu
    menu.add_cascade(label="Edit", menu=editMenu)
    editMenu.add_command(label="Redo", command=revertingall)
    toolbar = Frame(root, bg="blue")  # A Frame that stretches accross
    insert_Button = Button(toolbar, text='Launch PYSHA', command=launch_pysha)  # Creating  a button, this will launch pysha
    insert_Button.pack(side=LEFT, padx=2, pady=2)  # The side is left, the paddding(Extra spaces are 2)
    toolbar.pack(side=TOP, fill=X)
    # Adding the status bar as well in the windows
    status = Label(root, text="PYSHA Running..", bd=1, relief=SUNKEN, anchor=W)  # Ancdhor to be on the west
    status.pack(side=BOTTOM, fill=X)  # This will fill always fil the bottom
    root.mainloop()

# You must have the requirements on the requirements.txt
# Install the requirements using the pip command as pip install -r requirements.txt as per specified
# Before installing the requirements , install the additional requirements as per specified in the additional requirements.txt
