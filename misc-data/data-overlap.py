# Open files
# Example: 
file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

# Check the files and format, modify if necessary
# Exmaple:
lines1 = file1.readlines()
lines2 = file2.readlines()

# If needed, lose the \n:
stripped1 = [int(line.strip()) for line in lines1]
stripped2 = [int(line.strip()) for line in lines2]

# Find all overlapping values in the files and add them to a list:
overlap = [num for num in stripped1 if num in stripped2]
print(overlap)

# Change code as needed!


