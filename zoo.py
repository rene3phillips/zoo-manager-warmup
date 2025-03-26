class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Generic animal sound.")

class Dog(Animal):
    def make_sound(self):
        print("Bark! I'm", self.name)

class Cat(Animal):
    def make_sound(self):
        print("Meow! I'm", self.name)

if __name__ == "__main__":
    dog = Dog("Rex", "Canine")
    cat = Cat("Mittens", "Feline")

    dog.make_sound()
    cat.make_sound()