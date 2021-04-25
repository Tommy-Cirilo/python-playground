#A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#If you only have one Tuple, you should leave a trailing comma after the value


#Create Tuple
fruits = ('Apples', 'Oranges', 'Grapes')
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))
# Example of single value tuple with a trailing comma
# fruits2 = ('Apples',)
#Get Value
# print(fruits[1])

# Can't change value of a Tuple
# fruits2[0] = 'Pears'


#Delete Tuple
del fruits2


#Get Length
print(len(fruits))

print(fruits, type(fruits2))



#A Set is a collection which is unordered and unindexed. No duplicate members

#Create Set
fruits_set = {'Apples', 'Oranges', 'Mango'}

#Check if something is in a set
print('Apples' in fruits_set)

#Add to set (Can't Add a duplicate to a set)
fruits_set.add('Grape')

#Remove from set
fruits_set.remove('Grape')

#Clear set that wont have any more values in it
fruits_set.clear()

#Delete set
del fruits_set

print(fruits_set)