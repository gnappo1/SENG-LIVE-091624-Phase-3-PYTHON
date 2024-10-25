#!/usr/bin/env python3

# 📚 Review:
    # Python Environment Setup
	# Python Debugging Tools
	# Python Data Types 

# 🚨 To enable ipdb debugging, first import "ipdb"
# import ipdb


#TODO Initial Discussion
# 0. Style Guide (visit: https://peps.python.org/pep-0008/#code-lay-out)
# 1. Data Types
    # Sequence: str, list, tuple
    # Mapping: dict, frozendict
    # Numeric: int, float, complex
    # Set: set, frozenset
    # Bool: True, False
    # NoneType: None

# Truthiness and Falseness
    # Falsey: 0, 0.0, 0+0j, "", None, [], {}, set(), ()

# 2. Variable Naming Conventions (visit https://peps.python.org/pep-0008/#naming-conventions)
    # snakecase for variables and functions
    # Pascalcase for class names
    # All caps for values that should regarded as constant
pet_mood = "Hungry!"
pet_name = "Rose"

# 3. String Interpolation (over concatenation)
# 4. Printing to Console
# print(f"Hey! My name is {pet_name} and my mood is {pet_mood}")

def the_global_keyword():
    # In Python, if you assign a value to a variable inside a function
    # without using the global keyword, Python assumes that you're creating a
    # local variable within that function's scope.
    # If a variable with the same name exists in the global scope, it won't be modified.
    # So, you would use the global keyword when you want to modify a global variable
    # from within a function.
    global pet_name
    pet_name = "matteo"  # * without the global keyword it would create a local variable
    #! I just modified the global variable with the line above
    return pet_name

def outer_function():
    x = "outer"
    def inner_function():
        nonlocal x  # refers to the enclosing scope's x
        x = "modified in inner"

    inner_function()
    print(x)  # Outputs: modified in inner

outer_function()

# hello()
# print(x) #NameError: name 'name' is not defined

#TODO 1. ✅ Create a condition to check a pet's mood
    # If "pet_mood" is "Hungry!", "Rose needs to be fed."
    # If "pet_mood" is "Rowdy!", "Rose needs a walk."
    # In all other cases, "Rose is all good."
    
# if pet_mood == "Hungry!": 
#     print("Rose needs to be fed.")
# elif pet_mood == "Rowdy":
#     print("Rose needs a walk.")
# else:
#     print("Rose is all good.")
    # Note => Feel free to set your own values for "pet_mood" to view various outputs.

#TODO 2. ✅ Create a ternary operator using "pet_mood" as a condition:
    # If pet_mood is "Hungry!" => "Rose needs to be fed."
    # In all other cases => "Rose is all good."
# print("Rose needs to be fed.") if pet_mood == "Hungry!" else print("Rose is all good.")

#! Python 3.10+ introduced match statements
# match(pet_mood):
#     case "Hungry":
#         print("Rose needs to be fed.")
#     case "Rowdy!":
#         print("Rose needs a walk.")
#     case _:
#         print("Rose is all good.")
        
#TODO 3. ✅ Create a function (say_hello) that returns the string "Hello, world!"
    # Test invocation of "say_hello" in ipdb using "say_hello()"
    # say_hello() => "Hello, world!"
def say_hello():
    return "Hello, world!"

# print(say_hello())

#TODO 4. ✅ Create a function (pet_greeting) that will return a string with interpolated pet's name
    # Test invocation of "pet_greeting" in ipdb using "pet_greeting()"
    # pet_greeting("Rose") => "Rose says hello!"
    # pet_greeting("Spot") => "Spot says hello!"
def pet_greeting(pet_name="Default Value"):
    return f"{pet_name} says hello!"

# print(pet_greeting())

#TODO 5. ✅ Move conditional logic from Deliverable 1 into a function (pet_status) so that we may use it with different pets / moods
    # Test invocation of "pet_status" in ipdb using "pet_status(pet_name, pet_mood)"
    # pet_status("Rose", "Hungry!") => "Rose needs to be fed."
    # pet_greeting("Spot", "Rowdy!") => "Spot needs a walk."
    # pet_greeting("Bud", "Relaxed") => "Bud is all good."
    
    # Take a moment to note that "pet_name" and "pet_mood" parameters are within Local Scope and take priority over "pet_name" and "pet_mood"
    # in Global Scope.

#TODO 6. ✅ Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors. 
    # If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
    # pet_birthday(10) => "Happy Birthday! Your pet is now 11."
    # pet_birthday("oops") => "Type Error Occurred"
def pet_birthday(age):
    try:
        # ipdb.set_trace()
        print("test")
        return f"Happy Birthday! Your pet is now {age + 1}"
    except Exception as e:
        return e

pet_birthday("10")
    # Note => To view more common Python exceptions, visit https://docs.python.org/3/library/exceptions.html

# 🚨 To create an ipdb breakpoint, comment / uncomment line below:
# ipdb.set_trace()


