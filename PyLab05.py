# -*- coding: utf-8 -*-
"""

  Program: CSC115/170 Lab 05 - The Swamp of Shadows
 ----------------------------
  Partner 1: Esten Odney 
  Partner 1s contributions:

  Partner 2: Ben Lewis
  Partner 2s contributions: 
  
  Date: 3/25/25
      
      
  Tips:
    1. Read the entire Lab PDF so you understand what you need to do
    2. Describe each partners contributions - not just "Nate did part 1"
    3. Use proper coding standards
        * All import statements at the top of the code
        * All functions must be placed right after the imports (and after constants)
        * All functions must have **Docstrings** describing functionality, parameters, returns and 
          an example
        * Comment your code well - explain **WHY** you are doing it
        * Space out your code to make it more readable. Use blank lines and spaces around operators.  
          Use a blank line before and after functions, conditionals and logical blocks.
        * No lines should go past **100** characters wide 
    4. Try not to repeat code.  Use functions and loops
    5. Do not use structures we have not covered in class yet.
    6. Double check all outputs have units and are rounded correctly.
    7. Rerun the code and test the output before submitting
    8. Work on the lab a little each day. Come to the help session if you need assistance
      
"""

################################################
# Put any import statements here
import random


################################################
# 1. setup hero stats and enemies

# enemies 2d tuple
ENEMIES = (
    ('fluffy', 2, 10),
    ('eric', 5, 50),
    ('mr. nesbit', 3, 20),
    ('blight beetle', 1, 12),
    ('marsh troll', 8, 100),
    ('mud crab', 3, 25),
    ('murk wraith', 6, 45),
    ('swamp hag', 7, 60),
    ('bog imp', 2, 15),
    ('quicksand ooze', 4, 35)
)



################################################
# 2. attack and defend Functions from Lab 4
def attack(power, enemy_name, enemy_health):
    """
    This is the attack function. 
    Its parameters take in the power, enemy_name, and enemy_health.
    It will print how much you attacked for, and how much health the enemy has left. 
    If the enemy has no health it will print that the enemy is defeated
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
    
def defend(hero_health, enemy_power, duck_status, enemy_name):
    """
    This Function will take the enemy's power and multiply it before taking it away from the hero's
    health. with the duck status true, it will reduce the number through integer division of 5.
    It takes in the hero_health, enemy_power, and duck_status parameters.
    It returns the updated hero_health if duck_status is ture or not.
    Example: defend(50, 10, true) ->  returns: hero_health - 2
    """
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



################################################
# 3. Write function to display statistics
def display_battle_stats(enemies_encountered, enemy_dmg, hero_dmg):
    """
    This Function displays the statistics that are gathered throughout the entire travel through
    the swamp.
    Its parameters are the enemies_encountered, the enemy_dmg and the hero_dmg.
    It returns nothing as its void.
    At the End of the code, it will print out the he names of all enemies encountered in 
    alphabetical order, the total damage inflicted by the hero, the average damage inflicted 
    and recieved by the hero on/by each enemy, the most/least dangerous enemy encountered and 
    how much damage they inflicted, and finally the strongest/weakest enemy encountered and 
    how many hit points it took to defeat them. 
    Example:
    Enemies encountered:
----------------------------------------
Blight Beetle
Marsh Troll
Reedsnapper
Silt Stalker
Total damage given: 197
Average damage given: 49.2
Average damage received: 2.0
----------------------------------------
Enemy stats
----------------------------------------
Most dangerous: Silt Stalker gave 5 damage
Least dangerous: Blight Beetle gave 0 damage
Strongest: Marsh Troll took 100 to defeat
Weakest: Blight Beetle took 12 to defeat
    """
    
    # This Prints all enemies encountered in alphabetical order
    print("Enemies encountered:")
    print("----------------------------------------")
    for enemy in sorted(enemies_encountered):
        print(enemy.title())
    
    # Calculates and prints the damage statistics and the averages down to 1 decimal
    # Here I consulted AI on how to start this part, but there wasn't a straight copy/paste done
    total_hero_dmg = sum(hero_dmg)
    avg_hero_dmg = total_hero_dmg / len(hero_dmg) if hero_dmg else 0
    avg_enemy_dmg = sum(enemy_dmg) / len(enemy_dmg) if enemy_dmg else 0
    
    print(f"\nTotal damage given: {total_hero_dmg}")
    print(f"Average damage given: {avg_hero_dmg:.1f}")
    print(f"Average damage received: {avg_enemy_dmg:.1f}")
    
    # Calculate most/least dangerous enemies (by damage dealt to the hero)
    print("----------------------------------------")
    print("Enemy stats")
    print("----------------------------------------")
    
    if enemies_encountered:
        # Most and least dangerous enemies, had to cut the prints in half to fit the 100 char rule
        max_dmg_index = enemy_dmg.index(max(enemy_dmg))
        min_dmg_index = enemy_dmg.index(min(enemy_dmg))
        print(f"Most dangerous: {enemies_encountered[max_dmg_index].title()} ")
        print(f"gave {enemy_dmg[max_dmg_index]} damage")
        print(f"Least dangerous: {enemies_encountered[min_dmg_index].title()}")
        print(f"gave {enemy_dmg[min_dmg_index]} damage")
        
        # Strongest and weakest enemies (by health points)
        # got the original enemy data here to get health points for them during encounters
        enemy_healths = []
        for enemy_name in enemies_encountered:
            for enemy in ENEMIES:
                if enemy[0] == enemy_name:
                    enemy_healths.append(enemy[2])
                    break
        # Similarily to above I had to cut the prints in half to fit them properly
        max_health_index = enemy_healths.index(max(enemy_healths))
        min_health_index = enemy_healths.index(min(enemy_healths))
        print(f"Strongest: {enemies_encountered[max_health_index].title()}")
        print(f"took {enemy_healths[max_health_index]} to defeat")
        print(f"Weakest: {enemies_encountered[min_health_index].title()}") 
        print(f"took {enemy_healths[min_health_index]} to defeat")
    else:
        print("No enemies encountered!")

################################################
# 4. Set the stage
#display a short introduction
print("You travel with your duck, into a great swamp.")
print("A thick mist clouds your vision, as your feet sink in the mud.")
print("Suddenly, a hunched figure appears. You approach it with your valiant duck by your side.")
print("The figure asks for assistance in crossing the great swamp.")
print("You agree, however the figure tells you to beware of the ten clearings.")
print("As you head into the first clearing, a battle ensues.")



################################################
# 5. Traverse the swamp
hero_health = 50
hero_power = 10  
duck_status = True  

enemies_encountered = []
enemy_damages = []
hero_damages = []

# loop through all 10 clearings and with a 50% chance to encounter
for clearing in range(1, 11):
    print(f"\nYou come to clearing {clearing} on your journey.")
    if random.random() < 0.5:
        print("You do not encounter any enemies and continue on your journey.")
        continue
    
    enemy = random.choice(ENEMIES)
    enemy_name, enemy_pwr, enemy_hp = enemy
    current_enemy_hp = enemy_hp
    enemies_encountered.append(enemy_name)
    print(f"A vicious {enemy_name} emerges from the swamp.")
    print(f"It has {enemy_pwr} power and {enemy_hp} health.")
    print(f"You have {hero_health} health and the {enemy_name} has {current_enemy_hp} health.")
    
    hero_dmg_current = 0
    enemy_dmg_current = 0
    
    while hero_health > 0 and current_enemy_hp > 0:
        # Hero's attack turn
        input("➭ Press Enter to attack...")
        prev_hp = current_enemy_hp
        current_enemy_hp = attack(hero_power, enemy_name, current_enemy_hp)
        hero_dmg_current += (prev_hp - current_enemy_hp)
        
        if current_enemy_hp <= 0:
            print(f"☠ The {enemy_name} has been slain, vanquished by our hero.")
            break
        
        # Enemy's attack turn
        input(f"➭ The {enemy_name} readies their attack. Press Enter to defend...")
        prev_hero = hero_health
        hero_health = defend(hero_health, enemy_pwr, duck_status, enemy_name)
        enemy_dmg_current += (prev_hero - hero_health)
        
        if hero_health <= 0:
            break
        
        print(f"You have {hero_health} health and the {enemy_name} has {current_enemy_hp} health.")
    
    hero_damages.append(hero_dmg_current)
    enemy_damages.append(enemy_dmg_current)
    
    if hero_health <= 0:
        break

################################################
# 6. Closing narrative with statistics
if hero_health > 0:
  print("At long last, you emerge from the tenth clearing victorious.")
  print("It looks like Ducky Momo and the mysterious figure are alive as well.")
  print("As you leave the swamp, you enter the Forbidden Forest.")

if hero_health <= 0:
  print("Unfortunately, you did not survive this encounter.")
  print("With you dead, Ducky Momo is left to fight through the swamp by himself.")
  print("Incredibly, he doesn't struggle at all to clear the remaining monsters.")
  print("It is unclear why he didn't help earlier if he was so strong.")

#Statstics
display_battle_stats(enemies_encountered, enemy_damages, hero_damages)
