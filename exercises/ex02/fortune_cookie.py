"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730313501"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

random_integer: int = randint(1, 100)

# Begin your solution here...
print("Your fortune cookie says...")
if random_integer < 50:
    if random_integer < 25:
        print("You will succeed in your wildest endeavors")
    else:
        print("You will find the love of your life in unexpected ways")
else:
    if random_integer < 75:
        print("You will satisfy that urge that you couldn't ")
    else:
        print("You will ace your next comp exam!")
print("Now, go spread positive vibes!")