"""Counting letters in a string."""

__author__ = "730313501"


# Begin your solution here...

letter: str = input("What letter do you want to search for? ")
word: str = input("Enter a word: ")

i: int = 0
num_times: int = 0

while i < len(word):
    if (letter == word[i]):
        num_times = num_times + 1
    i = i + 1

print("Count: " + str(num_times))