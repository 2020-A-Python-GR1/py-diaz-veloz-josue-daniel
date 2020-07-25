# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 08:47:11 2020

@author: josh_
"""


import numpy as np
import pandas as pd

arr_pand = np.random.randint(0,10,6).reshape(2,3)

df1 = pd.DataFrame(arr_pand)

s1 = df1[0]
s2 = df1[1]
s3 = df1[2]


df1[3] = s1

df1[4] = s1 *s2


dato_fisicos_uno = pd.DataFrame(
    arr_pand,
    columns =[
        'Estatura (cm)',
        'Peso (kg)',
        'Edad (anios)'
        ]
    )

dato_fisicos_dos = pd.DataFrame(
    arr_pand,
    columns =[
        'Estatura (cm)',
        'Peso (kg)',
        'Edad (anios)'
        ],
    index =[
        'Josue',
        'Diaz']
    
    )

serie_peso = dato_fisicos_dos['Peso (kg)']
datos_josue = serie_peso['Josue']
print(serie_peso)
print(datos_josue)



df1.index = ['Wendy','Carolina']
df1.columns = ['A','B','C','D','E']