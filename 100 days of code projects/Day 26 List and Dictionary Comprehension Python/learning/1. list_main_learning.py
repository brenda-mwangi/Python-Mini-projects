# # List comprehension
# # new_list = [new_item for item in list]

# numbers = [1,2,3,4,5]
# new_numbers = [n+1 for n in numbers]


# name = "Brenda"  
# new = [i for i in name]

# range_numbers = [i*2 for i in range(1,5)]
# print(range_numbers)

# # Conditional List comprehension
# # new_list = [new_item for item in list if test]


names = ["Alex","Beth","Caroline", "Dave", "Eleanor", "Freddie"]

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)