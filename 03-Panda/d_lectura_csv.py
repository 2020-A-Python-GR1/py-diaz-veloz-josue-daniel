# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:09:35 2020

@author: josh_
"""

import pandas as pd
import os


path = "C:/Users/josh_/Documents/GitHub/py-diaz-veloz-josue-daniel/03-Panda/data/artwork.csv"

df1 = pd.read_csv(path, nrows=10)

columnas= ['id','artist','title','medium',
          'year','acquisitionYear','height',
          'width','units']

df2 = pd.read_csv(path, nrows=10,
                  usecols = columnas)

df3 = pd.read_csv(path,
                  usecols = columnas,
                  index_col='id')

path_guardado = "C:/Users/josh_/Documents/GitHub/py-diaz-veloz-josue-daniel/03-Panda/data/artwork.pickle"

df3.to_pickle(path_guardado)

df4 = pd.read_pickle(path_guardado)

