# No Starch Python - Functions

# Own Function
def own_function():
    """ Display a simple greeting. """
    print("Ello World?")

own_function()

# Passing Information to a Function
def information_func(username):
    print("Hello Mr./Mrs. " + username.title() + "!")

information_func("David")


# TRY IT YOURSELF

# 8-1 Message
def display_message():
    print("I'm learning about functions and how they are display ...")

display_message()

# 8-2 Favorite_Book
def favorite_book(title):
    print("My favorite book is: " + title.title() + "!")

favorite_book("Mona Lisa??")


# POSITIONAL ARGUMENTS 
# Definition
""" Positional arguments need to be written in the same order as they are call at the end of the function. """

def describe_pet(animal_type, pet_name):
    """ Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet("cat", "findus")
describe_pet("doggy", "pinis")


# KEY LEARNING STEP:
# REMEBER ---  THIS IS USED FOR NOT REWRITING UNNESCESSARY CODE ---


# KEYWORD ARGUMENTS
# Definition
""" A keyword argument is a name-value pair that you pass to a function. You directly associate the name and the value within the argument, so when you pass the argument to the function, there’s no confusion (you won’t end up with a harry named Hamster)."""

def describe_pet_02(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet_02(animal_type="hamster", pet_name="harry")


""" NOTE: When you use keyword arguments, be sure to use the exact names of the parameters in the function’s definition."""


