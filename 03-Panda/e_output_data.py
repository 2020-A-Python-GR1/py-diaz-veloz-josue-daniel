# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 09:43:48 2020

@author: josh_
"""

import numpy as np
import pandas as pd
import os
import sqlite3
import xlsxwriter

path_guardado = "C:/Users/josh_/Documents/GitHub/py-diaz-veloz-josue-daniel/03-Panda/data/artwork.pickle"

df = pd.read_pickle(path_guardado)

sub_df = df.iloc[49980:50519,:].copy() 


path_excel = "C:/Users/josh_/Documents/GitHub/py-diaz-veloz-josue-daniel/03-Panda/data/artwork_data.xlsx"
path_excel_indice = "C:/Users/josh_/Documents/GitHub/py-diaz-veloz-josue-daniel/03-Panda/data/artwork_data_index.xlsx"
path_excel_columnas = "C:/Users/josh_/Documents/GitHub/py-diaz-veloz-josue-daniel/03-Panda/data/artwork_data_columnas.xlsx"


sub_df.to_excel(path_excel)

#Sin inidices
sub_df.to_excel(path_excel_indice, index = False)

columnas = ['artist','title','year']

sub_df.to_excel(path_excel_columnas, columns=columnas)


#multiples hojas
path_excel_mt = "C:/Users/josh_/Documents/GitHub/py-diaz-veloz-josue-daniel/03-Panda/data/artwork_data_mt.xlsx"

writer = pd.ExcelWriter(path_excel_mt, engine='xlsxwriter')

sub_df.to_excel(writer, sheet_name = 'Primera')
sub_df.to_excel(writer, sheet_name = 'Segunda')
sub_df.to_excel(writer, sheet_name = 'Tercera')
writer.save()

#Formato Condicional 

num_artistas = sub_df['artist'].value_counts()

print(type(num_artistas))
print(num_artistas)

path_excel_colores = "C:/Users/josh_/Documents/GitHub/py-diaz-veloz-josue-daniel/03-Panda/data/artwork_data_colores.xlsx"

writer = pd.ExcelWriter(path_excel_colores, engine='xlsxwriter')

#Series
num_artistas.to_excel(writer, sheet_name = 'Artistas')

#Seleccionando la hoja
hoja_artistas = writer.sheets['Artistas']

#define el rango que se tiene
rango_celdas = 'B2:B{}'.format(len(num_artistas.index)+1)

#formato 

formato_artista = {
    "type": "2_color_scale",
    "min_value": "10",
    "min_type": "percentile",
    "max_value": "99",
    "max_type": "percentile"
    }

hoja_artistas.conditional_format(rango_celdas,formato_artista)

writer.save()

path_bdd = "C:/Users/josh_/Documents/GitHub/py-diaz-veloz-josue-daniel/03-Panda/bdd_artist.bdd"

path_json = "C:/Users/josh_/Documents/GitHub/py-diaz-veloz-josue-daniel/03-Panda/artistas.json"

path_json_tabla = "C:/Users/josh_/Documents/GitHub/py-diaz-veloz-josue-daniel/03-Panda/artistas_tabla.json"
########## SQL ##########

with sqlite3.connect(path_bdd) as conexion:
    sub_df.to_sql('py_artistas', conexion)
    

## with mysql.connect('mysql://user:password@ip:puerto/nombre_base')
##      df5.to_sql('tabla_mysql', conexion)
    
########## JSON ##########

sub_df.to_json(path_json)

sub_df.to_json(path_json_tabla, orient = 'table')















