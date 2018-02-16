import numpy as np
import pandas as pd
import csv
import logging
import os


#data = np.loadtxt('.txt')

#let me set a path for the file 
path = '/Users/obawany/Downloads/GDC_Downloads/Adrenal Gland/female/0a0a8e16-d3af-4e98-802e-761966588e4f/'

#data = pd.read_csv("/Users/obawany/Desktop/GItHub Repositories/Normalizing-data-using-python/3f42ef68-68d9-428b-be89-48da95336f3e.htseq.counts.txt", sep=" ", header = None)
#data.columns = ["a"]
#values = data.pop('a')

#data = np.loadtxt("/Users/obawany/Desktop/GItHub Repositories/Normalizing-data-using-python/3f42ef68-68d9-428b-be89-48da95336f3e.htseq.counts.txt", usecols=(1,))
#data = data/data[0]

data = np.loadtxt("/Users/obawany/Desktop/GItHub Repositories/Normalizing-data-using-python/test.txt", usecols=(1,))
#data.sum(axis=0)

#df = pd.DataFrame((9), reshape(3,3))

Count_row=data.shape[0]
logging.info(Count_row)
logging.info(data.index)
#write(Count_row)
#len(df.index)

#len(data.index)

#int n = data.length()

data = data/data[4]
np.savetxt('new.txt', data)