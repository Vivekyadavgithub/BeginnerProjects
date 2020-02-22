from tkinter import *
import sqlite3
import tkinter.messagebox

root=Tk()
root.geometry("800x600")

def save():
    conn = sqlite3.connect("tkin.db")
    a=[]
    l=[]
    a.append(e1.get())
    a.append(e2.get())
    a.append(e3.get())
    rs=[]
    l.append(e1.get())
    rs=conn.execute("select * from info where code=?", l)
    if(not rs.fetchall()):
        conn.execute("insert into info values(?,?,?)",a)
        conn.commit()
        tkinter.messagebox.showinfo("hello","record saved")
    else:
        tkinter.messagebox.showinfo("hello","record already exists")


def retrieve():

    conn = sqlite3.connect("tkin.db")
    l=[]
    l.append(e1.get())
    clear()
    rs=conn.execute("select * from info where code=?",l).fetchall()

    if(not rs):
        tkinter.messagebox.showinfo("hello","record not found")
    else:
        e1.insert(0, rs[0][0])
        e2.insert(0,rs[0][1])
        e3.insert(0, rs[0][2])
        tkinter.messagebox.showinfo("hello","record retrieved")
def clear():
    e1.delete(0,END)
    e2.delete(0, END)
    e3.delete(0, END)

def update():
    conn = sqlite3.connect("tkin.db")
    b=[]
    x=e1.get()
    b.append(e2.get())
    b.append(e3.get())
    b.append(x)
    conn.execute("update info set name=?,salary=? where code=?",b)
    conn.commit()
    tkinter.messagebox.showinfo("hello","record updated")

def delete():
    ans=tkinter.messagebox.showinfo("hello","are u sure u wanna delete it")
    if(ans):
      conn = sqlite3.connect("tkin.db")
      l=e1.get()
      conn.execute("delete from info where code=?",[l])
      conn.commit()


l0=Label(root,text="                                                                                               ")
la=Label(root,text="                                                                                               ")
lb=Label(root,text="                                                                                               ")
lc=Label(root,text="                                                                                               ")
ld=Label(root,text="                                                                                               ")
le=Label(root,text="                                                                                               ")
lf=Label(root,text="                                                                                               ")
l1=Label(root,text="code",bg="green")
e1=Entry(root)
#e1.insert(10,"111")
l2=Label(root,text="name",bg="green")
e2=Entry(root)
#e2.insert(10,"vivek")
l3=Label(root,text="salary",bg="green")
e3=Entry(root)
#e3.insert(10,"1000")
b1=Button(root,text="save",command=save)
b2=Button(root,text="retrieve",command=retrieve)
b3=Button(root,text="update",command=update)
b4=Button(root,text="delete",command=delete)
l0.grid(row=0)
la.grid(row=1)
lb.grid(row=2)
lc.grid(row=3)
ld.grid(row=4)
le.grid(row=5)
lf.grid(row=6)
l1.grid(row=7,column=1)
e1.grid(row=7,column=2)
l2.grid(row=8,column=1)
e2.grid(row=8,column=2)
l3.grid(row=9,column=1)
e3.grid(row=9,column=2)
b1.grid(row=10,column=1)
b2.grid(row=10,column=2)
b3.grid(row=10,column=3)
b4.grid(row=10,column=4)
root.mainloop()