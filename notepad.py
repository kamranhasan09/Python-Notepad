# you need to install tkinter and os module

from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[
                           ("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == " ":
        file = None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[
                                 ("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file)+"- Notepad")
            print("file Saved")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()


def cut():
    TextArea.event_generate(("<<Cut>>"))


def copy():
    TextArea.event_generate(("<<Copy>>"))


def paste():
    TextArea.event_generate(("<<Paste>>"))


def about():
    showinfo("Notepad", "Notepad by Kamran Hasan ")


if __name__ == "__main__":
    root = Tk()
    root.title("Untitled - Notepad")
    root.geometry("644x788")
    # root.wm_iconbitmap("1.ico")
    # text area
    TextArea = Text(root, font="lucida 13")
    file = NONE
    TextArea.pack(expand=TRUE, fill=BOTH)
    # lets create a menu bar
    MenuBar = Menu(root)
    # File menu starts
    fileMenu = Menu(MenuBar, tearoff=0)
    # to open new file
    fileMenu.add_command(label="New", command=newFile)
    # to open already exixting file
    fileMenu.add_command(label="Open", command=openFile)
    # to save file
    fileMenu.add_command(label="save", command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=quitApp)
    MenuBar.add_cascade(label="File", menu=fileMenu)
    # File menu end

    # edit menu Starts
    Editmenu = Menu(MenuBar, tearoff=0)
    # To give a feature of cut,copy,paste
    Editmenu.add_command(label="Cut", command=cut)
    Editmenu.add_command(label="Copy", command=copy)
    Editmenu.add_command(label="Paste", command=paste)

    MenuBar.add_cascade(label="Edit", menu=Editmenu)
    # edit Menu Ends
    # help menu starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="about notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    # help menu ends

    root.config(menu=MenuBar)

    # adding scroll bar
    Scrollbar = Scrollbar(TextArea)
    Scrollbar.pack(side=RIGHT, fill=Y)
    Scrollbar.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scrollbar.set)
    root.mainloop()
