# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:32:46 2020

@author: josh_
"""


import pandas as pd

path_guardado = "C:/Users/josh_/Documents/GitHub/py-diaz-veloz-josue-daniel/03-Panda/data/artwork.pickle"

df = pd.read_pickle(path_guardado)

artistas_duplicados = df['artist']

artistas = pd.unique(artistas_duplicados) #numpy Array

print(artistas.size)
print(len(artistas))

blake = df['artist'] == 'Blake, William'

print(blake.value_counts())

df_blake = df[blake]