# Reminder about dictionaries:
# Dictionaries do not need to be sorted {key:value, key:value, key:value}
# Dictionaries can be read from like lists

my_list = ['hello', 'owo', 'patreon']
#a_dictionary = {key:value, key:value, key:value}

# Tuples
ssn = (38943089, 'Gerard')
print(ssn)

# Dictionay methods

# clear()      Removes all the elements from the dictionary
# copy()      Returns a copy of the dictionary
# fromkeys()  Returns a dictionary with the specified keys and value
# items()      Returns a list containing a tuple for each key value pair
# keys()      Returns a list containing the dictionary's keys
# pop()          Removes the element with the specified key
# values()      Returns a list of all the values in the dictionary

# .clear() mehtod:
people_dictionary = {'Cory Monteith':'actress', 'Heath Ledger':'actor', 'Brandon Lee':'actor', 'Kim Jong-un':'politician'}
people_dictionary.clear()
print(people_dictionary)

# .copy()
my_dict = {1: 'apple', 2: 'left ball'}
my_dict_1 = my_dict.copy()
print(my_dict_1)

# .fromkeys
x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)
print(thisdict)

# .items()
for key, value in people_dictionary.items():
    if key == 'Cory Monteith' and value == 'actress':
        print('SHE IS!', '\n')

# .keys()
if 'Kim Jong-un' in people_dictionary.keys():
    print('He dead!', '\n')

# .pop()
undead = people_dictionary.pop("Heath Ledger")
print(people_dictionary)
print(undead)

# .values()
print(people_dictionary.values())

# [] square bracket
profession = people_dictionary['Brandon Lee']
print(profession)



urban_dictionary_dictionary = {'decoronafied':'Someone or something that has been thoroughly disinfected.',
                               'dead cat bounce':'Investor slang; a brief recovery in the price of a falling stock. Term is derived from the idea that "even a dead cat will bounce if it falls from a great height."',
                               'planeclapper':'An individual so exuberated from social hierarchy that they willingly and excitedly offer applause upon the landing of an airplane flight.',
                               'snickerpuss':'someone who laughs a lot at silly things',
                               'miso':'The acronym standing for "my internet shut off!". Used in an intense instant-messaging conversation that ended abruptly.',
                               'internet':'pornography\'s best friend',
                               'sexual predator':'James Charles',
                               'dead cat':'An ex-spouse/partner/lover. From the reference to how many people, in a given place, a person has had relationships with that can be hit by swinging a dead cat.',
                               'free lunch':'Used to refer to a *-free or catch free offer, the expression "there is no free lunch" sums it up.',
                               'wolfbag':'during anal intercourse your female partner gags herself purposely to constrict her rectum and cause pre-mature ejaculation (thank you miss).',
                               }


word_to_find = 'free lqirubflunch' # The key

# Check if key is in the dictionary
# We can use .keys()
if word_to_find in urban_dictionary_dictionary.keys():
    definition = urban_dictionary_dictionary[word_to_find]
    print('The defition of ', word_to_find, ' is: ', definition)
else:
    print("Fuck off I ain't got it")

# The defition of [word] is: [definition]
