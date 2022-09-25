# Importing Two Modules and accessing their members
# Both Modules has same name variable and function
# geekyshows.py <--- Main Module

import first			# Importing first Module
import second			# Importing second Module

print(first.a)			# Accessing first Module's Variable
first.name()			# Accessing first Module's Function

print(second.a)			# Accessing Second Module's Variable
second.name()			# Accessing Second Module's Function

