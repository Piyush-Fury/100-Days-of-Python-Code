#num_char = len(input("What is your name : \n"))

#new_num_char = str(num_char)

#print("Your name has " + new_num_char + " characters")


#num = input("Enter a 2 digit number : \n")
#print(type(num))
#print(int(num[0])+int(num[1]))


#BMI CALCULATOR
#height = float(input("Enter your Height in meters : \n"))
#
#weight = float(input("Enter your weight : \n"))
#
#bmi = weight/height ** 2
#
#print(bmi)


#week calcultor

#total_week = 4680
#1 year = 52.146
#current_age = int(input("Enter Your age : \n"))
#year_left = total_week/52 - current_age
#week_left = round(year_left * 52, 2)
#print(f"You have {week_left} Weeks left")


#TIP CALCULATOR#

print("This is an Tip calculator")

bill = float(input("Enter the bill amount : \n"))

people = float(input("Enter the total number of peoples : \n"))

tip = float(input("Tip percentage 10%, 12%, 15% : \n"))

total_amount = round((tip/100 * bill) + bill,2)

split_amount = round(total_amount/people, 2)

print("\n")

print(f"Bill amount is {bill} \n\ntip is {tip}% \n\nTotal amount is {total_amount} \n\namount payable by each person is {split_amount}\n\n")