class Add():
    def sum1(self,a,b,c):
        s = a + b + c
        print(s)
    def sum1(self,a,b):
        s = a + b
        print(s)
    def sum1(self):
        print('no argument')

o = Add()
o.sum1()



#
# class Myclass:
#     def sum(self, a=None, b=None, c=None):
#         if a != None and b != None and c != None:
#             s = a + b + c
#         elif a != None and b != None:
#             s = a + b
#         else:
#             s = 'Provide at least Two Numbers'
#         return s
#
#
# obj = Myclass()
# print(obj.sum())



class Add():
    def sum1(self,*a):
        s = 0
        for x in a:
            s += x
        print(s)
b = Add()
b.sum1(10,20,30,40)
