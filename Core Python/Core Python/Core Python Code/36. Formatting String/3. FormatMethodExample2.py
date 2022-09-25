# Integer
print("******** Integer ********")
print("{}".format(15))							# Printing as string 15
print("{:d}".format(15))
print("{0:d}".format(15))
print("{num:d}".format(num=15))
print("{num:5d}".format(num=15))
print("{num:05d}".format(num=15))
print("{num:+5d}".format(num=15))
print("{num:<5d}".format(num=15))				# Left align
print("{num:*<5d}".format(num=15))				# Left align with fill
print("{num:*>5d}".format(num=15))				# Right align with fill
print("{num:^5d}".format(num=15))				# Center align
print("{num:*^5d}".format(num=15))				# Center align with fill

# Float
print("******** Float ********")
print("{}".format(15.65))						# Printing as string 15.65
print("{:f}".format(15.65))					
print("{0:f}".format(15.65))
print("{num:f}".format(num=15.65))
print("{num:8f}".format(num=15.65))				# 15.650000	
print("{num:8.3f}".format(num=15.65))
print("{num:+8.2f}".format(num=15.65))
print("{num:<8.2f}".format(num=15.65))			# Left align
print("{num:*<8.2f}".format(num=15.65))			# Left align with fill
print("{num:*>8.2f}".format(num=15.65))			# Right align with fill
print("{num:^8.2f}".format(num=15.65))			# Center align
print("{num:*^8.2f}".format(num=15.65))			# Center align with fill

#String
print("******** String ********")
print("{:8s}".format("Geek"))
print("{:<8}".format("Geek"))
print("{:*<8}".format("Geek"))
print("{:>8}".format("Geek"))
print("{:*>8s}".format("Geek"))
print("{:^8s}".format("Geek"))
print("{:*^8s}".format("Geek"))

print("******** Truncating String ********")
print("{:.3s}".format("GeekShows"))
print("{:8.3s}".format("GeekShows"))
print("{:*<8.3s}".format("GeekShows"))
print("{:>8.3s}".format("GeekShows"))
print("{:*>8.3s}".format("GeekShows"))
print("{:^8.3s}".format("GeekShows"))
print("{:*^8.3s}".format("GeekShows"))
