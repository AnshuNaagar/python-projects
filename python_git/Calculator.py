name = "nick"
height_m = 31
weight_kg = 32

bmi = height_m / (weight_kg * weight_kg)
print(bmi)
print(name)
print("nick bmi of his health")

if bmi < 90.0:
    print(name)
    print("is not healthy")
else:
    if bmi > 90.0:
        print(name)
        print('is healthy')

if 5 > 3:
    print("both values are not same")
    print("make sure you enter the correct value otherwise there is an error.")
print("here the programm")

name = "this is a name"
print(name)
print("is this the value")

j = 0
w = 0
print(type(j))
print(type(w))

print("type command")

print("type")


# new tutorial for

# a collection of instructions
# a collection of code

def function1():  # use the function code to new type of code
    print("this is a function1")
    print("this is the outside part of the code")


print("this is also a outside part of the code")

function1()  # it prints the function code


def function24324():
    print("function 1")
    print("fuckit")


print("mass fuckit")  # this is the outside part of the function code

function24324()
print("hello world!")

b = 73
print(b)
print("b is configured to add a new time of the following way")

u = 42
i = 23

if u > i:
    print("u is greater than 2")
    print("i think u is greater than i")
m = 9  # m contains this value
q = 8  # q contains this value

if m > q:  # checking if m is greater than q
    print("m is greater than q")  # final statement.

poij = 866
print(poij)
print("poij contains this value")  # final statement.

pq = 5132
print(pq)
print("pq contains this value")  # final statement.

if poij > pq:  # checking if poij is greater than
    print("poij is greater than his another value")
else:  # checking if point contains the value of any another values
    print("point contain value fallen down and it cannot start yet")

re = 2112
print(re)
print("re contains value in integer format")

yu = 2112
print(yu)
print("yu contains value in integer format")

if re == yu:  # checking if the both of the numbers are same or not...
    print("successful")
else:  # checking if the comment is the same or not...
    print("unsuccessful")

# next perfrom of the code

e = 3  # value stored in this integer
print(e)  # execution
print("e contains this value")  # value printed with this string.

r = 4  # value stored in this integer
print(r)  # execution of the value
print("r contains this value")  # value printed with this string.

if e > r:  # checking if e is greater than r.
    print("e i greater than r")  # string printed with this string
elif e == r:  # checking if e is equal to r
    print("e is equal than r than r")  # string
else:  # else statement
    print("e is smaller than r")

q = 99
w = 788
if q > w:
    print("q is greater than w")
else:
    if q == w:
        print("q is greater than w")
    else:
        if q < w:
            print("q is greater than w")
# measuring the weight of a preson
name = "anshu"
height_m = 5
weight_kg = 90

if height_m < weight_kg:
    print("that person is unfit")
else:
    height_m == weight_kg
    print("that person is healthy weight ")

# another way to calculate the weight of a person using a bmi calculator
name = "anshu"
height_m = 5
weight_kg = 115

bmi = weight_kg / (height_m ** 2)
print("bmi:")
print(bmi)

if bmi > 4.9:
    print(name)
    print("is not overweight")
else:
    if bmi < 4.9:
        print(name)
        print("is overweight")
import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()

entry1 = tk.Entry(root)
canvas1.create_window(210, 100, window=entry1)

entry2 = tk.Entry(root)
canvas1.create_window(210, 140, window=entry2)

entry3 = tk.Entry(root)
canvas1.create_window(210, 240, window=entry3)

label0 = tk.Label(root, text='Calculator made by Anshu')
label0.config(font=('helvetica', 14))
canvas1.create_window(150, 40, window=label0)

label1 = tk.Label(root, text='Type Value 1:')
label1.config(font=('helvetica', 10))
canvas1.create_window(100, 100, window=label1)

label2 = tk.Label(root, text='Type Value 2:')
label2.config(font=('helvetica', 10))
canvas1.create_window(100, 140, window=label2)

label3 = tk.Label(root, text='Result:')
label3.config(font=('helvetica', 10))
canvas1.create_window(100, 240, window=label3)


def add():
    v1 = entry1.get()
    v2 = entry2.get()

    label4 = tk.Label(root, text=float(v1) + float(v2), font=('helvetica', 10, 'bold'), bg='white')
    canvas1.create_window(210, 240, window=label4)


buttonAdd = tk.Button(text='+', command=add, bg='green', fg='white', font=('helvetica', 9, 'bold'), width=5)
canvas1.create_window(90, 190, window=buttonAdd)


def sub():
    v1 = entry1.get()
    v2 = entry2.get()

    label5 = tk.Label(root, text=float(v1) - float(v2), font=('helvetica', 10, 'bold'), bg='white')
    canvas1.create_window(210, 240, window=label5)


buttonSub = tk.Button(text='–', command=sub, bg='green', fg='white', font=('helvetica', 9, 'bold'), width=5)
canvas1.create_window(140, 190, window=buttonSub)


def mul():
    v1 = entry1.get()
    v2 = entry2.get()

    label6 = tk.Label(root, text=float(v1) * float(v2), font=('helvetica', 10, 'bold'), bg='white')
    canvas1.create_window(210, 240, window=label6)


buttonMul = tk.Button(text='x', command=mul, bg='green', fg='white', font=('helvetica', 9, 'bold'), width=5)
canvas1.create_window(190, 190, window=buttonMul)


def div():
    v1 = entry1.get()
    v2 = entry2.get()

    label7 = tk.Label(root, text=float(v1) / float(v2), font=('helvetica', 10, 'bold'), bg='white')
    canvas1.create_window(210, 240, window=label7)


buttonDiv = tk.Button(text='/', command=div, bg='green', fg='white', font=('helvetica', 9, 'bold'), width=5)
canvas1.create_window(240, 190, window=buttonDiv)

root.mainloop()


