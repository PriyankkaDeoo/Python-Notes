# Importing Two Modules and accessing their members
# Both Modules has same name variable and function
# geekyshows.py <--- Main Module

import first as f			# Importing first Module
import second as s			# Importing second Module

print(f.a)			# Accessing first Module's Variable
f.name()			# Accessing first Module's Function

print(s.a)			# Accessing Second Module's Variable
s.name()			# Accessing Second Module's Function

