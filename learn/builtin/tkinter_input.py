#!/usr/bin/env python
#-*- encoding=utf-8  -*-
'tkinter test'
__all__={"Alex Yean","2015-11-13"}

from Tkinter import *
import tkMessageBox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput=Entry(self)
        self.nameInput.pack()
        self.quitButton=Button(self,text="Hello",command=self.hello)
        self.quitButton.pack()
  
    def hello(self):
        name=self.nameInput.get() or "World"
        tkMessageBox.showinfo("Message","Hello %s!" % name)

root=Tk()
menubar=Menu(root)
def hello():
    print('hello')

def about():
    print('我是开发者')
#创建下拉菜单File，然后将其加入到顶级的菜单栏中
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

#创建另一个下拉菜单Edit
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit",menu=editmenu)
#创建下拉菜单Help
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)
app=Application(root)
app.master.title("Hello world")
app.master.maxsize(1000, 400)
app.mainloop()
