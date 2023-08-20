#!/usr/bin/env python3
"""
class Dog:
    def __init__(self, name, favourite_toy="Any" ):
        print(f"{name} is born!")
        self.name = name
        self.favourite_toy = favourite_toy

    def bark(self):
        print("Woof!")

    def showing_self(self) -> None:
        return self

    def adopt(self, owner_name):
        self.owner = owner_name


tom = Dog("Fido")
snoopy = Dog("Snoopy", "Tennis Ball")
# print(tom.showing_self())
# print(tom)
# print(snoopy)
# print(snoopy.showing_self())
print(snoopy.name)
tom.bark()

# tom.owner = "Sophie"
# print(tom.owner)
tom.adopt("Sophie")
print(tom.owner)

print(tom.favourite_toy)
print(snoopy.favourite_toy)
"""
class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed
        