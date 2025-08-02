product_name = "wireless charger"
stock_count = 10
customer_age = 20
is_premium_member = False 
min_age_for_discount = 18
available_sizes = ["s","m","l"]

stock_check = stock_count > 0
print("is product in stock:", stock_check)

customer_eligible_age = customer_age >= min_age_for_discount
print("is customer eligible for discount:", customer_eligible_age)

discount_eligibility = is_premium_member or customer_age > 65
print("is customer eligible for senior / premium discount:", discount_eligibility)

product_discount = product_name== "wireless charger" and  stock_check < 5
print("special low stock discount :", product_discount)

is_avaliable_size = "xl" in available_sizes
print("is size available:", is_avaliable_size)

list_a = [1, 2, 3]
list_b = list_a
list_c = [1, 2, 3]
print("is list_a same as list_b:", list_a is list_b)
print("is list_a same as list_c:", list_a is list_c)

