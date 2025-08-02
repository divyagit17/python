num = 1
while num <= 10:
    print( num)
    num += 1



# Ask the user to enter a number
n = int(input("Enter a positive number: "))


total = 0
i = 1


while i <= n:
    total += i
    i += 1

print("Sum from 1 to", n, "is:", total)


# Ask the user to enter a number
n = int(input("Enter a positive integer: "))

# Initialize result and counter
factorial = 1
i = 1

# Use while loop to calculate factorial
while i <= n:
    factorial *= i
    i += 1

# Print the result
print(f"{n}! = {factorial}")


# Get input from user
num = int(input("Enter a number: "))

# Initialize reversed number
reverse = 0

# While loop to reverse digits
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

# Print the reversed number
print("Reversed number:", reverse)


# Get input from user
num = int(input("Enter a positive number: "))

# Initialize digit count
count = 0

# Use while loop to count digits
while num > 0:
    num = num // 10
    count += 1

# Print the result
print("Total digits:", count)



import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Initialize guess
guess = 0

print("Guess the number between 1 and 10!")

# Keep asking until the guess is correct
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")

print("🎉 Correct! You guessed the number:", secret_number)


# Get input from the user
num = int(input("Enter a number: "))

# Store the original number for comparison
original = num
reverse = 0

# Reverse the number using while loop
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

# Check if original and reversed numbers are the same
if original == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")


# Get input from the user
num = int(input("Enter a number: "))

# Print the multiplication table from 1 to 10
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")



# Initial balance
balance = 1000

print("💳 Welcome to the ATM!")
print("Your starting balance is ₹1000")
print("Enter 0 to exit.")

while True:
    amount = int(input("Enter amount to withdraw: ₹"))

    if amount == 0:
        print("Thank you for using the ATM. Goodbye!")
        break
    elif amount > balance:
        print("Insufficient funds. Current balance: ₹", balance)
    elif amount < 0:
        print(" Invalid amount. Please enter a positive value.")
    else:
        balance -= amount
        print("Withdrawal successful. Remaining balance: ₹", balance)




