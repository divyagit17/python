# name_1 = "Abinash"
# age_1 = 25
# height_1 = 5.8
# weight_1 = 70.5


# name_2 = "Sanjay"
# age_2 = 30
# height_2 = 6.0
# weight_2 = 80.0

# def eating(name):
#     print(f"{name} is eating healthy food.")

# def study(name):
#     print(f"{name} is studying for exams.")  

# eating(name_1)
# study(name_1)    
# eating(name_2)
# # study(name_2)  

# class students:
#     def __init__(self,name,age,height,weight):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight
#     def eating(self):
#         print(f"{self.name} is eating healthy food.")

#     def study(self):
#         print(f"{self.name} is studying for exams.")

# student_1 = students("Divya", 28, 5.5, 65.0)

# student_1.eating()
# student_1.study()

class Dog:
    species = "Labrador"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

dog_name    = input("Enter the dog's name: ")  
dog_age = int(input("Enter the dog's age: "))
dog1 = Dog(dog_name, dog_age)

print(dog1.name)
print(dog1.age)

dog1.bark()
