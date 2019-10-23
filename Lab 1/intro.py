print("Hello World")

# variable types on Pthon
print("-------------------------------------")
name = 'Travis'
age = 99
found = False
average = 42.21

print(name)
print(age)
print(found)
print(average)

print(type(name))
print(type(age))

# String and Math operations
print("-------------------------------------")
print(21 + 21)
print(age + 1)
print(8 - 4)
print(8 * 8)
print(42 / 21)
print(10 % 3) # % = modulus (return the residue of the division)

print(name + name)
print(name * 5)

print(name + str(age)) # in order to add string to a integer, i must parse one first

# conditions ( if )
print("-------------------------------------")
if(age < 90):
    print("You are still young")
    if(age < 12):
        print("You are a child")
else:
    print("Sorry bud, you are kind of old")

