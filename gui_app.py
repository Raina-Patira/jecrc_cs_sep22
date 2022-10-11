#GUI - Graphical User Interface
#Libraries- Tkinter, PyQT, Turtle
import tkinter as ttk 
app=ttk.Tk()
app.title('My App')
app.geometry("600x400")

msg=ttk.Variable(app)
print(msg.get())
msg.set("Empty")
print(msg.get())

#ttk.Label(app,text="A simple text label",).place(x=50,y=50)
#ttk.Label(app,textvariable=msg).place(x=80,y=70)


def abc():
    print("wow")
    msg.set("Ye bhi thik he")
#ttk.Button(app,text="Click here",command=abc,font=("Arial",25)).place(x=100,y=100)
#ttk.Button(app,text="Or else this",command= lambda:msg.set("thik nhi he")).place(x=200,y=100)

f1=ttk.Variable(app)
f1.set("0")
f2=ttk.Variable(app)
f2.set("0")
result=ttk.Variable(app)
ttk.Entry(app,textvariable=f1,width=3,font=("Arial",25)).place(x=50,y=250)
ttk.Entry(app,textvariable=f2,width=3,font=("Arial",25)).place(x=150,y=250)
ttk.Label(app,text="Result",font=("Arial",30)).place(x=200,y=30)
ttk.Label(app,textvariable=result,font=("Arial",25)).place(x=200,y=90)

def calci(op):
    print("I will calculate this")
    result.set(eval(f1.get()+op+f2.get()))

ttk.Button(app,text="+",command=lambda:calci("+"),font=("Arial",15)).place(x=50,y=300)
ttk.Button(app,text="-",command=lambda:calci("-"),font=("Arial",15)).place(x=100,y=300)
ttk.Button(app,text="*",command=lambda:calci("*"),font=("Arial",15)).place(x=150,y=300)
ttk.Button(app,text="/",command=lambda:calci("/"),font=("Arial",15)).place(x=200,y=300)

box=ttk.Listbox(app,height=5,fg="red",activestyle="dotbox")
box.insert(1,"Raina")
box.insert(2,"Palak")
box.insert(3,"Pooja")
box.place(x=300,y=100)

def show():
    print(box.get(box.curselection()))

ttk.Button(app,text="show",command=show).place(x=350,y=250)
app.mainloop()



#https://github.com/sanampeeyush/jecrc_cs_sep22/tree/assignment1/assignments
