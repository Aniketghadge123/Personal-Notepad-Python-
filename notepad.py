from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfile,asksaveasfile

def clear():
    textArea.event_generate('<<Clear>>')

def copy():
    textarea.event_generate('<<Copy>>')

def paste():
    textarea.event_generate('<<Paste>>')


def allselect():
    textarea.event_generate("<<SelectAll>>")

def cut():
    textarea.event_generate('<<Cut>>')

def closeApplocation():
    root.destroy()

def new():
    textarea.delete(1.0, END)

def about():
    showinfo("About Company ","This software is developed by NETTECHIANS and has the complete @ copywrite")

def openFile():
    nameofFile = askopenfile()
    pathOfFile = nameofFile.name

    f = open(pathOfFile,"r")
    data = f.read()
    f.close()
    textarea.insert(1.0,data)

def saveFile():
    content = textarea.get(1.0,END)
    nameFile  = asksaveasfile(initialfile = 'Untitled.txt',defaultextension=".txt",     filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    f = open(nameFile.name,"w")

    f.write(content)
    f.close()

def teams():
    showinfo("About Team","Lead Developer : Nachiket , Testing : Vishal Garje , Design and UI : Archana Bharti ")

root = Tk()
root.geometry("500x300")
root.title(" Personal Notepad by Aniket ")
textarea = Text()
textarea.pack(expand=True,fill=BOTH)
textarea.config(bg="light yellow")

mainMenu = Menu(root)
root.config(menu=mainMenu)


filemenu = Menu(mainMenu,tearoff=0)

editMenu = Menu(mainMenu,tearoff=0)
aboutMenu = Menu(mainMenu,tearoff=0)

filemenu.add_command(label = "New",command=new)
filemenu.add_command(label = "Open",command=openFile)
filemenu.add_command(label = "Save",command=saveFile)
filemenu.add_separator()
filemenu.add_command(label = "Quit",command=closeApplocation)


editMenu.add_command(label="Select All",command=allselect)
editMenu.add_command(label="Cut All",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)

aboutMenu.add_command(label="About Us",command=about)
aboutMenu.add_command(label="Developers Team",command=teams)


mainMenu.add_cascade(label="File",menu = filemenu)
mainMenu.add_cascade(label="Edit",menu=editMenu)
mainMenu.add_cascade(label="About",menu = aboutMenu)
root.mainloop()