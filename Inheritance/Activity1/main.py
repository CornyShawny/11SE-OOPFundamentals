class Animal:
    def __init__(self, name):
        self.name = name

    def get_sound(self):
        print("undefined")

class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name)
        self.sound = sound