import numpy as np
import pandas as pd
import os

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


# test code
# - file not found
filename = 'nofile.csv'
spellnames, spellpower  = read_csv_file(filename)
print(f"datatypes spellnames:{type(spellnames)}, spellpower:{type(spellpower)}")
if np.size(spellnames) == 0:
    print("Array is empty\n")


# - file exists
filename = 'spells.csv'
print(f"File: {filename}")
spellnames, spellpower  = read_csv_file(filename)
print(f"datatypes spellnames:{type(spellnames[0])}, spellpower:{type(spellpower[0])}\n")


for i in range(np.size(spellnames)):
    print(spellnames[i], spellpower[i])