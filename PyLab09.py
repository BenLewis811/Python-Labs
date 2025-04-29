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
opening_file = 'opening.txt'
closing_file = 'closing.txt'
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
def read_csv_file(filename):
    """Reads a CSV file containing spell names and damage into NumPy arrays.

    Parameters:
        filename (str): The path to the CSV file. The file should have a header row,
                          with the first column containing spell names (strings) and the
                          second column containing damage inflicted (integers).

    Returns:
        tuple: A tuple containing two NumPy arrays:
               - spell_names (np.ndarray): An array of spell names (strings).
               - damage (np.ndarray): An array of damage values (integers).
               If the file does not exist, returns two empty NumPy arrays.

    Example Usage:
        # Assume you have a CSV file named 'spells_data.csv' with the following content:
        # spell_name,damage
        # Magic Missile,10
        # Fireball,25
        # Ice Bolt,15

        names, damage_values = read_csv_file('spells_data.csv')
        print("Spell Names:", names)
        print("Damage Values:", damage_values)

        names_empty, damage_empty = read_csv_file('non_existent.csv')
        print("Spell Names (non-existent):", names_empty)
        print("Damage Values (non-existent):", damage_empty)
    """
    try:
        df = pd.read_csv(filename)
        spell_names = df.iloc[:, 0].to_numpy(dtype=str)
        damage = df.iloc[:, 1].to_numpy(dtype=int)
        return spell_names, damage
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
    """
    print(f"{enemy_name} attacks with {spell_name}! It deals {spell_power} damage.")
    hero_health -= spell_power
    hero_health = max(hero_health, 0)
    print(f"Hero's health is now {hero_health}.")
    return hero_health


#################################################
# 7. Any other functions needed
#For syntak 
if hero_health <= 0 and enemy_health > 0:
    print("\nYou crawl over to the altar, desperately reach up and grab the Syntak!")
    print("You feel a surge of ancient power coursing through you!")
    enemy_health = attack(power * 10, enemy_name, enemy_health)

#################################################
# 8. Narratives and program run

# display opening narrative
print(read_text_file(opening_file))

# run the battle
spell_names, spell_damage = read_csv_file(spell_file)
while hero_health > 0 and enemy_health > 0:
    # Hero's attack
    enemy_health = attack(power, enemy_name, enemy_health)
    if enemy_health <= 0:
        break
    
    # Morvath's spell attack
    if len(spell_names) > 0:
        idx = random.randint(0, len(spell_names)-1)
        spell = spell_names[idx]
        spell_power = spell_damage[idx]  
        hero_health = magic_attack(hero_health, enemy_name, spell, spell_power)
    else:
        print(f"{enemy_name} fumbles with no spells available!")
        break

if hero_health <= 0 and enemy_health > 0:
    print("\nYou crawl over to the altar, desperately reach up and grab the Syntak!")
    print("You feel a surge of ancient power coursing through you!")
enemy_health = attack(power * 10, enemy_name, enemy_health)

# display closing narrative
print("\n" + read_text_file(closing_file))


#################################################
# 9. IDEAS for improvements
"""
What are some ways you could improve this program (add/change)?
What code that you learned this semester would you guess you
would need to use to make these improvements

Improvement #1 
-----------------------------------
What improvement would you add?


What code would I need to write to make this work?



Improvement #2
-----------------------------------
What improvement would you add?


What code would I need to write to make this work?




Improvement #3
-----------------------------------
What improvement would you add?


What code would I need to write to make this work?





"""