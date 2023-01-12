#FileNotFound
try:
    file = open("data.txt")
    dict = {'key':'value'}
    # print(dict['khjk'])
except FileNotFoundError:
    file=open("data.txt", "w") 

except KeyError as error_message:
    print(f"Key {error_message} does not exist")

# else:
#     print(file.read())

finally:
    # file.close()
    # print("file closed")
    raise TypeError("Error I made up")
# KeyError
# IndexError
# TypeError


#raise our exceptions