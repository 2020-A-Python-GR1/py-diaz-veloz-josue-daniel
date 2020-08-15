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


##########################################

datos ={
        "nota 1":{
            "Pepito":7,
            "Juanita": 8,
            "Maria": 9
            },
        "nota 2":{
            "Pepito":7,
            "Juanita": 8,
            "Maria": 9
            },
        "disciplina":{
            "Pepito":4,
            "Juanita": 9,
            "Maria": 2
            }
        }

notas = pd.DataFrame(datos)

condicion_nota = notas["nota 1"]> 7

condicion_nota_dos = notas["nota 2"]> 7


condicion_disc = notas["disciplina"]> 7

mayores_siete = notas.loc[ condicion_nota, ["nota 1"]]

pasaron = notas.loc[condicion_nota][condicion_nota_dos][condicion_disc]

notas.loc["Maria", "disciplina"] = 7

notas.loc[:, "disciplina"] = 7


##### Promedio de las 3 notas (no1+no2+disc)/3

promedio = (notas.loc[:,"disciplina"] + notas.loc[:,"nota 1"]+notas.loc[:,"nota 2"])/3
notas["Promedio"]=promedio





















