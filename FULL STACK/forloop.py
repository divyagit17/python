def energy_summary(hourly_readings):
    if len(hourly_readings) != 24:
        print("Error: Please provide exactly 24 hourly readings.")
        return

    total_consumption = 0
    highest_consumption = hourly_readings[0]
    peak_hour = 0

    for hour in range(24):
        reading = hourly_readings[hour]
        total_consumption += reading

        if reading > highest_consumption:
            highest_consumption = reading
            peak_hour = hour

    print("\n--- Daily Consumption Summary ---")
    print(f"Total energy consumed: {total_consumption:.2f} kWh")
    print(f"Highest hourly consumption: {highest_consumption:.2f} kWh")
    print(f"Occurred at hour: {peak_hour}")

def identify_peak_hours(hourly_readings, threshold):
    print(f"\n--- Peak Hours (Threshold = {threshold} kWh) ---")
    for hour in range(24):
        if hourly_readings[hour] > threshold:
            print(f"Hour {hour}: {hourly_readings[hour]:.2f} kWh")

# Example input
hourly_data = [
    0.5, 0.7, 0.6, 0.4, 0.3, 0.5, 0.9, 1.2,
    1.0, 1.1, 0.8, 0.6, 0.7, 1.3, 1.5, 0.9,
    0.6, 0.5, 1.4, 1.1, 0.7, 0.4, 0.3, 0.6
]

threshold = 1.0

# Run the analysis
energy_summary(hourly_data)
identify_peak_hours(hourly_data, threshold)



#online store alignment
order_ids = ["ORD001", "ORD002", "ORD003", "ORD004", ]

print(" --- Basic order processing system---")
for order_id in order_ids:
    print(f"Processing order {order_id}...")



orders = [
    {"id": "ORD005", "items": ["Laptop", "Mouse"], "status": "pending"},
    {"id": "ORD006", "items": [], "status": "pending"},
    {"id": "ORD007", "items": ["Keyboard"], "status": "shipped"},
    {"id": "ORD008", "items": ["Monitor"], "status": "pending"},
    {"id": "ORD009", "items": ["Phone Case"], "status": "cancelled"}
]

fulfilled_count = 0

print("\n--- Order Validation & Fulfillment ---")
for i in range(len(orders)):
    order = orders[i]
    order_id = order["id"]
    items = order["items"]
    status = order["status"]

    # Skip already shipped or cancelled
    if status == "shipped" or status == "cancelled":
        print("Skipping order", order_id, ": already", status + ".")
        continue

    # Skip empty item list
    if len(items) == 0:
        print("Order", order_id, "is empty, skipping.")
        continue

    # Fulfill the order
    print("Fulfilling order", order_id, "with items:", items)
    orders[i]["status"] = "fulfilled"
    fulfilled_count += 1

print("\nTotal orders fulfilled:", fulfilled_count)





# List of temperature readings
temperature_readings = [25.1, 26.5, 24.9, 150.2, 27.0, -10.5, 25.8, "error", 39.9, -50]

valid_min = -20.0
valid_max = 40.0
invalid_count = 0

print("--- Valid Temperature Readings ---")
for i in range(len(temperature_readings)):
    reading = temperature_readings[i]

    # Check if reading is a number
    if type(reading) == float or type(reading) == int:
        if reading >= valid_min and reading <= valid_max:
            print(reading, "°C")
        else:
            invalid_count += 1
    else:
        invalid_count += 1

print("Total invalid readings:", invalid_count)

temperature_readings = [150.2, -100, "sensor error", "N/A", -25, 25.0, 28.4]

valid_min = -20.0
valid_max = 40.0
found = False

print("\n--- First Valid Temperature Reading ---")
for i in range(len(temperature_readings)):
    reading = temperature_readings[i]

    # Check if it's a number
    if type(reading) == float or type(reading) == int:
        if reading >= valid_min and reading <= valid_max:
            print("First valid reading:", reading, "°C")
            found = True
            break

if not found:
    print("No valid temperature reading found.")




import random

# List of product serial numbers
products = ["P001", "P002", "P003", "P004", "P005"]

# Inspection stages
stages = ["Stage 1", "Stage 2", "Stage 3"]

# Lists to track results
passed_products = []
rework_products = []

print("--- Product Inspection Start ---")
for i in range(len(products)):
    serial = products[i]
    print("Inspecting product", serial, "...")

    failed = False  # Flag to check if product failed

    for j in range(len(stages)):
        stage_number = j + 1
        print(" - Checking", stages[j], "...")

        # 20% chance of failure
        chance = random.randint(1, 100)
        if chance <= 20:
            print("Product", serial, "FAILED at Stage", stage_number, "! Sending to rework.")
            rework_products.append(serial)
            failed = True
            break

    if not failed:
        print("Product", serial, "PASSED all inspections!")
        passed_products.append(serial)

# Final results
print("\n--- End of Day Summary ---")
print("✅ Passed Products:")
for i in range(len(passed_products)):
    print("-", passed_products[i])

print("\n🔧 Rework Products:")
for i in range(len(rework_products)):
    print("-", rework_products[i])




# Communication channel monitoring
channel_statuses = ["active", "active", "inactive", "error", "active"]

print("--- Channel Status Monitoring ---")
for i in range(len(channel_statuses)):
    status = channel_statuses[i]
    print("Channel", i + 1, "status:", status)

    if status == "error":
        print("Critical error found on a channel! Shutting down monitoring.")
        break

channel_statuses = ["active", "active", "active", "active"]  # Try changing to test

print("\n--- Checking if All Channels Are Active ---")
all_active = True

for i in range(len(channel_statuses)):
    if channel_statuses[i] != "active":
        print("Warning: Not all channels are active. Review required.")
        all_active = False
        break

if all_active:
    print("All communication channels are operational.")



# Basic for loop examples
n = 4
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()
# This code prints a square pattern of asterisks with size n x n

n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()
# This code prints a right-angled triangle pattern of asterisks with height n

n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")  # Print spaces
    for k in range(i):
        print("*", end="")  # Print stars
    print()
# This code prints a right-angled triangle pattern of asterisks with height n, aligned to the right

n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
# This code prints an inverted right-angled triangle pattern of asterisks with height n




#basic number operations
n = int(input("Enter a positive integer: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum of first", n, "natural numbers is:", total)
# This code calculates the sum of the first n natural numbers using a for loop

num = int(input("Enter a positive integer: "))
original = num
count = 0

# Using for loop by looping till number becomes 0
for i in range(len(str(num))):  # Loop length based on string length
    if num == 0:
        break
    num = num // 10
    count += 1

print("Total number of digits in", original, "is:", count)
# This code counts the number of digits in a positive integer using a for loop


num = int(input("Enter a positive integer: "))
reverse = ""

num_str = str(num)

for i in range(len(num_str)-1, -1, -1):
    reverse += num_str[i]

print("Reversed number is:", reverse)
# This code reverses a positive integer using a for loop by iterating through the string representation of the number

number = int(input("Enter the number: "))
count = int(input("Enter how many multiples to print: "))

for i in range(1, count + 1):
    print(number * i, end=" ")


num = int(input("Enter a positive integer: "))
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("Is Prime")
else:
    print("Is Not Prime")
# This code checks if a positive integer is prime using a for loop by checking divisibility from 2 to num-1






