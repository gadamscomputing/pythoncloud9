#ZigZag 1.1

#Python follows BODMAS
help('keywords')

#Variables must have meaningful names

# MULTIPLE ASSIGNMENTS
print("MULTIPLE ASSIGNMENTS")
age, height = 23, 6
print(age, height)

age, height = height , age
print(age, height)

#Data Types:
print("Data types")
value = 35
type(value)
print(type(value))

#Integer operations:
print("Integer Operations")
x=2
y=3

#Addition
z = x + y
print(z)


#Power - x raised to the power of y
z = pow(x,y)

print(z)

z = 0

z = x**y
print(z)

#String
print("Using strings")

month = "September"

print(month)

print("Loop for every letter in the month variable")

i=0
for letter in month:
    print(month[i])
    i=i+1
    
#Subsequence of a string
print("Subsequence of a string")
print(month[3:6])

print(month[:6])

print(month[6:])


#Finding a string within a string
print("Finding a string within a string")

hoyle='It is the true making of mankind to learn from his mistakes'

#This will return the starting position of the find text
print(hoyle.find('is the'))

#It will return -1 if the text cannot be found.
print(hoyle.find('for every action'))
    
#Finding the length of a string
print(len(hoyle))
print(len(month))

#Upper case
print(month.upper())

#Lower case
print(month.lower())

#Concatenate string. - This will nt work for a string and an integer
print("Concatination")
greeting = 'hello'
name = 'Gazza '
age = 15
print(greeting + name)
#print(greeting + name + age)

#String and multipliication
print(name * 3)

#Testing for membership using the IN operator
print("Testing for membership using the IN operator")
print('p' in month)
print('v' in month)
