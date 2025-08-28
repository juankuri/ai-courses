#1
# Your code goes here. Define a function called 'sign'
def sign(number):
    if number == 0:
        return 0
    elif number > 0:
        return 1
    else: 
        return -1
    
# Check your answer
q1.check()

#2
def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    if total_candies == 1:
        print("Splitting", total_candies, "candy")
    else:
        print("Splitting", total_candies, "candies")
    return total_candies % 3

to_smash(91)
to_smash(1)

#3
def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    # Don't change this code. Our goal is just to find the bug, not fix it!
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

# Change the values of these inputs so they represent a case where prepared_for_weather
# returns the wrong answer.
have_umbrella = False
rain_level = 5
have_hood = True
is_workday = False

# Check what the function returns given the current values of the variables above
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)

# Check your answer
q3.check()

# Check your answer
q4.check()

#4
def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return ketchup and mustard and onion

# Check your answer
q5.a.check()

#5
def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return not ketchup and not mustard and not onion

# Check your answer
q5.b.check()

#6
def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    if ketchup and mustard or (not ketchup and not mustard) :
        return False
    else:
        return True

# Check your answer
q5.c.check()

#7
def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    r = int(ketchup) + int (mustard) + int(onion)
    return r == 1

# Check your answer
q6.check()

38
def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    
    order = arrivals.index(name)
    return order >= len(arrivals) / 2 and order != len(arrivals) - 1
    

# Check your answer
q5.check()