#ZigZag 1.1

#Python follows BODMAS
help('keywords')

#Variables must have meaningful names
print("_________________________________")
# MULTIPLE ASSIGNMENTS
print("MULTIPLE ASSIGNMENTS")
print("_________________________________")
age, height = 23, 6
print(age, height)

age, height = height , age
print(age, height)

print("_________________________________")
#Data Types:
print("Data types")
print("_________________________________")
value = 35
type(value)
print(type(value))
print("_________________________________")

#Integer operations:
print("Integer Operations")
print("_________________________________")
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
print("_________________________________")

#String
print("Using strings")
print("_________________________________")
month = "September"

print(month)
print("_________________________________")
print("Loop for every letter in the month variable")
print("_________________________________")
i=0
for letter in month:
    print(month[i])
    i=i+1
print("_________________________________")

#Subsequence of a string
print("Subsequence of a string")
print("_________________________________")
print(month[3:6])

print(month[:6])

print(month[6:])
print("_________________________________")

#Finding a string within a string
print("Finding a string within a string")
print("_________________________________")
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
print("_________________________________")

#Concatenate string. - This will nt work for a string and an integer
print("Concatination")
greeting = 'hello'
name = 'Gazza '
age = 15
print(greeting + name)
#print(greeting + name + age)

#String and multipliication
print(name * 3)
print("_________________________________")

#Testing for membership using the IN operator
print("Testing for membership using the IN operator")
print("_________________________________")
print('p' in month)
print('v' in month)
print("_________________________________")

#Functions
print("FUNCTIONS")
print("_________________________________")

def sum(a, b):
    return (a+b)
    
print(sum(12,10))

def hello_twice(name):
    print("Hello " + name)
    print("Hello " + name)

nameInput = input("Enter a name here!!")

print(hello_twice(nameInput))
print("_________________________________")


#Functions
print("Parameters and arguments")
print("_________________________________")

#Program flow
#The order that the functions are called in. Example the inner function is called first then the outer function.
def larger(a,b):
    if a > b:
        return(a)
    else:
        return(b)

x=12
y=7
z=79
print(larger(larger(x,y),z))

print("_________________________________")


#Control structures
print("Control structures")
print("_________________________________")

#If Statement
if 5>2:
    print("5 is larger")


#IF ELSE Statement
month = "September"
if len(month)>10:
    print(month + ' has more than ten characters')
else:
    print(month + ' has less than ten characters')
    
#Loops
