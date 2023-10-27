from tkinter import*
def clicked(num):
    start_no=txt.get()
    txt.delete(0,END)
    txt.insert(0,str(start_no)+str(num))
def add():
    first_number=txt.get()   
    global old_value
    old_value=int(first_number)
    global math
    math="add"
    txt.delete(0,END)
def sub():
    first_number=txt.get()   
    global old_value
    old_value=int(first_number)
    global math
    math="sub"
    txt.delete(0,END)
def mul():
    first_number=txt.get()   
    global old_value
    old_value=int(first_number)
    global math
    math="mul"
    txt.delete(0,END)
def div():
    first_number=txt.get()   
    global old_value
    old_value=int(first_number)
    global math
    math="div"
    txt.delete(0,END)
def equal():
    if math=="add":
        new_value=txt.get()
        txt.delete(0,END)
        txt.insert(0,int(old_value)+int(new_value))
    elif math=="sub":
        new_value=txt.get()
        txt.delete(0,END)
        txt.insert(0,int(old_value)-int(new_value))
    elif math=="div":
        new_value=txt.get()
        txt.delete(0,END)
        txt.insert(0,int(old_value)/int(new_value))
    elif math=="mul":
        new_value=txt.get()
        txt.delete(0,END)
        txt.insert(0,int(old_value)*int(new_value)) 
def clr():
    txt.delete(0,END)   
        
root=Tk()
root.geometry("200x400")
root.title("calculator")
root.resizable(False,False)
root.configure(background="black")
root.attributes("-alpha",0.9)
root.attributes("-topmost",True)
txt=Entry()
txt.place(x=25,y=80)
btn=Button(text="%").place(x=25,y=150)
clr=Button(text="CE",command=clr)
clr.place(x=50,y=150)
btn1=Button(text="C").place(x=80,y=150)
btn=Button(text="1/X").place(x=25,y=180)
btn1=Button(text="x2").place(x=55,y=180)
btn1=Button(text="2/x").place(x=80,y=180)
div=Button(text="/",command=div)
div.place(x=110,y=180)
btn7=Button(text="7",command=lambda:clicked(7))
btn7.place(x=25,y=210)
btn8=Button(text="8",command=lambda:clicked(8))
btn8.place(x=53,y=210)
btn9=Button(text="9",command=lambda:clicked(9))
btn9.place(x=80,y=210)
mul=Button(text="*",command=mul)
mul.place(x=110,y=210)
btn4=Button(text="4",command=lambda:clicked(4))
btn4.place(x=25,y=240)
btn5=Button(text="5",command=lambda:clicked(5))
btn5.place(x=53,y=240)
btn6=Button(text="6",command=lambda:clicked(6))
btn6.place(x=80,y=240)
sub=Button(text="-",command=sub)
sub.place(x=110,y=240)
btn1=Button(text="1",command=lambda:clicked(1))
btn1.place(x=25,y=270)
btn2=Button(text="2",command=lambda:clicked(2))
btn2.place(x=53,y=270)
btn3=Button(text="3",command=lambda:clicked(3))
btn3.place(x=80,y=270)
add=Button(text="+",command=add)
add.place(x=107,y=270)
btn=Button(text="+/-").place(x=25,y=300)
btn0=Button(text="0",command=lambda:clicked(0))
btn0.place(x=60,y=300)
btn1=Button(text=".").place(x=85,y=300)
eqaul=Button(text="=",command=equal)
eqaul.place(x=107,y=300)
root.mainloop()