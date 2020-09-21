"""Problem 1 Assigning angle's value to the valuable degrees then converting that value to radian and then assigning the value to the variable radian"""

#A function that assigns an angle as a value for degrees then converting it to a radian value
def degToRad(angle, pi = 3.14):
    global degrees, radians
    degrees = angle
    radians = degrees * pi / 180

degToRad(150) #calls the function to assign those variables

print(degrees, radians) 