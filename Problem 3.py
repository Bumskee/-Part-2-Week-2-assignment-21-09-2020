"""Problem 3 Finding the number of children in 1 group without the leftover and also finding the leftover"""

#Assigning the values using simultaneous assignment
class1Students, class2Students, class3Students = 32, 45, 51

#Function for finding the same amount of persons in a group and the leftover (also using simultaneous assignment) then print the variables
def personPerGroupAndLeftover(class1Students, class2Students, class3Students):
    class1, class2, class3 = class1Students // 5, class2Students // 7, class3Students // 6
    print("class 1 =", str(class1))
    print("class 1 =", str(class2))
    print("class 1 =", str(class3))
    class1, class2, class3 = class1Students % 5, class2Students % 7, class3Students % 6
    print("class 1 =", str(class1))
    print("class 1 =", str(class2))
    print("class 1 =", str(class3))

#calls the function
personPerGroupAndLeftover(class1Students, class2Students, class3Students)
