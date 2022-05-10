name = (input("enter your name : "))
print(f'hello,{name}')

n = (int(input("Enter your number : ")))
if n > 0:
    print("Is positive ")
elif n < 0:
    print('N is negative')
else:
    print("n is not positive")

#sequenzes in the python

names = ["harry" , "ron" , "harry2"]
print(names[0])
print(names[1])

#Storing a valuse in a single strings called args.
def args(*args):
    print(type(args))
    if(len(args)==3):
        print("student name is",args[0],"And his roll no is",args[1],"And his admission no is",args[3],)
    else:
        print("student name is",args[0],"And his roll no is",args[1],)
lis1 = ["Anshu",9]

args(*lis1)

#storing different values in a single string called kwargs .  (like storing student marks in a single stings just similar thing is called in to this funciton)

def kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
        print(type(kwargs))
dummy1 = {"dummy1":53,'dummy2':532,"Dummy3":4232,"dummy6":421}
kwargs(**dummy1)

#using args and kwargs in same function. (copy correct algorithm)

def printmarks(**kwargs): #assigned a function called printmarks
    print(type(kwargs))#printing the type of the kwargs
    for key, value in kwargs.items():#using for and in function to print key and value downside.
        print(key, value)#printing the key value.
def king(normal, *args, **kwargs):#printing both args and kwargs in same function.
    print(normal)#first printing the normal function in the form of string.
    for i in args:#assigning i using for statement.
        print(i)#printing i
    for key, value in kwargs.items():#using for and key function same to print key and value.
        print(key, value)#print key value.
li2 = ["anshuman",58,]#this string for args
marks = {"dummy1" : 53,"dummy2": 57,"dummy3" : 75,"dummy4" : 79,}#making a variable which contains the marks of students This is for kwargs items.
#printmarks(**marks)#calling the function and variable.
king("normal arg", *li2, **marks)#Callling function with a normal string and args and kwargs.

#making another function to assign an aonther kwargs
def printmark(**kwargs):
    print(type(kwargs))
    for i, value in kwargs.items():
        print(i,value)
lis = {"Dummy3":532,"Dummy5":532,"Dummo":8883,}
printmark(**lis)
#making another funcion and printing the same args and kwargs into a single function (self)
def io( *args,**kwargs):
    for i in args:
        print(i)
    for key,value in kwargs.items():
        print(key,value)
        print("Student name is",args[0],"And his roll no is",args[1],"Dummy5",args[2],)
lis0 = {"Dummy1" :532,"Dummy5":532,"def":5325,"Dummon":5321}
lisarg = ["Anshu",9,90]
io(*lis0,**lisarg)


#append function and sort algorithm defined a function then i runed into a function
def names():
    names = ["harry", "ron" , "Ginny" , "Draco"]
    print(names[0])
    names.append("draco23r")#adding an another name into the names list 
    names.sort()#sorting the names from this function
    print(names)#printing the names
names()

#sets code in python
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.remove(4)
print(s)
print(f"The set has {len(s)} elements")

#
any(none)


print("hello world")