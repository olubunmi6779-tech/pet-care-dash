# Parent Class
class Pet:
    def __init__(self, name, age, health):
        self.name = name
        self.age = age
        self.__health = health  # Encapsulated (private)

    # Getter
    def get_health(self):
        return self.__health

    # Setter
    def set_health(self, new_health):
        if 0 <= new_health <= 200:
            self.__health = new_health
        else:
            print("Health must be between 0 and 200.")

    # Method to override
    def display_info(self):
        print(f"Pet Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Health: {self.__health}")


# Child Class - Dog
class Dog(Pet):
    def __init__(self, name, age, health, breed):
        super().__init__(name, age, health)
        self.breed = breed

    def display_info(self):
        print("🐶 Dog Information")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Breed: {self.breed}")
        print(f"Health: {self.get_health()}")
        print()


# Child Class - Cat
class Cat(Pet):
    def __init__(self, name, age, health, color):
        super().__init__(name, age, health)
        self.color = color

    def display_info(self):
        print("🐱 Cat Information")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Color: {self.color}")
        print(f"Health: {self.get_health()}")
        print()


# Child Class - Bird
class Bird(Pet):
    def __init__(self, name, age, health, species):
        super().__init__(name, age, health)
        self.species = species

    def display_info(self):
        print("🐦 Bird Information")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Species: {self.species}")
        print(f"Health: {self.get_health()}")
        print()


# Creating Objects
dog = Dog("Tae", 2, 90, "Golden Retriever")
cat = Cat("JK", 2, 85, "White")
bird = Bird("jimin,", 1, 95, "Parrot")

# Updating health using setter
dog.set_health(92)
cat.set_health(88)
bird.set_health(97)

# List of pets
pets = [dog, cat, bird]

# Polymorphism using loop
print("===== MY PET CARE DASHBOARD =====\n")

for pet in pets:
    pet.display_info()