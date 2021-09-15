"""Repeating a beat in a loop."""

__author__ = "730313501"


# Begin your solution here...

repeat_beat: str = input("What beat do you want to repeat? ")
repeat_num: int = int(input("How many times do you want to repeat it? "))

i: int = 0
s: str = ""

if (repeat_num <= 0):
        print("No beat...")
else:
    while i < repeat_num:
        if (i == 0):
            s = repeat_beat
        else:
            s = s + " " + repeat_beat
        i = i + 1
    print(s)