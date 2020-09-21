"""Problem 2 finding the average score tests of 3 students"""

#Assigning the value for the student scores
student1 = 80
student2 = 90
student3 = 66.5

#Function for finding the average out of those student scores
def findAverage(student1, student2, student3):
    scoreAverage = (student1 + student2 + student3) / 3
    return scoreAverage

#Assigning the value to the average variable
average = findAverage(student1, student2, student3)

print(average)