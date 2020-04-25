from tkinter import *
root=Tk()
#global operator

def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    scval.set(operator)

def btnClear():
    global operator
    operator=""
    scval.set("")

def btnEqual():
    global operator
    sumup=str(eval(operator))
    scval.set(sumup)
    operator=""
operator=""
scval=StringVar()
scval.set("")
screen=Entry(root,textvariable=scval,font="lucida 20 bold",bg="#a31aff"
             ,bd=20,justify="right").grid(columnspan=4)
b9=Button(root,text="9",padx=16,bd=8,font="arial 20 bold",command=lambda:btnClick(9)).grid(row=1,column=0)
b8=Button(root,text="8",padx=16,bd=8,font="arial 20 bold",command=lambda:btnClick(8)).grid(row=1,column=1)
b7=Button(root,text="7",padx=16,bd=8,font="arial 20 bold",command=lambda:btnClick(7)).grid(row=1,column=2)
add=Button(root,text="+",padx=16,bd=8,font="arial 20 bold",command=lambda:btnClick("+")).grid(row=1,column=3)

b6=Button(root,text="6",padx=16,bd=8,font="arial 20 bold",command=lambda:btnClick(6)).grid(row=2,column=0)
b5=Button(root,text="5",padx=16,bd=8,font="arial 20 bold",command=lambda:btnClick(5)).grid(row=2,column=1)
b4=Button(root,text="4",padx=16,bd=8,font="arial 20 bold",command=lambda:btnClick(4)).grid(row=2,column=2)
sub=Button(root,text="-",padx=16,bd=8,font="arial 20 bold",command=lambda:btnClick("-")).grid(row=2,column=3)

b3=Button(root,text="3",padx=16,bd=8,font="arial 20 bold",command=lambda:btnClick(3)).grid(row=3,column=0)
b2=Button(root,text="2",padx=16,bd=8,font="arial 20 bold",command=lambda:btnClick(2)).grid(row=3,column=1)
b1=Button(root,text="1",padx=16,bd=8,font="arial 20 bold",command=lambda:btnClick(1)).grid(row=3,column=2)
mul=Button(root,text="*",padx=16,bd=8,font="arial 20 bold",command=lambda:btnClick("*")).grid(row=3,column=3)

b0=Button(root,text="0",padx=16,bd=8,font="arial 20 bold",command=lambda:btnClick(0)).grid(row=4,column=0)
bCr=Button(root,text="C",padx=16,bd=8,font="arial 20 bold",command=btnClear).grid(row=4,column=1)
bEq=Button(root,text="=",padx=16,bd=8,font="arial 20 bold",command=btnEqual).grid(row=4,column=2)
Div=Button(root,text="/",padx=16,bd=8,font="arial 20 bold",command=lambda:btnClick("/")).grid(row=4,column=3)






root.mainloop()
