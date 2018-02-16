#import numpy as np
import pandas as pd
import csv

#data = np.loadtxt('.txt')
data = pd.read_csv('3f42ef68-68d9-428b-be89-48da95336f3e.htseq.counts', sep=" ", header = None)
data.columns = ["a", "b"]

