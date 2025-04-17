#conditional logic with IF statement
#@auth ZJv
#10/3/25 5:28pm

#Create a list of student grades
student_grades = [85, 90, 55, 78, 92, 68, 74]
#use the for loop learnt in task 4 to iterate through the LIST
#using if statement check if grade is greater than or equal too 80
for grade in student_grades:
    if grade >= 80:
        print("You pass!")
    else: #if anything < 80 then print fail and end
        print("Score too low, FAILED!")
