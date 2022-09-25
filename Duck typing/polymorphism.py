## Duck Typing philosophy


class Duck:
    def talk(self):
        print("Quack Quack")
    def bark(self):
        print("bow bow")
class Dog:pass

def f1(obj):
    if hasattr(obj,"talk"):
        obj.talk()
    elif hasattr(obj,"bark"):
        obj.bark()

d1 = Dog()
c = Duck()
f1(c)


# class Duck: 
#     def swim_quack(self):
#         print("I'm a duck, and I can swim and quack.")

# class RoboticBird:
#     def swim_quack(self):
#         print("I'm a robotic bird, and I can swim and quack.")

# class Fish:
#     def swim(self):
#         print("I'm a fish, and I can swim, but not quack.")

# def duck_testing(animal):
#     animal.swim_quack()

# duck_testing(Duck())
# duck_testing(RoboticBird())
# duck_testing(Fish())



