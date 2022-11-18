import numpy as np
import pandas as pd


print(" ")
pokemon = pd.DataFrame({
    'Atak': [19, 52, 48, 55, 45],
    'Savunma': [49, 43, 60, 40, 160],
    'Hız': [45, 65, 43, 90, 70],
    'Tür': ['Ot', 'Ateş', 'Su', 'Elektrik', 'Kaya']
}, index=["Bulbasaur", "Charmander", "Squirtle", "Pikachu", "Onix"])
"""
print(pokemon.info())
print(" ")
print(pokemon)
print(" ")
print(pokemon.size)
print(" ")
print(pokemon.shape)
print(" ")
print(pokemon.describe()) 
"""

pokemon.append(pd.Series({
    "Atak": 104,
    "Savunma": 78,
    "Tür": "Ateş",
    "Hız": 100,
    "Boy": 1.7}, name="Chizard"))
print(pokemon)