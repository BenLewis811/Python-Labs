# -*- coding: utf-8 -*-
"""

  Program: CSC115/170 Lab 08 - The Map of Destiny
 ----------------------------
  Partner 1:  Ben Lewis
  Partner 1s contributions: First plot, and total original distance calculations

  Partner 2: Esten Odney
  Partner 2s contributions: Completed the second plot, The closing narrative, and some debugging
  
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
        operators. Use a blank line before and after functions, conditionals and logical blocks.
        * No lines should go past 100 characters wide 
    4. Try not to repeat code.  Use functions and loops. 
    5. Do not use structures or libraries we have not covered in class yet (up through Unit 7)
    6. Rerun the code and test the output before submitting
    7. Work on the lab a little each day. Come to the help sessions if you need assistance
    8. Feel free to change the print snippets and commenting I put in the template.
"""

################################################
# 1. Imports
import numpy as np
import matplotlib.pyplot as plt 
import math

################################################
# 2. Create NumPy arrays of x and y values we have visited and location names
loc = np.array(["Capital", "Barrier", "Archery Field", "Alchemist","Labyrinth","Swamp","Forest"])
x = np.array([0.5,2,2.5,3,4,6,7])
y = np.array([4,3.5,5.5,6,5,4,5])
################################################
# 3. Function to plot the map
def plot_map(loc,x,y,mapTitle, mapColor):
    """
    This function plots the map desired when called. 
    It's parameters are:
    loc: numpy array of the names of the locations
    x: numpy array of the x values of the locations
    y: numpy array of the y values of the locations
    mapTitle: String containing the title of the map
    mapColor: String containing the color value the map will be
    The function is a void function and has no return value. After the function is called, it
    will print the graph.
    """
    plt.figure() 
    #Load and display background
    background_image = plt.imread("lab08-background.png")   
    plt.imshow(background_image, aspect='auto', extent=[0,8,0,8])
    plt.plot(x,y,color = mapColor,marker="*")
    plt.title(mapTitle)
    plt.xlabel("Days Journey")
    plt.ylabel("Days Journey")
    plt.grid(True)
    plt.ylim(0, 8)
    plt.xlim(0, 8)
    
    #itirates through the locations and annotates them 
    for i in range(len(loc)):
        plt.annotate(
            loc[i],
            xy = (x[i],y[i])
        )
    plt.show()

################################################
# 4. Display your opening narrative and plot the map
print('''

                          Lab 8 - The Map of Destiny
                     -----------------------------------
            After learning the fate of the forest, you realise how quickly Morvath must be stopped.
      You ask Nyssa what to do, and she hands you a magical map. This map reveals your journey so 
      far, and shows hidden passeges through the forest. The map lays out a path to lead you to the
      ancient stones. These stones hide the lair of Morvath. While the map has told you where to 
      to, it will not protect you from his dark magic. 

        -----------------------------------------------------------------------

    ''')

plot_map(loc,x,y,"Journey so far","red")


################################################
# 5. Calculate and Display distances for each part of the journey
#Printing the title
print("From:         To:          Distance:(miles)")
print(f"-----         ----         ---------------")

#converting days to miles and setting up total distance travelled variable
totalDistance = 0
xmiles = x * 10
ymiles = y * 10

#Calculates distance from location to location. Prints distance table and adds it all to total
#distance.
for i in range(1,len(loc)):
    distance = math.sqrt((xmiles[i]-xmiles[i-1])**2 + (ymiles[i]-ymiles[i-1])**2)
    print(f"{loc[i-1]:<15}{loc[i]:<15}{distance:<4,.3}")
    totalDistance += distance

#printing the distance
print(f"Total Distance: {totalDistance:.2f} miles")

################################################
# 6. Find Morvath's Location and append to arrays
# Morvath's Location is 2.5 days journey at an angle of 1.25 times your total distance travelled 
# in miles


# Calculates distances and angle
distances = [math.hypot(x[i+1]-x[i], y[i+1]-y[i]) for i in range(len(x)-1)]
total_miles = sum(distances) * 10  # Converts to imperial miles
angle_deg = (5/4) * total_miles
angle_rad = math.radians(angle_deg)

# Calculates Grotto position from Forest (last point)
grotto_x = x[-1] + 2.5 * math.cos(angle_rad)
grotto_y = y[-1] + 2.5 * math.sin(angle_rad)

# Append new location
loc = np.append(loc, "Morvath's Grotto")
x = np.append(x, grotto_x)
y = np.append(y, grotto_y)

# Verifies coordinates are within bounds
print(f"Grotto coordinates: X: {grotto_x:.2f}, Y: {grotto_y:.2f} (must be 0-8)")
input("Press Enter to show complete map...")

# 7. Plot updated map with new coordinates
plot_map(loc,x,y,
         "Path to Morvath's Hidden Lair",  # Different title
         "gold")  # Different color

################################################
# 8. Tell the ending Story

print(f"""
        -----------------------------------------------------------------------
   With the map now displaying a glowing dotted line like a fantasy GPS, you mutter,
"Should've brought snacks for this dramatic final walk." Ducky Momo looks up at you and 
quacks, "If I wanted a mud bath, I’d have booked a spa day!" as you slosh through another 
puddle that definitely wasn't on the map.

The "ancient stones" turn out to look suspiciously like a villain's Airbnb listing - 
complete with ominous glowing pentagram welcome mat. "5/5 stars would summon dark forces 
again," you joke nervously, while your duck hides behind a suspiciously normal-looking 
shrub.

With a deep breath and your duck sporting a tiny battle helmet, you declare: "Let's 
get this over with before the local tavern closes for last call!" The Syntak better 
be under that rock. That specific rock. No, the other rock.
  
    """)
