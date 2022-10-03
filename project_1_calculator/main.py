from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.geometry("350x550")
root.maxsize(350,550)
root.minsize(350,550)
root.title("Calculator")

def click(event):

    text = event.widget.cget("text")
    try:
        if text == "=":
            if ent.get().isdigit():
                value = int(var.get())
            else:
                value = eval(var.get())
                var.set(value)

        elif text == "C":
            var.set("")
        else:
            var.set(var.get() + str(text))
    except Exception as e:
        msg.showerror("Information","Invalid Buttons You Cliked!")


#entry
var = StringVar()
ent = Entry(root,font=('Verdana',30),textvariable=var)
ent.pack(fill=X,ipady=15)

#buttons ,palce,bind
btn1 = Button(root,text=9,width=10,height=3)
btn1.place(x=20,y=85)
btn1.bind('<Button-1>',click)

btn2 = Button(root,text=8,width=10,height=3)
btn2.place(x=135,y=85)
btn2.bind('<Button-1>',click)

btn3 = Button(root,text=7,width=10,height=3)
btn3.place(x=250,y=85)
btn3.bind('<Button-1>',click)

btn4 = Button(root,text=6,width=10,height=3)
btn4.place(x=20,y=160)
btn4.bind('<Button-1>',click)

btn5 = Button(root,text=5,width=10,height=3)
btn5.place(x=135,y=160)
btn5.bind('<Button-1>',click)

btn6 = Button(root,text=4,width=10,height=3)
btn6.place(x=250,y=160)
btn6.bind('<Button-1>',click)

btn7 = Button(root,text=3,width=10,height=3)
btn7.place(x=20,y=240)
btn7.bind('<Button-1>',click)

btn8 = Button(root,text=2,width=10,height=3)
btn8.place(x=135,y=240)
btn8.bind('<Button-1>',click)

btn9 = Button(root,text=1,width=10,height=3)
btn9.place(x=250,y=240)
btn9.bind('<Button-1>',click)

btn10 = Button(root,text=0,width=10,height=3)
btn10.place(x=20,y=320)
btn10.bind('<Button-1>',click)

btn11 = Button(root,text="+",width=10,height=3)
btn11.place(x=135,y=320)
btn11.bind('<Button-1>',click)

btn12 = Button(root,text="-",width=10,height=3)
btn12.place(x=250,y=320)
btn12.bind('<Button-1>',click)

btn13 = Button(root,text="*",width=10,height=3)
btn13.place(x=20,y=400)
btn13.bind('<Button-1>',click)

btn14 = Button(root,text="/",width=10,height=3)
btn14.place(x=135,y=400)
btn14.bind('<Button-1>',click)

btn15 = Button(root,text="%",width=10,height=3)
btn15.place(x=250,y=400)
btn15.bind('<Button-1>',click)

btn16 = Button(root,text="=",width=10,height=3)
btn16.place(x=20,y=480)
btn16.bind('<Button-1>',click)

btn17 = Button(root,text="C",width=10,height=3)
btn17.place(x=135,y=480)
btn17.bind('<Button-1>',click)

btn18 = Button(root,text=".",width=10,height=3)
btn18.place(x=250,y=480)
btn18.bind('<Button-1>',click)


root.mainloop()