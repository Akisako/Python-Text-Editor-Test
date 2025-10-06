# TEXT EDITOR PYTHON

from tkinter import *
from tkinter.filedialog import *

filename = None

# Font  ___________________________

def FontHelvetica():
    global text
    text.config(font="Helvetica")

def FontCourier():
    global text
    text.config(font="Courier")

# LOGIC  _________________________

def saveFile():
    # NEED REDO
    global text

    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()

def saveAsFile():
    global text

    t = text.get("1.0", "end-1c")
    savelocation = asksaveasfilename(defaultextension='.txt')

    file1 = open(savelocation, "w+")
    file1.write(t)
    file1.close()


def newFile():
    global filename
    
    filename = "Untitled"
    text.delete(0.0, END)

def openFile():
    f = askopenfile(mode="r")
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

# main  __________________________________________________

root = Tk("Text Editor")

root.title("Text Editor | Python")
root.minsize(width=460, height=400)
root.maxsize(width=460, height=400)



menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Save As", command=saveAsFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="New File", command=newFile)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

fontmenu = Menu(menubar, tearoff=0)

fontmenu.add_checkbutton(label="Courier", command=FontCourier)
fontmenu.add_checkbutton(label="Helvetica", command=FontHelvetica)
menubar.add_cascade(label="Fonts", menu=fontmenu)

text = Text(root)
text.grid()

root.config(menu=menubar)
root.mainloop()
