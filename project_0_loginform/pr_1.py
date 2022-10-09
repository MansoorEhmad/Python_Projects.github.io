from tkinter import *


win = Tk()

#Size of Window
win.geometry("700x500")
win.minsize(700,500)
win.maxsize(700,500)

#background
win.configure(background="green")

#title
win.title("suit")

#lables
lb1 =Label(win,text="Sign Up Page",bg="black",fg="white")
lb1.place(x=300,y=30)


lb2 =Label(win,text="User Name:",bg="black",fg="white")
lb2.place(x=200,y=180)

lb3 =Label(win,text="Password:",bg="black",fg="white")
lb3.place(x=205,y=230)

#variables
lb2_var = StringVar()
lb3_var = StringVar()


#entry box
ent1 = Entry(win,fg="black",width=30,textvariable=lb2_var)
ent2 = Entry(win,show="*",fg="black",width=30,textvariable=lb3_var)
ent1.place(x=300,y=180)
ent2.place(x=300,y=230)


#function
def func():

    u = lb2_var.get()
    p = lb3_var.get()
    if u == "admin" and p == "admin":
        lb4.config(text="Login Successfully")
        with open("pr_1.text", "a") as f:
            f.write(f"Your UserName:{u} And Password:{p} \n")
    else:
        lb4.config(text="Invalid UserName Or Password")


#button
btn =Button(win,text="Submit",bg="black",fg="white",command=func)
btn.place(x=207,y=265)


#label4 for validation


lb4 = Label(win,text="Press Button",bg="black",fg="white")
lb4.place(x=300,y=350)

win.mainloop()
