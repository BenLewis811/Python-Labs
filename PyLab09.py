# -*- coding: utf-8 -*-
"""

  Program: CSC115/170 Lab 09 - The Final Battle
 ----------------------------
  Partner 1:  Esten Odney
  Partner 1s contributions:

  Partner 2: Ben Lewis
  Partner 2s contributions: 
  
  Date: 
      
      

"""

################################################
# 1. Imports
import numpy as np
import random
import pandas as pd

################################################
# 2. Constants - filenames, hero stats etc
opening_file = 'opening29.txt'
closing_file = 'closing29.txt'
spell_file = 'spells_data.csv'
hero_health = 100
power = 10
enemy_name = 'Morvath the Malevolent'
enemy_health = 500  # Significantly higher than the hero's health

################################################
# 3. read_text_file function
def read_text_file(filename):
    """
    Reads the contents of a text file and returns it as a string.

    Parameters:
        filename (str): The name or path of the text file to be read.

    Returns:
        str: The contents of the file as a string if it exists,
             otherwise an empty string if the file cannot be found.

    Example usage:
        contents = read_text_file("example.txt")
        print(contents)
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "no file, try again later"




################################################
# 4. read_csv_file function
import csv
import numpy as np

def read_csv_file(filename):
    """Reads a CSV file containing spell names and damage into NumPy arrays.

    Parameters:
        filename (str): The path to the CSV file.

    Returns:
        tuple: Two NumPy arrays - spell names (str) and damage values (int).
    """
    spell_names = []
    damage = []

    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header

            for row in reader:
                if len(row) < 2:
                    continue  # Skip malformed lines
                spell_names.append(row[0])
                try:
                    damage.append(int(row[1]))
                except ValueError:
                    print(f"Warning: Could not convert damage value '{row[1]}' to int. Skipping row.")
                    continue

        return np.array(spell_names, dtype=str), np.array(damage, dtype=int)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return np.array([]), np.array([])

    except Exception as e:
        print(f"An error occurred while reading '{filename}': {e}")
        return np.array([]), np.array([])




################################################
# 5. attack function from Lab 4 (feel free to modify as needed)
def attack(power, enemy_name, enemy_health):
    """
    This is the attack function. It will print how much you attacked for, and how much health the
    enemy has left. If the enemy has no health it will print that the enemy is defeated

    Parameters: Power, enemy_name, enemy_health.  

    returns: enemy_health if the enemy is still alive after the attack, or 0 if it is slain. 
    Both results are printed by the function. 
    Example: attack(5, 'Swamp Troll', 100) ->  returns: enemy_health = 95
    """
    attack = power * random.randint(1,6)
    print(f"You attacked {enemy_name} for {attack} damage")

    enemy_health = enemy_health - attack
    if enemy_health > 0:
        print(f"{enemy_name} has {enemy_health} hitpoints left.")
        return enemy_health
    else:
        print(f"You have slain {enemy_name}")
        return 0



#################################################
# 6. magic_attack function for the sorcerer's attacks
def magic_attack(hero_health, enemy_name, spell_name, spell_power):
    """Simulates sorcerer's spell attack on hero, returns updated hero health.
    
    Parameters:
    hero_health (int): Hero's current health
    enemy_name (str): Name of sorcerer
    spell_name (str): Name of spell used
    spell_power (int): Damage value of spell
    
    Returns:
    int: Updated hero health

    Example magic_attack( 50, Morvath, Fireball, 5) returns -> 45
    """
    print(f"{enemy_name} attacks with {spell_name}! It deals {spell_power} damage.")
    hero_health -= spell_power
    hero_health = max(hero_health, 0)
    print(f"Hero's health is now {hero_health}.")
    return hero_health


#################################################
# 7. Any other functions needed
#For syntak 
def grab_syntak(power, enemy_name, enemy_health):
    """
    This function is for when the hero hits 0 health. When it is called, it attacks Morvath with 
    10x your normal damage.

    Parameters: Power, enemy_name, enemy_health
    This takes all the inputs needed for the attack function and calls the attack function while
    multiplying the power by 10. 

    Returns: none.  This is a void function that changes a global variable of enemy health. 

    Example: grab_syntak(power, enemy_name, enemy_health) will set the variable enemy_health to a 
    value of 100-500 points lower than it's current value. 
    """
    print("\nYou crawl over to the altar, desperately reach up and grab the Syntak!")
    print("You feel a surge of ancient power coursing through you!")
    enemy_health = attack(power * 10, enemy_name, enemy_health)
    

#################################################
# 8. Narratives and program run

# display opening narrative
print(read_text_file(opening_file),"\n")

print(f"You have {hero_health} health and Morvath has {enemy_health}\n")
# run the battle
spell_names, spell_damage = read_csv_file(spell_file)
while hero_health > 0 and enemy_health > 0:

    # Hero's attack
    x = input("Press Enter to Attack")
    enemy_health = attack(power, enemy_name, enemy_health)
    if enemy_health <= 0:
        break
    
    # Morvath's spell attack
    x = input("Press Enter to Defend")
    if len(spell_names) > 0:
        idx = random.randint(0, len(spell_names)-1)
        spell = spell_names[idx]
        spell_power = spell_damage[idx]  
        hero_health = magic_attack(hero_health, enemy_name, spell, spell_power)
    else:
        print(f"{enemy_name} fumbles with no spells available!")
        break

if hero_health <= 0 and enemy_health > 0:
    grab_syntak(power,enemy_name, enemy_health)


# display closing narrative
if(enemy_health > 0):
    print("\n" + read_text_file(closing_file))
else:
    print("After a long, hard battle, you succumb to Morvath's attacks. Please run " \
    "the program to try again.")


#################################################
# 9. IDEAS for improvements
"""
What are some ways you could improve this program (add/change)?
What code that you learned this semester would you guess you
would need to use to make these improvements

Improvement #1 
-----------------------------------
What improvement would you add?

Adding more options to the fight, such as different attacks and ways to defend. 

What code would I need to write to make this work?
Input statements to get what attack or defense the player wanted, and then either add to the 
attack function and defense code or make more functions.

Improvement #2
-----------------------------------
What improvement would you add?

More imagery, instead of just text battles. 

What code would I need to write to make this work?
Matplotlib can be used to print images as graphs, so I could use that similar to how the magic 
map was done in lab 8. 


Improvement #3
-----------------------------------
What improvement would you add?
Making the battle a function instead of loose code. I think this would make the code look a little neater but would be a little harder to code. 

What code would I need to write to make this work?
Basic functions. 




"""
