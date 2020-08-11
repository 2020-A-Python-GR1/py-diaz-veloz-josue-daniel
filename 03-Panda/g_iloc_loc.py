# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:58:16 2020

@author: josh_
"""


import pandas as pd


path_guardado = "C:/Users/josh_/Documents/GitHub/py-diaz-veloz-josue-daniel/03-Panda/data/artwork.pickle"

df = pd.read_pickle(path_guardado)

primero = df.loc[1035]

print(primero)
print(primero['artist'])
print(primero.index)

serie_vertical = df['artist']

print(serie_vertical)
print(serie_vertical.index)


segundo = df.loc[1035] #filtrado por indice
segundo = df.loc[[1035,1036]] #filtrado por arreglo de indices
segundo = df.loc[3:5] #filtrado desde x hasta y inidice

sedundo = df.loc[df.index == 1035] #filtrado por Arreglo true y false


segundo = df.loc[1035,'artist'] #1 indice
segundo = df.loc[1035,['artist','medium']] #Varios indices


tercero = df.iloc[0]
tercero = df.iloc[[0,1]]
tercero = df.iloc[0:10]
tercero = df.iloc[df.index == 1035]

tercero = df.iloc[0:10,0:4]



