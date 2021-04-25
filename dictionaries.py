# A Dictionary is a collection which is unordered, changeable and indexed. No Duplicate members

# Create a dictionary
person = {
    'first_name': 'Tommy',
    'last_name': 'Dommy',
    'age': '28'
}

print(person, type(person))

# Use constructor
person2 = dict(first_name='Sarah', last_name='Connor')


# Get Value
# print(person2, type(person2))
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'

# Get dict keys
print(person.keys())

# Get dict Items
print(person.items())

# Copy dict
person2 = person.copy()
person2['city'] = 'Boston'

print(person2)


# Remove item
del(person['age'])

#alternate way of deleting stuff
person.pop('phone')

# Clear
person.clear()

# Get Length
print(len(person2))

# List of dict
people = [
    {'name': 'Martha', 'age': 29},
    {'name': 'Bob', 'age': 30}
]
print(people[1]['name'])