# Integer
print("******** Integer *********")
print("{}".format(10))				# Do not write space between {}
print("{} {}".format(10, 20))
print("{0}".format(10))
print("{0} {1}".format(10, 20))
print("{1} {0}".format(10, 20))
print("{num1}".format(num1=10))
print("{num1} {num2}".format(num1=10, num2=20))
print("{num2} {num1}".format(num1=10, num2=20))

#Float
print("******** Float *********")
print("{}".format(10.56))
print("{} {}".format(10.56, 20.42))
print("{0}".format(10.56))
print("{0} {1}".format(10.56, 20.42))
print("{1} {0}".format(10.56, 20.42))
print("{num1}".format(num1=10.56))
print("{num1} {num2}".format(num1=10.56, num2=20.42))
print("{num2} {num1}".format(num1=10.56, num2=20.42))

#String
print("******** String *********")
print("{}".format("GeekyShows"))
print("{} {}".format("Geeky", "Shows"))
print("{0}".format("Geeky"))
print("{0} {1}".format("Geeky", "Shows"))
print("{1} {0}".format("Geeky", "Shows"))
print("{str1}".format(str1="GeekyShows"))
print("{str1} {str2}".format(str1="Geeky", str2="Shows"))
print("{str2} {str1}".format(str1="Geeky", str2="Shows"))

# Integer and String
print("Hello My Name is {}".format("GeekyShows"))
print("{} {}".format(10, "Shows"))
print("{0} {1}".format(10, "Shows"))
print("{1} {0}".format(10, "Shows"))
print("{num1} {str1}".format(num1=10, str1="Shows"))
print("{str1} {num1}".format(num1=10, str1="Shows"))


