# append()  Adds an element at the end of the list [X]
# clear()  Removes all the elements from the list [X]
# copy()  Returns a copy of the list [X]
# count()  Returns the number of elements with the specified value [X]
# index()  Returns the index of the first element with the specified value [X]
# insert()  Adds an element at the specified position [X]
# pop()  Removes the element at the specified position [X]
# remove()  Removes the first item with the specified value [X]
# reverse()  Reverses the order of the list [X]
# sort()  Sorts the list

# Access values within a list:
number_list = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7]
number_5 = number_list[4]
print(number_5)

# .count()
hair_colors = ['blonde', 'red', 'black', 'pink', 'blonde']
print(hair_colors.count('blonde'))

# .index()
print(hair_colors.index('blonde'))

# .inser()
hair_colors.insert(4, 'purple')
print(hair_colors)
#--!--#--#--#--#

# .pop()
pink = hair_colors.pop(3)
print(hair_colors, pink)

# .remove()
hair_colors.remove('red')
print(hair_colors)

# .reverse()
print(number_list)
number_list.reverse()
print(number_list)

# .sort()
number_list.sort()
print(number_list)

# In this example you will be a doctor! 
# You have a set of patients
# One of your patients is really ill
