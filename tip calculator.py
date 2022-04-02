#If the bill was $150.00, split between 5 people, with 12% tip. 
bill = int(input("enter the total bill: "))
no_of_person = int(input("enter the number of people to split the bill: "))
tip = int(input("enter the percentage of tip u want to give 10%, 12%, or 15%: "))
per_tip = (tip / 100) + 1

#Each person should pay (150.00 / 5) * 1.12 = 33.6

each_to_pay = round((bill / no_of_person) * per_tip, 2)
print(f"each person will pay ${each_to_pay}")
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇