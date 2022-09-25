class Shape:
    def __init__(self):
        self._length = 10
        self._breadth = 20

class Circle(Shape):
    def __init__(self):
        print('hello')
        Shape.__init__(self)
        print(self._length)
        print(self._breadth)
        
        

cr = Circle()

# cr._breadth=40
# cr._length=50
# print(cr._length)
# print(cr._breadth)


# class Shape:#protected variables
#     __length = 10
#     __breadth = 20
#
# class Circle(Shape):
#     def __init__(self):#printing protected variables in the derived class
#      print(self.__length)
#      print(self.__breadth)
#
# cr = Circle()

# print(cr.length)
# print(cr.breadth)