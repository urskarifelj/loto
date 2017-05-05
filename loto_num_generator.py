# -*- coding: utf-8 -*-
# --author-- = Urska Rifelj

import random

desired_number_of_integers = int(raw_input("How many random numbers would you like to generate?"))
number_of_random_integers = 0
list_of_random_numbers = []

while number_of_random_integers < desired_number_of_integers:
    random_number = random.randint(1,30)
    if random_number in list_of_random_numbers:
        pass
    else:
        list_of_random_numbers.append(random_number)
        number_of_random_integers += 1

print list_of_random_numbers

