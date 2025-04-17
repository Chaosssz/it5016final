#Labtask6 - Combine all arguments
#13/3/25 11:24am
#@auth ZJ

# create a number list from 1-10
numbers = [1,2,3,4,5,6,7,8,9,10]

#create a dictionary that stores student information
students = {
    "Name": "Zezu",
    "Age": 22,
    "Grade": 1, #adjust grade as needed
}
#INDEX is for the list iteration
#use a while loop to iterate through list of numbers
index = 0
while index < len(numbers):
    print(numbers[index])
    index += 1
#Use a for loop to print a message for each key : value pair in the dictionary.
print("\nStudent Information:")
for key, value in students.items():
    print(f"{key}: {value}")
#step 5 check if students grade is >= 80
print("\nGrade Check:")
if students["Grade"] > 80:
    print("Pass")
else:
    print("Fail")