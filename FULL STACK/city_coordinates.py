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