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


