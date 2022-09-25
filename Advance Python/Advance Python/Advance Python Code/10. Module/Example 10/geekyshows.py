# Importing Two Modules and accessing their members
# Both Modules has same name variable and function
# geekyshows.py <--- Main Module

from first import *			# Importing first Module

print(a)		# Accessing first Module's Variable
name()			# Accessing first Module's Function

from second import *			# Importing second Module

print(a)		# Accessing Second Module's Variable
name()			# Accessing Second Module's Function

