# -*- coding: utf-8 -*-
"""

  Program: CSC115/170 Lab 04 - Feathers of Fortitude
 ----------------------------
  Partner 1:  
  Partner 1s contributions:

  Partner 2: Ben Lewis
  Partner 2s contributions: 
  3 and 5, opening narrative
  Date: 
      
      
  Tips:
    1. Read the entire Lab PDF so you understand what you need to do
    2. Describe each partners contributions - not just "Nate did part 1"
    3. Use proper coding standards
        * All import statements at the top of the code
        * Comment your code well - explain **WHY** you are doing it
        * Space out your code to make it more readable. Use blank lines and spaces around operators
        * No lines should go past **100** characters wide
        * All functions have **Docstrings** describing functionality, parameters, returns and an example
    4. Try not to repeat code.  Use functions and loops
    5. Do not use structures we have not covered in class yet.
    6. Double check all outputs have units and are rounded correctly.
    7. Rerun the code and test the output before submitting
    8. Work on the lab a little each day. Come to the help session if you need assistance
      
"""


# Put any import statements here
import math
import random

# character attributes
# def myhero():

################################################
# 1. Set the stage with a short introduction
print("After you leave the labyrinth, you approach a misty swamp.")
print("Before entering the swamp, you decide to sharpen your sword.")
print("As you pull the sword out, you realize there is a new golden jewel on the hilt.")
print("You inspect the jewel, and in a flash a duck appears.")
print("You find the Duck can magically increase your strength, and can be toggle with the jewel")

################################################
# 2. Introduce your duck
print("The ducks name is ducky momo")
duckyName = "Ducky Momo"
duckyColor = "Yellow"



################################################
# 3. toggle duck function
print("""
        -----------------------------------------------------------------------

    "First you will learn to summon me from the sword", your feathered friend says.
    """)

def toggle_duck(current_status):
    """
    This function toggles the duck on and off. It returns the opposite of the parameter,
     them prints whether the duck is on or off. It then returns the status of the toggled duck.
    """

    if current_status == True:
        print("The duck has been toggled off")
        return False
    else:
        print("The Duck has been toggled on")
        return True



################################################
# 4. Quack function
print("""
        -----------------------------------------------------------------------

    "Next, I will show you my mighty quack, which will give you extra strength in battle."
    """)

def quack(old_power, duckyName, duck_status):
    if duck_status:
        quack_power = old_power * random.randint(2, 4)
        print(f"📢 {duckyName} lets out a mighty (but still cute) quack.")
        print(f"You feel much stronger, your power is now {quack_power}")
        return quack_power
    else:
        print("🚫 Nothing happens, maybe you need to call your duck first")
        return old_power
    """
    This function quacks the duck, and amplifies the hero's damage if the duck is toggled on. 
    If the duck is toggled off it does not amplify damage.
    """


################################################
# 5. Attack function
print("""
        -----------------------------------------------------------------------

    "You already know how to do battle, but with me by your side, you will be much more effective."

    "Consider this hay bale with 10 health points.  Can you defeat it?  Try both with and without 
    my mighty quack."
    """)    
def attack(power, enemy_name, enemy_health):
    """
    This is the attack function. It will print how much you attacked for, and how much health the
    enemy has left. If the enemy has no health it will print that the enemy is defeated
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


################################################
# 6. Defend Function
print("""
        -----------------------------------------------------------------------

    "Now, let me show you to increase your defensive stance.  With me by your side, we will be 
    able withstand many a blow.

    "I'm going to throw this rock at you", your feathered friend says,  "The rock attacks with a 
    power of 2. Can you withstand its force?"
    """)   
def defend(hero_health, enemy_name, enemy_power, duck_status):
    enemy_attack = enemy_power * random.randint(1, 6)
    if duck_status:
        enemy_attack = enemy_attack // 5
        print("The duck defense reduces it to", enemy_attack)
    hero_health -= enemy_attack
    print(f"🔰 You have been attacked for {enemy_attack} points")
    if hero_health <= 0:
        print("💀 You have been defeated!")
    else:
        print(f"😣 You have {hero_health} health points left")
    return hero_health

    """
    Reduces the hero's health by the enemy's attack power, multiplied by a random integer. If the
    duck is toggled on the damage will be divided by 5
    """

################################################
# 7. Attack simulation
def attacksim():
    """
    Simulates the battle. This is the main function of the lab. 
    """


    

################################################
# 8. Closing narrative

# check if defeated
