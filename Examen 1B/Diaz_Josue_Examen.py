# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 09:02:54 2020

@author: josue
"""


import numpy as np
import pandas as pd
from scipy import ndimage
from scipy import misc

#2) Crear un vector de ceros de tamaño 10

p_2 = np.zeros(10)

print('Pregunta 2 = ', p_2)

#3) Crear un vector de ceros de tamaño 10 y el de la posicion 5 sea igual a 1

p_3 = np.zeros(10)

p_3[5] = 1

print('Pregunta 3 = ', p_3)

#4) Cambiar el orden de un vector de 50 elementos, el de la posicion 1 es el de la 50 etc.

p_4 = np.arange(50)

p_4 = p_4[::-1]

print('Pregunta 4 = ', p_4)


#5) Crear una matriz de 3 x 3 con valores del cero al 8

p_5 = np.arange(9)

p_5 = p_5.reshape((3,3))

print('Pregunta 5 = ', p_5)

#6) Encontrar los indices que no sean cero en un arreglo

arreglo = [1,2,0,0,4,0]

arreglo = np.array(arreglo)

p_6 = np.where(arreglo != 0)[0]

print('Pregunta 6= Indices donde no es cero',p_6)


#7) Crear una matriz de identidad 3 x 3

p_7 = np.eye(3)

print('Pregunta 7 = ', p_7)


#8) Crear una matriz 3 x 3 x 3 con valores randomicos

p_8 = np.random.randint(27, size=27).reshape(3,3,3)

print('Pregunta 8 = ', p_8)


#9) Crear una matriz 10 x 10 y encontrar el mayor y el menor

p_9 = np.arange(100).reshape(10,10)

p_9_min = p_9.min()

p_9_max = p_9.max()

print('Pregunta 9 = minimo: ', p_9_min, ' maximo: ', p_9_max)


#10) Sacar los colores RGB unicos en una imagen (cuales rgb existen ej: 0, 0, 0 - 255,255,255 -> 2 colores)

mapache = misc.face()

p_10 = np.unique(mapache, axis=0)

count_RBG = len(p_10)

print('Pregunta 10 = ', p_10, '\n Colores unicos en total = ', count_RBG)

#11) ¿Como crear una serie de una lista, diccionario o arreglo?

mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

serie_list = pd.Series(mylist)
serie_arr = pd.Series(myarr)
serie_dict = pd.Series(mydict)

print('Pregunta 11 = lista: ', serie_list)
print('Pregunta 11 = arreglo: ', serie_arr)
print('Pregunta 11 = diccionario: ', serie_dict)

#12) ¿Como convertir el indice de una serie en una columna de un DataFrame?

ser = pd.Series(mydict)
# Transformar la serie en dataframe y hacer una columna indice

p_12=pd.DataFrame(ser).transpose().set_index('a')
print('Pregunta 12 = ',p_12)


#13) ¿Como combinar varias series para hacer un DataFrame?

ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

concat = pd.concat([ser1, ser2], axis = 1)

p_13 = pd.DataFrame(concat)

print('Pregunta 13 = ', p_13)

#14) ¿Como obtener los items que esten en una serie A y no en una serie B?

ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

p_14 = np.setdiff1d(ser1, ser2)

print('Pregunta 14 = ', p_14)

#15) ¿Como obtener los items que no son comunes en una serie A y serie B?

ser_a=ser1[-ser1.isin(ser2)]
ser_b=ser2[-ser2.isin(ser1)]

p_15=pd.concat([ser_a,ser_b])

print('Pregunta 15 = ', p_15)

#16) ¿Como obtener el numero de veces que se repite un valor en una serie?

ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))

p_16, counts = np.unique(ser, return_counts=True)

p_16 = dict(zip(p_16, counts))

print('Pregunta 16 =', p_16)

#17) ¿Como mantener los 2 valores mas repetidos de una serie, y a los demas valores cambiarles por 0 ?
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))

df=pd.DataFrame(ser,columns=['values'])
top_dos_valores=df['values'].value_counts().head(2)
indices=top_dos_valores.index
count=ser.map(top_dos_valores)
indices_cero=np.isnan(count)
count[indices_cero]=0
p_17 = pd.concat([ser, count], axis=1)
p_17[indices_cero]=0
del p_17[1]

print('Pregunta 17 = Serie: ', ser, '\n Mas_Repetidos = ', p_17)

#18) ¿Como transformar una serie de un arreglo de numpy a un DataFrame con un shape definido?
ser = pd.Series(np.random.randint(1, 10, 35))

p_18 = pd.DataFrame(ser.values.reshape(7,5))

print('Pregunta 18 =', p_18, ' ', type(p_18))


#19) ¿Obtener los valores de una serie conociendo la posicion por indice?
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
# a e i o u
p_19 = ser[pos]

print('Pregunta 19 =', p_19)


#20) ¿Como anadir series vertical u horizontalmente a un DataFrame?
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))

df_vertical = pd.concat([pd.DataFrame(),ser2], ignore_index = True)


df_horizontal = pd.DataFrame().append(ser2, ignore_index=True)

print('Problema 20 = \n Vertical:', df_vertical, '\nHorizontal:',df_horizontal)


#21)¿Obtener la media de una serie agrupada por otra serie?
#groupby tambien esta disponible en series.

frutas = pd.Series(np.random.choice(['manzana', 'banana', 'zanahoria'], 10))
pesos = pd.Series(np.linspace(1, 10, 10))
print(pesos.tolist())
print(frutas.tolist())
#> [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
#> ['banana', 'carrot', 'apple', 'carrot', 'carrot', 'apple', 'banana', 'carrot', 'apple', 'carrot']

# Los valores van a cambiar por ser random
# apple     6.0
# banana    4.0
# carrot    5.8
# dtype: float64


p_21 = pd.concat([frutas, pesos], axis = 1)

p_21 = p_21.groupby(p_21[0], as_index=False)[1].mean()

print('Pregunta 21 = ', p_21)

#22)¿Como importar solo columnas especificas de un archivo csv?
url = 'https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv'

p_22=pd.read_csv(url,usecols = ['crim','zn','indus','tax','medv'])

print('Pregunta 22 = ', p_22)




