first_name = "Divya"
last_name= "Prashanth"
age = 25
is_enrolled = True
current_city = "coimbatore"
favorite_course = "python full stack development"
years_of_experience = "half a year"

my_variable = "favorite_course"
print(f"Original: {my_variable}, Type: {type(my_variable)}")


my_variable = 2025
print(f"New: {my_variable}, Type: {type(my_variable)}")

print("Hello, my name is", first_name, last_name, ". I am", age, "years old and live in", current_city, "." 
      " I am currently enrolled in", favorite_course, "and have", years_of_experience, "of experience.")


#here we can declare another variable with the same name as my_variable, but we cant declare the number as 
#variable name, like 2nd_variable = "something", here it will throw an error, when it becomes live.
# Variable names should not start with a number, but can contain numbers after the first character.
# Variable names can contain letters, numbers, and underscores, but cannot start with a number.