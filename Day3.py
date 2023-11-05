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


#year = int(input("Enter the Year : \n"))
#
#if year%4==0:
#    if year%100 == 0:
#        #print("Not a leap year")
##        if(year%400 == 0):
##            print("Leap year")
##        else:
##            print("not a leap year")
##    else:
##        print("Leap year")
##else:
##    print("Not a leap year")
#
#print("Welcome to pizza store\n")
#
#bill = 0
#
#size = input("Enter The Size S,M or L : \n")
#
#add_pepproni = input("ADD PEPPRONI Y or N : \n")
#
#extra_cheese = input("EXTRA CHEESE Y or N : \n")
#
#if size == "S":
#    bill += 15
#elif size == "M":
#    bill += 20
#elif size == "L":
#    bill += 25
#    
#if add_pepproni == "Y":
#    if size == "S":
#        bill +=2
#    else:
#        bill +=3
#        
#if extra_cheese == "Y":
#    bill +=1
#    
#print(f"Bill amount is {bill}")




#*********LOVE CALCULATOR*********#
#print("The Love Calculator is calculating your Score...\n")
#
#name1 = input("Enter Your Name : \n")
#name2 = input("Enter Partner Name : \n")
#combined_name = name1 + name2
#lower_name = combined_name.lower()
#t = lower_name.count("t")
#r = lower_name.count("r")
#u = lower_name.count("u")
#e = lower_name.count("e")
#
#firstDigit = t+r+u+e
#
#l = lower_name.count("l")
#o = lower_name.count("o")
#v = lower_name.count("v")
#e = lower_name.count("e")
#
#secondDigit = l+o+v+e
#
#score = int(str(firstDigit)+str(secondDigit))
#
#if score < 10 or score > 90:
#    print(f"Your score is {score}, You are like coke and Mentos \n")
#elif score>=40 and score <=50:
#    print(f"Your score is {score}, you are great together. \n")
#else:
#    print(f"Your Score is {score}. RUN!!!")
    
 


#********TREASURE GAME PUZZLE**********#
print("WELCOME TO THE GAME\n")
print("WELCOME TO THE TREASURE ISLAND. \n YOUR MISSION IS TO FIND THE HIDDEN TREASURE.")

choice1 = input("Your're at a Cross Road. Where do you want to go Type 'Right' or 'Left' : \n").lower()
if  choice1 == "left":
    choice2 = input("You come to a lake. There is an Island in the middle of the lake.  Type 'Wait' to wait for a boat. Type 'Swim' to swim across.\n").lower()
    if choice2 == "wait":
        choice3 = input("You arrive to the island unharmed. There is a house with 3 doors. One Red, One Yellow, and one blue. which colour do you choose.\n").lower()
        if choice3 == "red":
            print("you diied..")
        elif choice3 == "yellow":
            print("You won the game you found the treasure")
        elif choice3 == "blue":
            print("You died")
        else:
            print("wrong")
    else:
        print("You got attacked by animal. Game Over!!")
else:
    print("You fall into an hole. GAME OVER!!")




