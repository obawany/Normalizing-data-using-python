#import numpy as np
import pandas as pd

#data = np.loadtxt('.txt')
data = pd.read_csv('/Users/obawany/Downloads/GDC_Downloads/Adrenal Gland/female/0a0a8e16-d3af-4e98-802e-761966588e4f/3f42ef68-68d9-428b-be89-48da95336f3e.htseq.counts.txt', sep=" ", header = None)
data.columns = ["Gene", "count"]

