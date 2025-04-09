"""

Rajan does not know what to put in his lunch, and Anjali will starve without it. Create a program that will decide
what Rajan should put in his lunch. 
There should be two sweet snacks, one salty snack, two fruits/vegetables, and a main.

rule: no random.choice(list)

lunch.py
Jeremy Liu
4/9/2025

"""

import random

def main():

    # lists for the different foods

    sweet = ["sour straps", "granola bars", "cookies", "fruit gummies"]
    salty = ["doritos", "pretzels", "peanuts", "samosas"]
    fruits_n_veggies = ["apples", "oranges", "mangoes", "cuckumbers", "bell peppers"]
    main_course = ["chicken parmesan", "turkey sandwich", "pasta", "roast beef and mashed potatoes"]

    # prints the different random choices by passing the lists into the random_picker function

    print(f"Your sweet snacks are: {random_picker(sweet, 2)}")
    print(f"Your salty snacks are: {random_picker(salty, 1)}")
    print(f"Your fruits and veggies are: {random_picker(fruits_n_veggies, 2)}")
    print(f"Your main course is: {random_picker(main_course, 1)}")

def random_picker(list, numbers):

    new_list = [] # creates a new_list for appending picked goods into the list

    # generate a random integer between 0 and the length of the list

    for _ in range(numbers):
        random_number = random.randint(0, len(list)-1)
        new_list.append(list[random_number]) # appends the chosen element with the index of the chosen random_number
        list.pop(random_number) # pops the original list so the element cannot be randomly chosen again (no repeats)
    
    return (" and ".join(new_list)) # returns the newly, randomly chosen elements as a str

main()
