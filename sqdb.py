import sqlite3

conn=sqlite3.connect("vivek.db")
print("dataBASE connected")
basic=0
a=[]
def input1():
    global basic
    global a
    a.append(int(input("enter code")))
    a.append(input("enter name"))
    basic=int(input("enter sal"))
    a.append(basic)
def calculate():
    global basic
    global a
    a.append(.2*basic)
    a.append(.15*basic)
    a.append(.01*basic)
    a.append(a[2]+a[3]+a[4]+a[5])

def save():
    conn.execute("insert into emp values(?,?,?,?,?,?,?)",a)
    conn.commit()
    print("record inserted")

def update():
    global basic
    global a
    a.append(0)
    x=int(input("enter code to be updated"))
    a.append(input("enter name"))
    basic=int(input("enter sal"))
    a.append(basic)
    calculate()
    a.pop(0)
    a.append(x)
    conn.execute("update emp set name=?,basic=?,hra=?,da=?,conv=?,total=? where code=?",a)
    conn.commit()
    print("record updated")

input1()
calculate()
save()
#update()