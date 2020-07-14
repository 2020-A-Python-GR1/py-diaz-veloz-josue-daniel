# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 07:57:36 2020

@author: josh_
"""


import numpy as np
import pandas as pd

lista_numeros=[1,2,3,4]
tupla_numeros=(1,2,3,4)
np_numeros = np.array((1,2,3,4))

series_a = pd.Series(lista_numeros)
series_b = pd.Series(tupla_numeros)
series_c = pd.Series(np_numeros)


series_d = pd.Series([
    True,
    False,
    12,
    12.45,
    "Josue",
    None,
    (1),
    [2],
    {"nombre":"Josue"}
    ]
    )

print(series_d[3])


lista_cuidades = [
    "Ambato",
    "Cuenca",
    "Loja",
    "Quito"
    ]

series_cuidad= pd.Series(lista_cuidades,
                         index=["A","C","L","Q"])

valores_cuidad = {
    "Ibarra":9500,
    "Guayaquil": 10000,
    "Cuenca": 7000,
    "Quito": 8000,
    "Loja": 3000
    }

serie_valor_cuidad = pd.Series(valores_cuidad)

cuidades_menor_5k = serie_valor_cuidad <5000

print(type(serie_valor_cuidad))
print(type(cuidades_menor_5k))
print(cuidades_menor_5k)


serie_valor_cuidad = serie_valor_cuidad*1.1

serie_valor_cuidad["Quito"] = serie_valor_cuidad["Quito"] -50

print("Lima" in serie_valor_cuidad)












