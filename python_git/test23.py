import tkinter as tk

root=tk.Tk()

canvas1 = tk.Canvas(root, height=200, width=200)
canvas1.pack()

root.mainloop()

#pywhatkit message send
import pywhatkit as kit
kit.sendwhatmsg('+918800731826','this is anonymous',10,49)
#ARGS

def args(*args):
    print(type(args))
    if(len(args)== 3):
        print("student name is",args[0],"and his roll no is",args[1],"and his admission no is",args[2],)
    else:
        print("student name is",args[0],"and his roll",args[1],"and his admission",args[2],"and his marks is",args[3],)
lis = ["dummy",585737,352523235]

args(*lis)

#kwargs

def kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
    print(type(kwargs))
dummy123 = {"Dummy1":53252,"Dummy2":523523,"Dummy3":473}
kwargs(**dummy123)

