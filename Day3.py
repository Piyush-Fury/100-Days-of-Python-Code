#TICKET COUNTER
#height = int(input("Enter your height in CM : \n"))
#age = int(input("What's your age"))
#if height>=120:
#    if age>=18:
#        print("Yes you can Ride")
#        print("$12")
#    else:
#        print("Sorry you are not allowed people above 18 only")
#else:
#    print("You are short not allowed!!")

#ODD EVEN CHECK
#num = int(input("Enter The Number : \n"))
#print(type(num))
#
#if int(num%2==0):
#    print("Even number")
#else:
#    print("ODD ")
#
#
##BMI CALCULATOR 2.O
#height = float(input("Enter your Height in meters : \n"))
#
#weight = float(input("Enter your weight : \n"))
#
#bmi = weight/height ** 2
#
#print(bmi)
#
#if(bmi<18.5):
#    print("Underweight")
#elif(bmi<25):
#    print("Normal weight")
#elif(bmi<30):
#    print("slightly overweight")
#elif(bmi<35):
#    print("overweight")
#else:
#    print("Clinincally Obese")


year = int(input("Enter the Year : \n"))

if year%4==0:
    if year%100 == 0:
        #print("Not a leap year")
        if(year%400 == 0):
            print("Leap year")
        else:
            print("not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")