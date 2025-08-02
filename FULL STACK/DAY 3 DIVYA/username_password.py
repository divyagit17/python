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

