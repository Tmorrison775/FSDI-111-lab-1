print("-" * 20)
print("         Welcome!")
print("-" * 20)
name = input("Please type your name: ")
age = input("Type your age: ")
ageInt = int(age)
print("Hi " + name)
print("You will turn " + str(ageInt + 1))

#string methods
name_length = len(name) #return length
print("There are " + str(name_length) + " letters in your name")
print(name.upper())        # to upper
print(name.lower()) #to lower
print(name.replace("s", "z")) #replace letters or words inside variable

print('X' in name)