# class Add:
#     def result(self, a, b):
#         print('Addition:', a + b)
#
#
# class Multi(Add):
#     def result(self, a, b):
#         print('Multiplication:', a * b)
# #
# #
# m = Multi()
# m.result(10, 20)

# m = Add()
# m.result(10, 20)


class Add:
    def result(self, a, b):
        print('Addition:', a + b)


class Multi(Add):
    def result(self, a, b):
        super().result(a, b)  # Calling Parent Class's Method
        print('Multiplication:', a * b)


m = Multi()
m.result(10, 20)