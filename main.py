# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

def addition_(x):
    def adding(y):
        return x + y

    return adding

add_random = addition_(random.randint(0,10))

print(add_random(10))

