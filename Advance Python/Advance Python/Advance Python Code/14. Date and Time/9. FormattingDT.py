# Formatting Date and Time
from datetime import datetime
dt = datetime.today()
print(dt)
newd1 = dt.strftime("%B %d, %Y")
print(newd1)
newd2 = dt.strftime("%d/%b/%Y")
print(newd2)
newd3 = dt.strftime("%d-%m-%Y")
print(newd3)

newt1 = dt.strftime("%H:%M:%S")
print(newt1)
newt2 = dt.strftime("%I:%M:%S")
print(newt2)