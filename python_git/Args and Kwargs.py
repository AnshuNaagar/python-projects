# ? args and kwargs are

def function(*args): # ?  ? function assigned
    print(type(args)) # ?  ? printting args type which is tuple
    if(len(args)== 3): # ?  ? using if operator that is if the length of args is 3 then print the 3 valuse given below the print function
        print("Student Name is",args[0],"and roll no is",args[1],"and his age is" ,args[2],) # ? print function which conatins args operators.
    else: # ?  ? assigning the else operator that shows that if args parameter is 2 then this function will execute.
        print("Student Name is", args[0], "and roll no is", args[1],)# ? this is work for else function
lis = ["anshu",89,]# ?  ? using list function which works as showing output in list.
function (*lis)
# ?  ?function("anshu",7867) # ? calling the function with his name to print.

# ?  TODO Kwargs in python

def printmarks(**kwargs): # ? assigned a function called printmarks
    print(type(kwargs))# ? printing the type of the kwargs
    for key, value in kwargs.items():# ? using for and in function to print key and value downside.
        print(key, value)# ? printing the key value.
def king(normal, *args, **kwargs):# ? printing both args and kwargs in same function.
    print(normal)# ? first printing the normal function in the form of string.
    for i in args:# ? assigning i using for statement.
        print(i)# ? printing i
    for key, value in kwargs.items():# ? using for and key function same to print key and value.
        print(key, value)# ? print key value.
li2 = ["anshuman",58,]# ? this string for args
marks = {"dummy1" : 53,"dummy2": 57,"dummy3" : 75,"dummy4" : 79,}# ? making a variable which contains the marks of students This is for kwargs items.
# ? printmarks(**marks)# ? calling the function and variable.
king("normal arg", *li2, **marks)# ? Callling function with a normal string and args and kwargs.

