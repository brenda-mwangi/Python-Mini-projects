with open("file1.txt") as f1:
    file1 = [int(i.strip()) for i in f1.readlines()]

with open("file2.txt") as f2:
    file2 = [int(i.strip()) for i in f2.readlines()]


result = [n for n in file1 if n in file2]

# Write your code above 👆

print(result)


