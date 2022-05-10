try:
    open("this.txt")
except Exception as e:
    print(e)
print("The program is alive")

try:
    file = open("this.txt",'r')
except EOFError as e:
    print(e)
    print("EOFError")
except IOError as e:
    print("This is an irrespective error as IOError.")
finally:
    print("This is the one of the most of the follwing ways.")
try:
    print("This can't able to run the else and if block how can i fix it")
except Exception as e:
    print("This code can't able to repair it.")
else:
    print("this code is cant able fix properly and it can't able to repair it.")
finally:
    print('this statement will run in all the excepton and make it properly')

    