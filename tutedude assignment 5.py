#Task 1: Create a Dictionary of Student Marks
dictionary={'Alice':85,'Bob':75,'Dany':65}
name=input("Enter student name")
if name in dictionary:
    print(name,"'s marks are:",dictionary[name])
else:
    print("student not found.")

#Task 2: Demonstrate List Slicing 
# Step 1: Create a list of numbers from 1 to 10
numbers = list(range(1, 11))
print("Original list:", numbers)
# Step 2: Extract the first five elements
first_five = numbers[:5]
print("Extracted first five elements:", first_five)
# Step 3: Reverse the extracted elements
reversed_five = first_five[::-1]
print("Reversed extracted elements:", reversed_five)
