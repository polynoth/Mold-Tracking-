"""
A GUI application with a sqlite backend for locating molds
"""
import backend
from tkinter import *
def getSelectedRow(event):
    try:
        global selectedTuple
        index=list1.curselection()[0]
        selectedTuple = list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selectedTuple[1])
        e2.delete(0,END)
        e2.insert(END,selectedTuple[2])
        e3.delete(0,END)
        e3.insert(END,selectedTuple[3])
        e4.delete(0,END)
        e4.insert(END,selectedTuple[4])
    except IndexError:
        pass
        
    

def viewCommand():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def searchCommand():
    list1.delete(0,END)
    for row in backend.search(ShopOrderInput.get(),MoldLocation.get(),QuanityTotal.get(),Alloy.get()):
        list1.insert(END,row)

def addCommand():
    backend.insert(ShopOrderInput.get(),MoldLocation.get(),QuanityTotal.get(),Alloy.get())
    list1.delete(0,END)
    list1.insert(END,(ShopOrderInput.get(),MoldLocation.get(),QuanityTotal.get(),Alloy.get()))
    
def deleteCommand():
    backend.delete(selectedTuple[0])

def updateCommand():
    backend.update(selectedTuple[0],ShopOrderInput.get(),MoldLocation.get(),QuanityTotal.get(),Alloy.get())
    
    
window = Tk()
window.title("MOLD TRACKER")
#labels for catagories
l1 = Label(window, text="Shop Order #")
l1.grid(row=0,column=0)
l2 = Label(window, text="Mold Location")
l2.grid(row=0,column=2)
l3 = Label(window, text="quanity/total")
l3.grid(row=1,column=0)
l4 = Label(window, text="Alloy")
l4.grid(row=1,column=2)
#input for the catagories
ShopOrderInput = StringVar()
e1 = Entry(window, textvariable =ShopOrderInput) 
e1.grid(row=0,column=1)
MoldLocation = StringVar()
e2 = Entry(window,textvariable=MoldLocation)
e2.grid(row=0,column=3)
QuanityTotal = StringVar()
e3 = Entry(window,textvariable=QuanityTotal)
e3.grid(row=1,column=1)
Alloy = StringVar()
e4 = Entry(window,textvariable=Alloy)
e4.grid(row=1,column=3)
#list of molds
list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,rowspan=6)
sb1=Scrollbar(window)
sb1.grid(row=2,column=1,rowspan=6)
list1.configure(yscrollcommand=sb1.set)
list1.bind('<<ListboxSelect>>',getSelectedRow)
sb1.configure(command=list1.yview)
#buttons
b1=Button(window,text="view All", width=12, command=viewCommand)
b1.grid(row=2,column=3)

b2=Button(window,text="Search Entry",width=12,command=searchCommand)
b2.grid(row=3,column=3)

b3=Button(window,text="Add Entry ", width=12, command=addCommand)
b3.grid(row=4,column=3)
b1=Button(window,text="Update Selected" ,width=12, command=updateCommand)
b1.grid(row=5,column=3)
b1=Button(window,text="Delete Selected" ,width=12,command=deleteCommand)
b1.grid(row=6,column=3)
b1=Button(window,text="Close" ,width=12,command=window.destroy)
b1.grid(row=7,column=3)


window.mainloop()
