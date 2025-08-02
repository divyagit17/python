#dynamic shopping list
shopping_list = []

while True:
    print("\n choose an action to perform: add/ remove/view/exit")
    action = input("Enter action: ")

    if action == "add":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print("Added {item} to the shopping list.")

    elif action == "remove":
        item = input("Enter item to remove:")
        if item in shopping_list:
            shopping_list.remove(item)
            print("{item} removed from the shopping list.")

        else:
            print("Item not found in the shopping list.")

    elif action == "view":
        if shopping_list:
            print("shopping list items:")
            for item in shopping_list:
                print(item)
        else:
           print("print your shopping list is empty.")

    elif action == "exit":
        print("good bye!") 
        break     
    else:
        print("Invalid action. Please choose add, remove, view, or exit.")


  #students marks  
scores = []

score1 = int(input("enter score 1 (0-100):"))
scores.append(score1)

score2 = int(input("enter score 2 (0-100):"))
scores.append(score2)

score3 = int(input("enter score 3 (0-100):"))
scores.append(score3)

score4 = int(input("enter score 4 (0-100):"))
scores.append(score4)

score5 = int(input("enter score 5 (0-100):"))
scores.append(score5)

average = sum(scores)/len(scores)
highest = max(scores)
lowest = min(scores)

print("\nScores entered:", scores)
print("Average score:", average)
print("Highest score:", highest)
print("Lowest score:", lowest)

# city_coordinates.py
chennai = ("Chennai",(13.0827, 80.2707))
mumbai = ("Mumbai",(19.0760, 72.8777))
bangalore = ("Bangalore",(12.9716, 77.5946))
hyderabad = ("Hyderabad",(17.3850, 78.4867))
kolkata = ("Kolkata",(22.5726, 88.3639))

cites = [chennai, mumbai, bangalore, hyderabad, kolkata]
city_input = input("Enter the name of the city (chennai, mumbai, bangalore, hyderabad, kolkata): ")

if city_input == "chennai":
    print("Coordinates of Chennai: {chennai[1]}")
elif city_input == "mumbai":
    print("Coordinates of Mumbai: {mumbai[1]}")
elif city_input == "bangalore":
    print("Coordinates of Bangalore: {bangalore[1]}")
elif city_input == "hyderabad":
    print("Coordinates of Hyderabad: {hyderabad[1]}")
elif city_input == "kolkata":
    print("Coordinates of Kolkata: {kolkata[1]}")
else:
    print("City not found. Please enter a valid city name.")

# unique_word_counter.py
    sentence = input("Enter a sentence: ")

words = sentence.split()
lowercase_words =   [word.lower() for word in words]
unique_words = set(lowercase_words)


print("Number of unique words:", len(unique_words))
print("unique words found:")
for word in unique_words:
    print(word)


# inventory.py
    
inventory = {
    "Laptop": {"price": 1200, "stock": 50},
    "Mouse": {"price": 25, "stock": 200}
}

while True:
    print("\nChoose an action: view_stock / sell_item / add_stock / quit")
    action = input("Enter action: ")

    if action == "view_stock":
        print("\nCurrent Inventory:")
        for item, details in inventory.items():
            print(f"{item} - Price: ${details['price']}, Stock: {details['stock']}")

    elif action == "sell_item":
        item_name = input("Enter item name to sell: ")
        if item_name in inventory:
            try:
                quantity = int(input("Enter quantity to sell: "))
                if inventory[item_name]["stock"] >= quantity:
                    inventory[item_name]["stock"] -= quantity
                    print(f"Sold {quantity} {item_name}(s).")
                else:
                    print("Insufficient stock.")
            except ValueError:
                print("Invalid quantity.")
        else:
            print("Item not found.")

    elif action == "add_stock":
        item_name = input("Enter item name to restock: ")
        if item_name in inventory:
            try:
                quantity_to_add = int(input("Enter quantity to add: "))
                inventory[item_name]["stock"] += quantity_to_add
                print(f"Added {quantity_to_add} to {item_name} stock.")
            except ValueError:
                print("Invalid quantity.")
        else:
            print("Item not found.")

    elif action == "quit":
        print("Exiting inventory manager.")
        break

    else:
        print("Invalid action. Try again.")



# courses.py
        avaliable_courses= {"Math", "Physics", "Chemistry", "Biology", "Computer science", "History"}

completed_courses = set()

course1 = input("Enter completed course 1: ")
completed_courses.add(course1)

course2 = input("Enter completed course 2: ")
completed_courses.add(course2)

course3 = input("Enter completed course 3: ")
completed_courses.add(course3)

course4 = input("Enter completed course 4: ")
completed_courses.add(course4)

course5 = input("Enter completed course 5: ")
completed_courses.add(course5)

new_courses_to_enroll = avaliable_courses - completed_courses

print("courses to enroll in :")
for course in new_courses_to_enroll:
    print(course)