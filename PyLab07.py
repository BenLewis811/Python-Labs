# -*- coding: utf-8 -*-
"""

  Program: CSC115/170 Lab 07 - The Forbidden Forest 
 ----------------------------
  Partner 1:Ben Lewis
  Partner 1s contributions: Made the forest health simulation, and user inputs.

  Partner 2: Esten Odney

  Partner 2s contributions: Made opening and closing narratives. Also helped with debugging and 
  global variables
  
  Date: 
      
      
  Tips:
    1. Read the entire Lab PDF so you understand what you need to do
    2. Describe each partners contributions - not just "Nate did part 1..."
    3. Use proper coding standards
        * All import statements at the top of the code
        * Any constants come next
        * All functions must be placed right after the imports and the constants
        * All functions must have Docstrings describing functionality, parameters, returns and an 
        example
        * Comment your code well - explain WHY you are doing it
        * Space out your code to make it more readable. Use blank lines and spaces around 
        operators.  Use a blank line before and after functions, conditionals and logical blocks.
        * No lines should go past 100 characters wide 
    4. Try not to repeat code.  Use functions and loops. 
    5. Do not use structures or libraries we have not covered in class yet (up through Unit 7)
    6. Rerun the code and test the output before submitting
    7. Work on the lab a little each day. Come to the help sessions if you need assistance
    8. Feel free to change the print snippets and commenting I put in the template.
"""


# Put any import statements here

import random
import numpy as np

################################################
# 1. Global variables

seed_num = 0
tree_health = []




################################################
# 2. Simulate forest health function

def simulate_forest_health(forest):
    """
    This function runs a simulation of the forests health.It runs a loop, with every 
    iteration being 1 day. Every day, the trees with more than 5 health have their health
    multiplied by .9, and the trees with less than 5 health are multiplied by .75. 
    Once a trees health falls below 0.1, its health is set to zero and it is dead. 

    Parameters - The function takes in forest as it's only parameter.  forest is a 1d numpy array
    containting every tree and it's health. 

    returns and prints - Every iteration in the loop is one day. Every iteration, it prints out 
    what day it is and how many trees are dead and how many are alive. When all the trees are dead
    the loop ends. After the loop ends, it prints how many days the forest would last, and 
    returns the amount of days the forest lasted. 

    example: simulate_forest_health(forest) will print 
    "Day  1: Alive Trees =         100 - Dead Trees = 0"
    for every day the forest lasts. When this is done it will print:
    "The forest will be dead in 22 days"
    and return 22
    """

    days = 1
    forest_health = np.where(forest > 0)

    #main loop of the function

    while (len(forest[forest_health]) >= 1):

        #finding indices of > 5, > 0.1, and < .1 health trees. If a tree has less than 0.1
        #health it is considered to be dead.
        #Trees with more than 5 health are indexed as healthy trees, and trees with less than or 
        #equal to 5 health are indexed as unhealthy trees. 
        healthy_tree = np.where(forest > 5)
        unhealthy_tree = np.where((forest >= 0.1) & (forest <=5))
        dead_tree = np.where(forest < 0.1)
        alive_tree = np.where(forest > 0.1)

        #Printing what day it is and how many trees are left. The variables alive and dead are 
        #created simply to save horizontal space. 
        #print(len(alive_tree), alive_tree)
        alive = len(forest[alive_tree])
        dead = len(forest[dead_tree])
        print(f"Day {days:>2}: Alive Trees = {alive:>11,d} - Dead Trees = {dead:,d} ")

        #Adjusting the health of the trees according to the lab directions
        forest[healthy_tree] *= 0.9
        forest[unhealthy_tree] *= 0.75
        forest[dead_tree] = 0

        #Sets the forest health list equal to the amount of living trees. Onces the living trees
        #are gone the list will be empty. 
        forest_health = np.where(forest > 0)
        #adding days
        days += 1
    print(f"The forest will be dead in {days - 1} days")
    return days




################################################
# 3. Display Opening Narrative

print('''

                          Lab 7 - Forbidden Forest
                     -----------------------------------

The air grows heavy as you step from the murky swamp into the shadow of the Forbidden Forest.
An unnatural stillness hangs between the skeletal trees, their once-vibrant leaves now brittle
and brown. Your duck lets out a quiet quack, pressing close to your side as the last of the
swamp's fog dissipates behind you.

The hunched figure who guided you through the marshes suddenly straightens, her form shimmering
like sunlight through leaves. With a fluid motion, she casts off her tattered cloak, revealing
hair that flows like a willow's branches and eyes that glow with ancient wisdom.

"I am Nyssa," she says, her voice both musical and mournful. "Guardian of these woods, now
witness to their slow demise." She gestures to the dying trees around you. "Morvath the
Malevolent has stolen the syn-tak - the heart of our forest. With each passing hour, he drains
more of its power while the trees wither and my strength fades."

She presses a small vial into your hand, its contents pulsing with golden light. "This is the
last of the forest's essence. Use it wisely, for time runs short." As you pocket the vial,
Nyssa's form flickers like a guttering candle. "We must know how long we have before the forest
is lost forever. Will you help me calculate our remaining days?"

The ground beneath your feet feels unnaturally warm, as if the earth itself is feverish. In
the distance, an unnatural purple glow pulses from deep within the forest - Morvath's dark
fortress. Ducky Momo nibbles at your sleeve, its beady eyes full of concern.

        -----------------------------------------------------------------------

    ''') 

 #I decided to keep the same intro message as it is a rather simple and good introdrcution
################################################
# 4. Run the forest health function

#Collecting user data. This will be used to set the seed for the random numbers and determine how 
#many trees there are. 
seed_num = eval(input("Enter the seed number:"))
tree_health = eval(input("Enter the number of trees. (max 999 million):"))
np.random.seed(seed_num)

#Sets up a 1d np array to represent the forest. The trees have a random amount of health from 1-10
#The health and amount of trees are entered earlier by the user.

#####################################################
# 5. Run the Forest Health Simulation and save return value
forest = np.random.randint(1, 11, size=tree_health).astype(float)
forest_lifespan = simulate_forest_health(forest)


################################################
# 6 Closing narrative including days left result

print(f"""
        -----------------------------------------------------------------------

 The final numbers appear before you in glowing runes. Your hands tremble as you turn to Nyssa,
whose form has grown noticeably more translucent. "{forest_lifespan-1} days," you whisper. "The
forest has {forest_lifespan-1} days before..." The words catch in your throat.

Nyssa nods solemnly, her leaf-like hair rustling though there's no wind. "So little time," she
murmurs. Then suddenly she straightens, her eyes flashing with renewed determination. "But
enough! The path to Morvath's tower lies through the Valley of Whispers. Dangerous, yes, but
with your skills and..." she smiles at your duck, "...this brave companion, we may yet succeed."

Your Ducky Momo puffs its chest proudly at the praise.

"The syn-tak rests in Morvath's obsidian vault," Nyssa continues. "We must retrieve it before
the last tree falls, or all will be lost." She places a hand on your shoulder, her touch like
sun-warmed bark. "Will you join me on this perilous quest?"

You glance at the simulation results one last time - {forest_lifespan-1} days to save the forest,
to save Nyssa, to save all of Coderia. Your duck meets your gaze and gives a determined nod.

"Then let's begin," you say, tightening your grip on your Sword. The first light of dawn filters
through the dying trees as you set off toward the Valley of Whispers, the countdown to the
forest's doom echoing in your mind: {forest_lifespan-1} days remain.
    
    """)

