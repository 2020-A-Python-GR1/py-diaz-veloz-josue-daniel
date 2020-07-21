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


svr_cuidades = np.square(serie_valor_cuidad)

cuidades_uno = pd.Series({
    "Montañita": 300,
    "Guayaquil": 10000,
    "Quito": 2000
    })

cuidades_dos = pd.Series({
    "Loja": 300,
    "Guayaquil": 10000,
    })

cuidades_uno["Loja"] = 0



print(cuidades_uno+cuidades_dos)


cuidades_add = cuidades_uno.add(cuidades_dos)


cuidades_concatenada = pd.concat(
    [cuidades_uno,cuidades_dos])


cuidades_conct_verify = pd.concat(
    [cuidades_uno,cuidades_dos],
    verify_integrity=False
    )

cuidades_append_verify = cuidades_uno.append(
    cuidades_dos, verify_integrity=False)


print(cuidades_uno.max())
print(pd.Series.max(cuidades_uno))
print(np.max(cuidades_uno))

print(cuidades_uno.min())
print(pd.Series.min(cuidades_uno))
print(np.min(cuidades_uno))

print(cuidades_uno.mean())
print(cuidades_uno.median())
print(np.average(cuidades_uno))

print(cuidades_uno.head(2))
print(cuidades_uno.tail(2))

print(cuidades_uno.sort_values(
    ascending = False).tail(2))

print(cuidades_uno.sort_values().tail(2))


#0-1000 5%
#1001-5000 10%
#5001-20000 15%

def calcular(valor_serie):
    if(valor_serie <=1000):
        return valor_serie*1.05
    if(valor_serie >1000 and valor_serie <=5000):
        return valor_serie*1.10
    if(valor_serie >5000):
        return valor_serie*1.05

cuidad_calculada = cuidades_uno.map(calcular)

#if else
# cuano no se cumple condicion, aplica 

resultado = cuidades_uno.where(cuidades_uno< 1000,
                   cuidades_uno*1.05)

serires_numeros = pd.Series(['1.0','2',-3])

#integer, float, signed, unsigned
print(pd.to_numeric(serires_numeros, downcast='integer'))

series_numeros_err = pd.Series(['no tiene', '1.0','2',-3])

#ignore, coerce, raise(defualt)
#print(pd.to_numeric(series_numeros_err))
print(pd.to_numeric(series_numeros_err, errors='ignore'))
print(pd.to_numeric(series_numeros_err, errors='coerce'))


