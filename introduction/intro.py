print("Tell them am here")

x = 1 #variable x is assigned the value 1
print(x)

if x > 1:
    print("x is greater than 1.")
else:
    x = 1
    print("x is equal to 1.")

############################### Data types
# Strings - text
# integers - whole numbers
# floats - decimal numbers
# booleans - True or False
# lists - ordered collection of items "[1, 2, 3]"
# tuples - ordered collection of items that cannot be changed "(1, 2, 3)"
# dictionaries - unordered collection of items in key:value pairs "{key: value}"
# sets - unordered collection of unique items "{1, 2, 3}": subset, superset, union, intersection, difference.

# Strings
def print_name():
    name = "John"
    print("Your name is", name)

print_name() # function call


def sum():
    a = 5
    b = 3
    print(a + b)

sum() # function call

# Integers
age = 25

if age >= 18:
    print(age, ",You are an adult.")
else:
    print(age, "You are a minor.")

# Floats
height = 5.9
print("Your height is", height)
