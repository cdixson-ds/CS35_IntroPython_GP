"""Hello World"""

print("Hello World!")

"""Bignum: Print some big numbers, this is confusing because Python
automatically converts large integers to bignum when needed?"""

very_big = 1000**1000
#print(very_big)

"""Datatypes: Experiment with type conversion aka type casting"""

kinda_small = 10*121   #create int
print(type(kinda_small))  

kinda_small = str(kinda_small)  #cast as string
print(type(kinda_small))  

kinda_small = float(kinda_small)  #cast as float
print(type(kinda_small))

"""So when you coerce a value using pandas, is that implicit or explicit type casting?"""

import pandas as pd

stringy = "12345"

stringy = pd.to_numeric(stringy, errors='coerce')
print(stringy, type(stringy))

"""Modules:  learn to import from modules"""
"""uncomment play_game() to play rock paper scissors"""

import rps

rps.show_welcome_message()
#rps.play_game()

"""Printing: formatted print output"""

print(f'fsting containing stringy: {stringy} and kinda_small: {kinda_small}')

print('add together numeric types', stringy + kinda_small)

"""cast as strings"""
stringy = str(stringy)
kinda_small = str(kinda_small)

print('concatenate stringy and kinda_small: ', stringy + kinda_small)

print(f'fstring smash stringy and kinda_small: {stringy}{kinda_small}')

real_concat = stringy + kinda_small
print(f'concatenated into new variable {real_concat}')


decimally = float(real_concat) / 9
print(f'This is my friend decimally: {decimally}')

print(f'round decimally down to three spaces: {decimally:.3f}')

"""Lists: Python's version of arrays. A list is a collection which is ordered 
and changeable, allows duplicate members, mixed data types. written in square brackets"""

jam = ["strawberry jam", "blueberry jam", "marionberry jam", "grape jelly", "strawberry jam"]
jam_jam = ["marionberry jam", 3, "grape jelly"]

print("print jam list: ", jam)
print("print jam_jam list: ", jam_jam)

print("this should print strawberry jam: ", jam[0])

"""Tuples: Immutable lists typically for heterogenous data, 
ordered and unchangeable, round brackets"""

jam_tuple = ("strawberry jam", "blueberry jam", "grape jelly", "marmalade", "mint jelly", 
            "apple butter", "cranberry jelly")
print("this should print grape jelly: ", jam_tuple[2])

"""Slices: accessing parts of lists"""
"""slice(start, end, step)"""

slicer = slice(1, 5)
print("Printing sliced jam: ", jam_tuple[slicer])

"""Comprehensions: list comprehensions"""

# jammy = []

# for elem in range(len(jam)):
#     print(elem, jam[elem])

#jammy = [for elem in range(len(jam)): print(elem, jam[elem])]

jammy = [(elem, jam[elem]) for elem in range(len(jam))]
print("list elements within jam list: ", jammy)

jammy_tuple = [(elem, jam_tuple[elem]) for elem in range(len(jam_tuple))]
print("list elements within jammy_tuple: ", jammy_tuple)

"""print factorials"""

def generator():
    total = 1
    current = 1
    while True:
        total *= current
        yield total
        current += 1

factorial = generator()
factorial_comp = [next(factorial) for i in range(10)]
print("factorials 1-10: ", factorial_comp)

