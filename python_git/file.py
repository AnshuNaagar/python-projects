name = input("Enter the canidiate name : ")
height_m = float(input("Enter the canidiate Height In meters : "))
weight_kg = float(input("Enter the Canidiate weight in Kilograms : "))

def bmi():
    bmi = weight_kg/(height_m**2)
    print(name,bmi)
    if bmi > 2:
        print(name,"Is overweight because his bmi is : ",bmi)
    else:
        print(bmi,"Is not overweight because his bmi is : ",bmi)
    if bmi == 2:
        print(name,"weight is same as recommendation",bmi)

bmi()

def args(*args):
    if(len(args)==3):
        print("Student Name is",args[0],"And his roll no is",args[1],"and his roll no is",args[2],)
    else:
        print("Student Name is",args[0],"And his roll no is",args[1],"and his roll no is",args[2],"and his marks is",args[3])
    if(len(args)==3):
        print("student Name is",args[0],"And his roll no is",args[1])

lis = ["Anshu",42,8347]

args(*lis)

#args code will end here.

#kwargs code will start here.

def kwargs(**kwrargs):
    for key,value in kwrargs.items():
        print(key,value)
        print(type(kwargs))
lis2 = {"Dummy one":53,"Dumy two":54,"Dumy three":57,"Dumy four":532,}
kwargs(**lis2)
    
#tkinter calculaor inside of items









