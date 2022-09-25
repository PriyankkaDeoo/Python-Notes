## operator overloading
# Example 1
# class Book:
#     def __init__(self,pages):
#         self.pages = pages
#     def __add__(self,other):
#         return self.pages+other.pages
#     def __mul__(self, other):
#         return self.pages-other.pages

# b = Book(100)
# c = Book(200)
# print(b+c)
# print(b*c)


# Example 2
# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def __gt__(self, other):
#         return self.marks>other.marks
#     def __ge__(self, other):
#         return self.marks>=other.marks
#     def __lt__(self, other):
#         return self.marks<other.marks
#     def __le__(self, other):
#         return self.marks<=other.marks

# s1 = Student("shubham",100)
# s2 = Student("pratik",200)
# print("s1>s2:",s1>s2)
# print("s1>=s2:",s1>=s2)
# print("s1<s2:",s1<s2)
# print("s1<=s2:",s1<=s2)

# Example 3
# class Book:
#     def __init__(self,pages):
#         self.pages = pages
#     def __add__(self,other):
#         print("add method calling....")
#         total = self.pages+other.pages
#         return Book(total)
#     def __str__(self):
#         print("str method calling....")
#         return str(self.pages)

# b1 = Book(100)
# b2 = Book(200)
# b3 = Book(300)
# b4 = Book(50)
# bx = b1+b2+b3+b4
# print(bx)

# print(b1)
# print(b1+b2)
# print(b1+b2+b3)
# print(b1+b2+b3+b4)

# Example 4
# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#     def __mul__(self, other):
#         return self.salary*other.days
# class Timsheet:
#     def __init__(self,name,days):
#         self.name = name
#         self.days = days
#     def __mul__(self, other):
#         return self.days * other.salary

# e = Employee("shubham",800)
# t = Timsheet("shubham",25)
# e1 = Employee("sss",400)
# print("this month salary:",e*t)
# print("this month salary:",t*e)


# Example 5
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return "({0},{1})".format(self.x, self.y)

#     def __lt__(self, other):
#         self_mag = (self.x ** 2) + (self.y ** 2)
#         other_mag = (other.x ** 2) + (other.y ** 2)
#         return self_mag < other_mag

# p1 = Point(1,1)
# p2 = Point(-2,-3)
# p3 = Point(1,-1)

# print(p1<p2)
# print(p2<p3)
# print(p1<p3)

## Method overloading
# class Test:
#     def m1(self):
#         print("no arg method")
#     def m1(self,a):
#         print("one arg method")
# t = Test()
# t.m1()
# t.m1(10)

# default argument
# class Sum:
#     def sum(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#             print("The sum of 3 numbers:",a+b+c)
#         elif a!=None and b!=None:
#             print("the sum of 2 numbers:",a+b)
#         elif a!=None:
#             print("th sum:",a)
#         else:
#             print("plz provide atleast one argument")
# s = Sum()
# s.sum()
# s.sum(10)
# s.sum(10,20)
# s.sum(10,20,30)

# variable length argument
# class Sum:
#     def sum(self,*a):
#         total = 0
#         for x in a:
#             total += x
#         print("the sum: ",total)
#
# s = Sum()
# s.sum()
# s.sum(10)
# s.sum(10,20)
# s.sum(10,20,30)
#







