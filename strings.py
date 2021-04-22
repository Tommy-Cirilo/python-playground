# Strings in python are surrounded by either single or double quotation marks. Here are some string formatting and some string methods

name = 'Tommy'
age = 37

# Concatenate
print('Hello my name is ' + name + ' and I am ' + str(age))

# String Formatting 

# Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F=Strings (3.6+)
print(f'Hello, my name is {name} and I am {age}')

# String Methods

s = 'hello world'

# Capitalize first word of string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lowercase
print(s.lower())

# Swap Case
print(s.swapcase())

# Get lenth of string
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts with. This returns a boolean
print(s.startswith('hello'))

# Ends with. This returns a boolean
print(s.endswith('d'))

#Split string into a list (Like an array)
print(s.split())

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())