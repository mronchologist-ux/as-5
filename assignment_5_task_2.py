'''Task 2: Demonstrate List Slicing 
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
'''
numbers = list(range(1, 11))

first_five = numbers[0:5]
reversed_first_five =first_five [::-1]

print("extrected first five element:", first_five)
print("Reversed exrected elements:", reversed_first_five)

