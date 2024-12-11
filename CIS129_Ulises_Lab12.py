"""
script: Pet Class
action: This code creates a pet class with the attributes name, type and age and allows users to enter their pets and
prints their pet.
name: Cesar Ulises Valenzuela
date: 12/11/24
"""

class Pet:
    # Initializes attributes
    def __init__(self, name="", pet_type="", age=0):
        self.name = name
        self.type = pet_type
        self.age = age

    # returns name, type and age
    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_age(self):
        return self.age

    # uses the parameter name and sets it to object name
    def set_name(self, name):
        self.name = name

    def set_type(self, pet_type):
        self.type = pet_type

    def set_age(self, age):
        self.age = age


def get_pet():
    """
    action: This function instantiates a pet object then prompts the user to enter their name, type and age then sets
    the input variable to their respective methods then prints the users pet according to what they inputted

    input: no args passed
    output: prints the prompt and the users pet
    return: no return
    """

    # instantiate pet object

    user_pet = Pet()

    # input prompts and sets input variable to respective method

    print("Enter your pet's name:")
    pet_name = input()
    user_pet.set_name(pet_name)

    print("Enter your pet's type:")
    pet_type = input()
    user_pet.set_type(pet_type)

    print("Enter your pet's age:")
    pet_age = int(input())
    user_pet.set_age(pet_age)

    # prints users pet using the get methods

    print(f"Your pet name: {user_pet.get_name().title()}")
    print(f"Your pet type: {user_pet.get_type().title()}")
    print(f"Your pet age: {user_pet.get_age()}")


# runs the function
get_pet()
