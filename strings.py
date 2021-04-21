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

