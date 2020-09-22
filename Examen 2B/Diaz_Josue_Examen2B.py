# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 07:05:57 2020

@author: Josue
"""
import numpy as np
import pandas as pd
import random
import string

#Pregunta 1

df1 = pd.DataFrame(np.random.randint(0,100,size=(10, 6)), columns=list('ABCDEF'))

df1_primeros = df1.head(5)

df1_ultimos = df1.tail(5)

print('Pregunta 1 = \n', df1)
print("primeros 5")
print(df1_primeros)
print("ultimos 5")
print(df1_ultimos)

#Pregunta 2
arreglo2 = np.random.uniform(0,100,size=(6, 4))

columnas = pd.date_range(start='09/22/2020', end='09/27/2020')

df2 = pd.DataFrame(arreglo2, columns=list('ABCD'), index=columnas)

print('Pregunta 2 = \n', df2)

#Pregunta 4
df4 = pd.DataFrame(np.random.randint(0,100,size=(10, 6)), columns=list('ABCDEF'))

columnas_4 = df4.columns

valores_4 = df4.values
print('Pregunta 4 = \n', df4)
print('columnas = ', columnas_4)
print('valores = ', valores_4)

#Pregunta 5

df5 = pd.DataFrame(np.random.randint(0,100,size=(10, 6)), columns=list('ABCDEF'))

estadisticas = df5.describe()

print('Pregunta 5 = \n', df5)

print('Estadisticas = \n', estadisticas)

#Pregunta 6

df6 = pd.DataFrame(np.random.randint(0,100,size=(10, 6)), columns=list('ABCDEF'))

transpuesta = df6.transpose()

print('Pregunta 6 = \n', df6)

print('Transpuesta = \n', transpuesta)

#Pregunta 7

df7 = pd.DataFrame(np.random.randint(0,100,size=(10, 6)), columns=list('ABCDEF'))

print('Pregunta 7 = \n', df7)

df7_A_asc = df7.sort_values('A')
df7_A_desc = df7.sort_values('A', ascending=False)
print('Columna A ascendente = \n', df7_A_asc)
print('Columna A descendente = \n', df7_A_desc)
df7_B_asc = df7.sort_values('B')
df7_B_desc = df7.sort_values('B', ascending=False)
print('Columna B ascendente = \n', df7_B_asc)
print('Columna B descendente = \n', df7_B_desc)
df7_C_asc = df7.sort_values('C')
df7_C_desc = df7.sort_values('C', ascending=False)
print('Columna C ascendente = \n', df7_C_asc)
print('Columna C descendente = \n', df7_C_desc)
df7_D_asc = df7.sort_values('D')
df7_D_desc = df7.sort_values('D', ascending=False)
print('Columna D ascendente = \n', df7_D_asc)
print('Columna D descendente = \n', df7_D_desc)
df7_E_asc = df7.sort_values('E')
df7_E_desc = df7.sort_values('E', ascending=False)
print('Columna E ascendente = \n', df7_E_asc)
print('Columna E descendente = \n', df7_E_desc)
df7_F_asc = df7.sort_values('F')
df7_F_desc = df7.sort_values('F', ascending=False)
print('Columna F ascendente = \n', df7_F_asc)
print('Columna F descendente = \n', df7_F_desc)

#Pregunta 8

df8 = pd.DataFrame(np.random.randint(1,10,size=(10, 6)), columns=list('ABCDEF'))

df8_filtered = df8.where(df8 > 7)

print('Pregunta 8 = \n', df8)
print('Valores mayores a 7 = \n', df8_filtered)

#Pregunta 9

df9 = pd.DataFrame(np.random.randint(1,10,size=(10, 6)), columns=list('ABCDEF'))

df9 = df9.where(df9 < 5)

df9 = df9.fillna(0)

print('Pregunta 9 = \n', df9)

#Pregunta 10

df10 = pd.DataFrame(np.random.randint(1,10,size=(10, 6)), columns=list('ABCDEF'))

df10_mean = df10.mean().mean()

df10_median = df10.median().median()

print('Pregunta 10 = \n', df10)

print('media =', df10_mean)
print('mediana =', df10_median)

#Pregunta 11

df11 = pd.DataFrame(np.random.randint(1,10,size=(10, 6)), columns=list('ABCDEF'))

df11_2 = pd.DataFrame(np.random.randint(1,10,size=(10, 6)), columns=list('ABCDEF'))

df11 = df11.append(df11_2)

print('Pregunta 11 = \n', df11)

#Pregunta 12

lista_string = []

for i in range(60):
    lista_string.append(''.join(random.choices(string.ascii_uppercase, k=5)))

df12 = pd.DataFrame(np.array(lista_string).reshape(10,6), columns=list('ABCDEF'))

df12_final = pd.DataFrame()

df12_final['A'] = df12['A'] + df12['B'] 

df12_final['B'] = df12['C'] + df12['D']

df12_final['C'] = df12['E'] + df12['F']

print('Pregunta 12 = \n', df12)
print('DataFrame Final = \n', df12_final)

#Pregunta 13

df13 = pd.DataFrame(np.random.randint(1,10,size=(10, 6)), columns=list('ABCDEF'))

df13_A = df13['A'].value_counts()
df13_B = df13['B'].value_counts()
df13_C = df13['C'].value_counts()
df13_D = df13['D'].value_counts()
df13_E = df13['E'].value_counts()
df13_F = df13['F'].value_counts()

print('Pregunta 13 = \n', df13)
print('Frecuencia columna A = \n', df13_A)
print('Frecuencia columna B = \n', df13_B)
print('Frecuencia columna C = \n', df13_C)
print('Frecuencia columna D = \n', df13_D)
print('Frecuencia columna E = \n', df13_E)
print('Frecuencia columna F = \n', df13_F)

#Pregunta 14

df14 = pd.DataFrame(np.random.randint(1,10,size=(10, 3)), columns=list('ABC'))

df14['Calculo (A*B)/C'] = (df14['A'] * df14['B']) / df14['C']

print('Pregunta 14 = \n', df14)
