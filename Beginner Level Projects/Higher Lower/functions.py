from random import random
from data import data


def selection_for_b(a):
    """Select random account for b"""
    b = data[random.randint(0, 49)]
    while a['name'] == b['name'] :
        b = data[random.randint(0, 49)]
    return b


def print_score(score, count):
    """Print the score line."""
    if count> 0:
        print(f"You're right !!,You're Score :{score}")