#AGE
age = int(input("enter age:"))
if age <=5:
    print("FREE ENTRY FOR TOODLERS IN  THEME PARK")

#MARKS
marks = int(input("Enter your marks: "))
if marks >= 50:   
  print("PASS") 
else:
   print("FAIL")

#TRAFFIC_LIGHT_SYSTEM
traffic_light = input("Enter the traffic light color (red, yellow, green): ").lower()
if traffic_light == "red":
    print("STOP! DO NOT PROCEED")
elif traffic_light == "yellow":
    print("PREPARE TO STOP!")
elif traffic_light == "green":
    print("GO! YOU CAN PROCEED")
else:
    print("INVALID COLOR")


#movie ticket pricing
age = int(input("Enter your age: "))
if age < 12:   
    print("Ticket price: $5")
elif age >= 12 and age < 17:
    print("Ticket price: $8") 
elif age >= 18 and age < 64:
    print("Ticket price: $12")
elif age >= 65:
    print("Ticket price: $7")
else:
    print("Invalid age entered.")


#simple calculator?
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
if operation == "+":
     result = num1 + num2
     print(f"Result: {result}")
elif operation == "-":
     result = num1 - num2
     print(f"Result: {result}")
elif operation == "*":
     result = num1 * num2
     print(f"Result: {result}")
elif operation == "/":
     if num2 != 0:
         result = num1 / num2
         print(f"Result: {result}")
     else:
         print("Error: Division by zero is not allowed.")



# Loan Eligibility Checker

# Get user input
income = float(input("Enter your annual income in dollars: "))
credit_score = int(input("Enter your credit score: "))

# Check loan eligibility using nested if
if income >= 30000:
    if credit_score >= 650:
        print("Eligible for Loan")
    else:
        print("Income good, but credit score too low")
else:
    if credit_score >= 650:
        print("Credit score good, but income too low")
    else:
        print("Not eligible for loan")

#online store discount
purchase_amount = float(input("Enter the purchase amount: $"))
membership_status = input("Are you a member? (yes/no): ").lower()
if purchase_amount >= 50:
    if membership_status == "yes"  and purchase_amount >= 100:
        discount = 0.15 # 15% discount for members
    else:
        discount = 0.10  # 10% discount for non-members

else:
    discount = 0.0

discounted_amount = purchase_amount * discount
final_amount = purchase_amount - discounted_amount
    

print(f"Discount applied: {discount * 100:}%")
print(f"Final price after discount: ${final_amount:}")


#quadrant identifier
x=float(input("Enter the x-coordinate: "))
y=float(input("Enter the y-coordinate: "))  
if x > 0 and y > 0:
    print("Point is in Quadrant I")
elif x < 0 and y > 0:
    print("Point is in Quadrant II")
elif x < 0 and y < 0:
    print("Point is in Quadrant III")
elif x > 0 and y < 0:
    print("Point is in Quadrant IV")
else:
    print("Point is on axis (0, 0)")


# Leap Year Checker
year = int(input("Enter a year: "))

# Use a complex if condition
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


#resturant  order checker
main_course = input("Enter the main course (pizza, pasta, burger): ").lower()
drinks = input("Enter the drink (coke, juice, water): ").lower()

valid_main_courses = ["pizza", "pasta", "burger"]
valid_drinks = ["coke", "juice", "water"]

if main_course in valid_main_courses :
    if  drinks in valid_drinks:
       print(f"Your order: {main_course} with {drinks}. total : $15")
    else:
       print(f"Invalid drink. Only {main_course} ordered. Total: $10.")
else:
    print("Invalid main course.") 




