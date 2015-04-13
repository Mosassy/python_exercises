__author__ = 'mosassy'
x = raw_input(("Enter your first number here: "))
y = raw_input("Enter your second number here: ")

x = int(x)
y = int(y)

while y == 0:
    y = raw_input("Please enter an integer other than zero: ")

y = int(y)

add = x + y
subtract = x - y
product = x * y
division = x / y
remainder = x % y

print "The sum of the " + str(x) + " and " + str(y) + ": " + str(add)
print "The difference of " + str(x) + " and " + str(y) + ": " + str(subtract)
print "The product of " + str(x) + " and " + str(y) + ": " + str(product)
print "The quotient of " + str(x) + " and " + str(y) + ": " + str(division) + " with remainder: " + str(remainder)


#b = y - x
