meal_cost = 55.75
tax_rate = 0.08
tip_percentage = 0.15
num_diners = 3

tax_amount = meal_cost * tax_rate
total_before_tip = meal_cost + tax_amount
tip_amount= total_before_tip * tip_percentage
final_bill = total_before_tip + tip_amount
cost_per_diner = final_bill / num_diners

print(f"Meal cost: ${meal_cost:.2f}")
print(f"Tax amount: ${tax_amount:.2f}")
print(f"Total before tip: ${total_before_tip:.2f}")
print(f"Tip amount: ${tip_amount:.2f}")
print(f"Total bill: ${final_bill:.2f}")
print(f"Total cost per diner: ${cost_per_diner:.2f}")

final_bill += 2.50
print(f"Final bill after adding $2.50: ${final_bill:.2f}")

