# Sequence Types
import ipdb;
# Note: use print() to execute the examples. Comment out examples as needed to keep your Terminal
# output clean.

#! DOGMAS TO LIVE BY
# When dealing with a new method:
# 1. What does the method do
# 2. How many arguments does it expect
# 3. What does it return
# 4. Destructive vs Non-destructive

#! Lists
# TODO Creating Lists
# 1. ✅ Create a list of 10 pet names
pet_names = ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul']

# TODO Reading Information From Lists

# 2a. ✅ Return the total count of elements
len(pet_names)
# 2b. ✅ Return the first pet name
pet_names[0]  #! IndexError if index is not in list
# 3. ✅ Return all pet names beginning from the 3rd index (included)
pet_names[3:]
# 4. ✅ Return all pet names before the 3rd index (not included)
pet_names[:3]
# 5. ✅ Return all pet names beginning from the 3rd index and up to / including the 7th index
pet_names[3:8]
# 6. ✅ Find the index of a given element
pet_names.index("Rose") #! ValueError if element not in list
# 7. ✅ Read the original list in reverse order
pet_names[::-1] #! preferred to reverse as the latter is destructive!!!
# 8. ✅ Return the frequency of a given element
pet_names.count("Rose") #! no errors will be raised for elements outside of the collection

# TODO Updating Lists
# 9. ✅ Change the first pet_name to all uppercase letters
pet_names[0] = pet_names[0].upper()
# 10. ✅ Append a new name to the list
pet_names.append("Romeo")
# 11. ✅ Add a new name at a specific index
pet_names.insert(4, "Milo")
# 12. ✅ Add two lists together
pet_names.extend(["Matteo", "Claudia"]) #! DESTRUCTIVE
pet_names + ["Matteo", "Claudia"] #! NON-DESTRUCTIVE
[*pet_names, "Matteo"] #! NON_DESTRUCTIVE SPREAD OPERATOR
# 13. ✅ Remove the final element from the list
pet_names.pop()
# 14. ✅ Remove element by specific index
pet_names.pop(3)  #! IndexError if index not in list, DESTRUCTIVE and returns the removed el
# 15. ✅ Remove a specific element
# pet_names.remove("Luke")  #! DESTRUCTIVE
# 16. ✅ Remove all pet names from the list
pet_names.clear()  #! DESTRUCTIVE

#!Tuple
# 📚 Review:
# Mutable, Immutable <=> Changeable, Unchangeable

# Why Are Tuples Immutable?

# What advantages does this provide for us? In what situations
# would this serve us?
# TODO Accessing Elements
# 17. ✅ Create an empty Tuple, one with one element and one with 10 pet ages
empty_tuple = ()
single_tuple = (True,)
ages_generator = tuple(range(10))

# 18. ✅ Print the first pet age
ages_generator[0]

# TODO Testing Mutability (you can add a tuple to a tuple though)
# 19. ✅ Attempt to remove an element with ".pop" #! AttributeError: 'tuple' object has no attribute 'pop'
# 20. ✅ Attempt to change the first element #! TypeError: 'tuple' object does not support item assignment

# TODO Tuple Methods
# 21. ✅ Return the frequency of a given element
ages_generator.count(8)
# 22. ✅ Return the index of a given element
ages_generator.index(8)
# 22b. ✅ Concatenate a tuple into another tuple => returns a new tuple in the end, no modifications
ages_generator + (999, 1000)

#! Range
# 23. ✅ create a Range
# Note:  Ranges are primarily used in loops
range_ = range(1, 100, 2)
range_.start #=> 1
range_.stop #=> 100 (NOT INCLUDED)
range_.step #=> 2 by 2

#! Sets (value cannot be modified but you can add/remove elements)
# TODO Think about uniqueness in sets
# 24. ✅ Create a set of 3 pet foods
pet_fav_food = {'house plants', 'fish', 'bacon'}
pet_fav_food2 = {'fish', 'eggs'}
#! empty sets cannot just use {} because those will be interpreted as dict {} -> set()

# TODO Reading
# 25. ✅ Print set elements with a loop
for el in pet_fav_food:
    if el == "fish":
        print(el)
# 26. ✅ Check if an element is in a set
'fish' in pet_fav_food
# 27. ✅ Get an element
#! sets are unordered collections, so there is no concept or first/second and you cannot access a specific element but rather check its presence
# 28. ✅ Get a copy of a set
pet_fav_food.copy()
# 29. ✅ isdisjoint, issubset, issuperset

# TODO Updating
# 30. ✅ Add an element to a set
pet_fav_food.add("tuna")
# 31. ✅ Union, intersection, difference
pet_fav_food.union(pet_fav_food2)
pet_fav_food.intersection(pet_fav_food2)
pet_fav_food.difference(pet_fav_food2)
# 32. ✅ Update current set with elements from other set
pet_fav_food.update(pet_fav_food2)

# TODO Deleting
# 33. ✅ Delete specific el using ".remove"  VS ".discard"
pet_fav_food.remove("tuna") #! KeyError for non existing removals
pet_fav_food.discard("tuna") #! NO Error for non existing removals
# 34. ✅ Delete random element using ".pop"
pet_fav_food2.pop()

#! Dictionaries (from 3.7+, dictionaries are ordered)
# TODO Creating
# 35. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_rose = {'name':'Rose', 'age':11, 'breed':'domestic long'}
# 36. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed" => dict(...)
pet_info_spot = dict(name='Spot', age=25, breed='boxer')

# TODO Reading
# 37. ✅ Print the pet attribute of "name" using bracket notation
pet_info_rose["name"] #! Raises KeyError in case the key doesn't exist
# 38. ✅ Print the pet attribute of "age" using ".get"
pet_info_rose.get(
    "name", "default value"
)  #! RaisDoes not raise a KeyError and allows to provide a default value

# Note: ".get" is preferred over bracket notation in most cases
# because it will return "None" instead of an error
# 39b. ✅ Get dict keys
pet_info_rose.keys()
# 39c. ✅ Get dict values
pet_info_rose.values()
# 39d. ✅ Get dict pairs
pet_info_rose.items()

# TODO Updating
# 40. ✅ Update Rose's age to 12
pet_info_rose["age"] = pet_info_rose["age"] + 1
# 41. ✅ Update Spot's age to 26

# TODO Deleting
# 42. ✅ Delete Rose's age using the "del" keyword => []
del pet_info_rose["breed"] #! Destructive, returns nothing
# 43. ✅ Delete Spot's age using ".pop"
pet_info_rose.pop("age")  #! Destructive, returns the popped value
# 44. ✅ Delete the last item for Rose using "popitem()"
pet_info_rose.popitem()
# 45 ✅ Delete every key/value pair => clear()
pet_info_rose.clear() #! clear the data in the current memory location
pet_info_rose = {} #! point to a diff memory location

#! Loops
pet_info = [
    {
        'name':'Rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'Spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Gracie',
        'age':2,
        'breed': 'domestic long-haired',
    }
]

# 46. ✅ Loop through a range of 10 and print every number within the range
for el in range(10):
    print(el)
# 47. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number
# 48. ✅ Loop through the "pet_info" list and print every dictionary
for val in pet_info:
    print(val)

for k, v in pet_info_rose.items():
    print(k, v)
#! Exercises for you to practice
# 49. ✅ Create a function that takes a list a parameter
# The function should use a "for" loop to loop through the list and print each item
# Invoke the function and pass it "pet_names" as an argument
# 50. ✅ Create a function that takes a list as a parameter
# The function should define a variable ("counter") and set it to 0
# Create a "while" loop
# The loop will continue as long as the counter is less than the length of the list
# Every loop should increase the count by 1
# Once the loop has finished, return the final value of "counter"
# 51. ✅ Create a function that updates the age of a given pet
# The function should take a list of "dictionaries", "name" and "age" as parameters
# Create an index variable and set it to 0
# Create a while loop
# The loop will continue so long as the list does not contain a name matching the "name" param
# and the index is less then the length of the list
# Every list will increase the index by 1
# If the dictionary containing a matching name is found, update the item's age with the new age
# Otherwise, return 'Pet not found'

#! Functional Programming corner
# map like VS map
# 52. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase
new_list = []
for pet_dict in pet_info:
    new_list.append(pet_dict.get("name").upper())

pet_caps_names = [pet_dict.get("name").upper() for pet_dict in pet_info]
pet_caps_names = list(map(lambda pet_dict: pet_dict.get("name").upper(), pet_info))

# find like VS find
# 53. ✅ Use list comprehension to find a pet named spot

# filter like VS filter
# 54. ✅ Use list comprehension to find all of the pets under 3 years old
new_list = []
for pet_dict in pet_info:
    if pet_dict.get("age") < 3:
        new_list.append(pet_dict)

filtered_coll = [pet_dict for pet_dict in pet_info if pet_dict.get("age") < 3]
filtered_coll = list(filter(lambda pet_dict: pet_dict.get("age") < 3, pet_info))

# reduce like VS reduce
# 55. ✅ Use list comprehension to find all of the pets under 3 years old

#! Writing Generators
# 56. ✅ Create a generator expression matching the filter above
#! THIS
[pet_dict.get("name").upper() for pet_dict in pet_info]
#! VS
(pet_dict.get("name").upper() for pet_dict in pet_info)

#! Compare Generators and Expressions
import sys
import timeit
starter_list = list(range(100000))

#! MEMORY
print("List Comprehension Memory Size", sys.getsizeof([el for el in starter_list if el%2==0]))
# 444376
print("Generator Expression Memory Size",sys.getsizeof((el for el in starter_list if el%2==0)))
# 208

#! RUNTIME
print("Comprehension Run 1 Time", timeit.timeit("[el for el in starter_list if el%2==0]", "from __main__ import starter_list", number=1))
# => 0.005183833185583353
print("Comprehension Run 1000 Time", timeit.timeit("[el for el in starter_list if el%2==0]", "from __main__ import starter_list", number=1000))
# => 2.4483373747207224
print("Generator Run 1 Time", timeit.timeit("(el for el in starter_list if el%2==0)", "from __main__ import starter_list", number=1))
# => 9.041279554367065e-06
print("Generator Run 1000 Time", timeit.timeit("(el for el in starter_list if el%2==0)", "from __main__ import starter_list", number=1000))
# => 0.00024854158982634544
