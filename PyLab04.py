# -*- coding: utf-8 -*-
"""

  Program: CSC115/170 Lab 04 - Feathers of Fortitude
 ----------------------------
  Partner 1:  Esten Odney
  Partner 1s contributions:

  Partner 2: Benjamin Lewis
  Partner 2s contributions: 
  
  Date: March 3, 2025
      
      
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
import random

# character attributes
duck_status = False
power = 5
hero_health = 50

################################################
# 1. Set the stage with a short introduction       BEN
print("After you leave the labyrinth, you approach a misty swamp.")
print("Before entering the swamp, you decide to sharpen your sword.")
print("As you pull the sword out, you realize there is a new golden jewel on the hilt.")
print("You inspect the jewel, and in a flash a duck appears.")
print("You find the Duck can magically increase your strength, and can be toggled with the jewel")


################################################
# 2. Introduce your duck        ESTEN
duckyName = "Ducky Momo"
duck_color = "Yellow"
print(f"""
The {duck_color} duck lands gracefully on the grass next to you and excitedly
begins to speak. "My name is {duckyName}", it quacks. "And I have been
sent by Ordin to assist you on your quest. Together we will defeat the evil
sorcerer and recover the Syn-tak - the mystical code that will heal the
king."

{duckyName} gets closer to you and whispers, "But first I will need to
teach you some new skills. Follow me!"

The duck walks over the crest of the hill, its {duck_color} feathers swaying as it
waddles. Obediently, you grab your effects and follow it, ready to train.
-----------------------------------------------------------------------
""")

################################################
# 3. toggle duck function           BEN

def toggle_duck(duck_status):
    #This function toggles the duck on and off. It returns the opposite of the parameter,
    #then prints whether the duck is on or off. It then returns the status of the toggled duck
    if duck_status == True:
        print("The duck has been toggled off")
        return False
    else:
        print("The Duck has been toggled on")
        return True
print('"First you will learn to summon me from the sword", your feathered friend says.')
print(f"Current duck status is {duck_status}")
input("➭ Press Enter to toggle duck...")
duck_status = toggle_duck(duck_status)
print(f"Current duck status is {duck_status}")
input("➭ Press Enter to toggle duck...")
duck_status = toggle_duck(duck_status)
print("-----------------------------------------------------------------------")



################################################
# 4. Quack function             ESTEN
def quack(old_power, duckyName, duck_status):
    if duck_status:
        quack_power = old_power * random.randint(2, 4)
        print(f"📢 {duckyName} lets out a mighty (but still cute) quack.")
        print(f"You feel much stronger, your power is now {quack_power}")
        return quack_power
    else:
        print("🚫 Nothing happens, maybe you need to call your duck first")
        return old_power
print('"Next, I will show you my mighty quack, which will give you extra strength in battle."')
print(f"Your power is currently {power}")
print(f"Current duck status is {duck_status}")
input("➭ Press Enter to attempt quack...")
power = quack(power, duckyName, duck_status)
print("Now with duck power")
print(f"Your power is currently {power}")
input("➭ Press Enter to toggle duck...")
duck_status = toggle_duck(duck_status)
input("➭ Press Enter to attempt quack...")
power = quack(power, duckyName, duck_status)
print("-----------------------------------------------------------------------")


################################################
# 5. Attack function       BEN
    
def attack(power, enemy_name, enemy_health):
    #This is the attack function. It will print how much you attacked for, and how much health the
    #enemy has left. If the enemy has no health it will print that the enemy is defeated

    attack = power * random.randint(1,6)
    print(f"You attacked {enemy_name} for {attack} damage")

    enemy_health = enemy_health - attack
    if enemy_health > 0:
        print(f"{enemy_name} has {enemy_health} hitpoints left.")
        return enemy_health
    else:
        print(f"You have slain {enemy_name}")
        return 0
print('"You already know how to do battle, but with me by your side,') 
print(' you will be much more effective."')
print('"Consider this hay bale with 10 health points. ')
print('Can you defeat it? Try both with and without my mighty quack."')
input("➭ Press Enter to toggle duck...")
duck_status = toggle_duck(duck_status)
print(f"Your power is currently {power}")
print(f"Current duck status is {duck_status}")
input("➭ Press Enter to attack...")
enemy_health = attack(power, "the first hay bale", 10)
if enemy_health == 0:
        print("Now with duck power")
        input("➭ Press Enter to toggle duck...")
        duck_status = toggle_duck(duck_status)
        input("➭ Press Enter to attempt quack...")
        power = quack(power, duckyName, duck_status)
        input("➭ Press Enter to attack...")
        attack(power, "the second hay bale", 10)
print("-----------------------------------------------------------------------")

################################################ 
# 6. Defend Function    ESTEN
  
def defend(hero_health, enemy_name, enemy_power, duck_status):
    enemy_attack = enemy_power * random.randint(1, 6)
    if duck_status:
        enemy_attack = ( enemy_attack // 5 )
        print("The duck defense reduces it to", enemy_attack)
    hero_health -= enemy_attack
    print(f"🔰 You have been attacked for {enemy_attack} points")
    if hero_health <= 0:
        print("💀 You have been defeated!")
    else:
        print(f"😣 You have {hero_health} health points left")
    return hero_health

print('"Now, let me show you to increase your defensive stance. ')
print('With me by your side, we will be able withstand many a blow.')
print('"I\'m going to throw this rock at you", your feathered friend says, ')
print('"The rock attacks with a power of 2. Can you withstand its force?"')
input("➭ Press Enter to toggle duck...")
duck_status = toggle_duck(duck_status)
print(f"Current duck status is {duck_status}")
input("➭ The rock readies their attack. Press Enter to defend...")
hero_health = defend(hero_health, "the rock", 2, duck_status)
print("Now with duck power")
input("➭ Press Enter to toggle duck...")
duck_status = toggle_duck(duck_status)
print(f"Duck status is now {duck_status}")
input("➭ The rock readies their attack. Press Enter to defend...")
hero_health = defend(hero_health, "the rock", 2, duck_status)

################################################
# 7. Attack simulation      Both worked on here
duck_status = True  # Duck starts toggled on
monster_name = "Swamp Troll"
monster_health = 100
monster_power = 10

print(f"\nA wild {monster_name} appears! It has {monster_health} health and {monster_power}") 
print("attack power.")
print("Prepare for battle!\n")

while hero_health > 0 and monster_health > 0:
        # Hero's turn
        print(f"Your power is currently {power}")
        print(f"Current duck status is {duck_status}")
        action = input("Do you choose to (A)ttack, (T)oggle Duck or (Q)uack? ").strip().lower()

        # Makes sure the input are a/t/q and nothing else
        while action not in ['a', 't', 'q']:
            print("Invalid input. Please choose (A)ttack, (T)oggle Duck, or (Q)uack.")
            action = input("Do you choose to (A)ttack, (T)oggle Duck or (Q)uack? ").strip().lower()

        # Here the actions can be input
        if action == 'a':
            input("➭ Press Enter to attack...")
            monster_health = attack(power, monster_name, monster_health)
        elif action == 't':
            input("➭ Press Enter to toggle duck...")
            duck_status = toggle_duck(duck_status)
        elif action == 'q':
            input("➭ Press Enter to attempt quack...")
            power = quack(power, duckyName, duck_status)

        # Check if monster is defeated
        if monster_health <= 0:
            break

        # Monster's turn
        input(f"➭ The {monster_name} readies their attack. Press Enter to defend...")
        hero_health = defend(hero_health, monster_name, monster_power, duck_status)



################################################
# 8. Closing narrative      ESTEN
if hero_health > 0:
        print(f"\n🎉 You and {duckyName} have defeated the {monster_name}! 🎉")
        print("With the monster vanquished,") 
        print("you set off across the swamp towards the Forbidden Forest,") 
        print("ready for your next adventure.")
else:
        print(f"\n💀 You have been slain by the {monster_name}. 💀")
        print("Your journey ends here, but your legend will live on in the hearts of ")
        print("those who dare to follow in your footsteps.")

