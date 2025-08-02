#calculator
item_price =  45.50
quantity = 3
total_cost = item_price * quantity
cost_per_person = item_price // 2
remainder = quantity % 2
discounted_price = item_price - 5.0
print( "$", total_cost)
print("$", cost_per_person )
print(remainder)
print(discounted_price)



#dynamic score
player_score = 100

player_score += 50
print("player_score after adding 50:", player_score)

player_score -= 20
print("player_score after subtracting 20:", player_score)

player_score *= 1.5
print("player_score after multiplying by 1.5:", player_score)

player_score /= 2
print("player_score after dividing by 2:", player_score)


#event eligibility checker
your_age = 19
has_ticket = True
is_vip = False
event_age_limit = 18

can_enter_standard_event = (your_age >= event_age_limit) and has_ticket
print(f"can enter standard event ? {can_enter_standard_event } # ({your_age} >= {event_age_limit} is {your_age >= event_age_limit}) AND ({has_ticket} is True) -> {can_enter_standard_event}")

can_enter_vip_lounge = is_vip or (your_age >= 21)
print(f"can enter VIP lounge ? {can_enter_vip_lounge }  # ({is_vip} is True) OR ({your_age} >= 21 is {your_age >= 21}) -> {can_enter_vip_lounge}")

is_denied_entry = not (can_enter_standard_event)
print(f"denied entry ? {is_denied_entry }   # NOT ({can_enter_standard_event}) -> {is_denied_entry}")



#username and  password validator
valid_users = ["admin", "guest", "moderator"]
user_input_username = "Guest"
user_input_password = "P@ssw0rd123"

username_lower = user_input_username.lower()

is_valid_user = username_lower in valid_users
print(f"is '{username_lower}'a valid user? {is_valid_user}")

is_not_valid_user = username_lower not in valid_users
print(f" is not '{username_lower}' a valid user? {is_not_valid_user}")

cleaned_password = user_input_password.strip().lower()
print(f"cleaned password : '{cleaned_password}' ")




#mixed type greeting string
product_name = "laptop"
price  = 799.99
discount_price = 10
print(f"Today's special : The {product_name} is now only $ {price}! you get a {discount_price}% discount")
