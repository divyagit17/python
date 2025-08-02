raw_name_input = "  john Doe  "
raw_age_input = "28"

cleaned_name = raw_name_input.strip().title()
age_number = int(raw_age_input)

print(f"hello {cleaned_name}, you are {age_number} years old.")

print("first three letters of cleaned name :", cleaned_name[:3])
print(" second letter to end of cleaned name :", cleaned_name[1:])
print(" last two  letters of the name :",cleaned_name [-2:])

contains_a ="a" in cleaned_name.lower()
print("does the name contain letter 'a':", contains_a)

