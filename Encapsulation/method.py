# class Car:
#     def __init__(self):
#          self.__updatesoftware()
#     def drive(self):
#         print('Driving')
#     def __updatesoftware(self):
#         print("updating software")

# obj=Car()
# obj.drive()
# obj.__updatesoftware()


class Car:
    def __init__(self):
        self.__updatesoftware()

    def drive(self):
        print('Driving')
    
    def __updatesoftware(self):
        print('updating software')

obj = Car()
obj.drive()
# obj.__updatesoftware()