name = (input("Enter your Name : ")) #here input take of a person in characters 
Height_m = float(input("Enter your height In meters : ")) #here height taken in float program
Weight_kg = float(input("Enter your weight in Kilograms : " ))#here weight taken in float program
bmi = Height_m / (Weight_kg ** 2) #assigning a dividor formula
print(name, +bmi)#printing name and bmi
if bmi > 15: #using if function.
    print(name, "is Not Overweight  : " ,+bmi  )
else: #using else function
    if bmi < 20:
            print(name, "is overweight : " ,+bmi  )
            