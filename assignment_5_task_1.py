'''Task 1: Create a Dictionary of Student Marks
Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the students name is not found, display an appropriate message.'''

students = {"alice":92, "rahul":85, "raju":50}

name = input("enter the student's name: ")

if name in students:
    print(f"{name} marks: {students[name]}")
else:
    print("student not found")


