# # 1. Reading from a file

# with open("../../../../Desktop/my_file.txt") as file:
#     content = file.read()
#     print(content)

# # 2. Writing to a file
# # a) write afresh
# with open("my_file.txt", mode = "w") as file:
#     file.write("I am from Kiambu")
# # b) append
# with open("my_file.txt", mode = "a") as file:
#     file.write("\nI am from Kiambu")

# # 3. Writing to a file that doesnt exist creates a new file in the same directory
# with open("my.txt", mode = "w") as file:
#     file.write("I am from Kiambu")