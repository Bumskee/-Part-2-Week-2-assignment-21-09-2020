"""Problem 4 fixing the program's code"""

#Fixing some variable naming and converting circumference into a string for the final print command
pi = 3.14
pie_diameter = 55.4
pie_radius = pie_diameter // 2
circumference = 2 * pi ** pie_radius
circumference_msg = "Jimmy’s pie has a circumference:"
print(circumference_msg, str(circumference))