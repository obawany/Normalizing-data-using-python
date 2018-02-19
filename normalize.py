import numpy as np
import pandas as pd
import csv
import logging
import os
import io
#from os import listdir
#from os.path import isfile, join
import sys

# #data = np.loadtxt('.txt')

# #let me set a path for the file 
path = '/Users/obawany/Downloads/GDC_Downloads/'
downloads = os.listdir(path)

for cancertype in downloads:
	male_female = os.listdir(path + cancertype)
	print(cancertype)
	for male_female in cancertype:
		print(male_female)
# #data = pd.read_csv("/Users/obawany/Desktop/GItHub Repositories/Normalizing-data-using-python/3f42ef68-68d9-428b-be89-48da95336f3e.htseq.counts.txt", sep=" ", header = None)
# #data.columns = ["a"]
# #values = data.pop('a')

# data = np.loadtxt("/Users/obawany/Desktop/GItHub Repositories/Normalizing-data-using-python/3f42ef68-68d9-428b-be89-48da95336f3e.htseq.counts.txt", usecols=(1,))
# #data = data/data[0]

# data1 = np.loadtxt("/Users/obawany/Desktop/GItHub Repositories/Normalizing-data-using-python/test.txt", usecols=(1,))
# #data.sum(axis=0)

# #df = pd.DataFrame((9), reshape(3,3))

# #Count_row=data.shape[0]
# #logging.info(Count_row)
# #logging.info(data.index)
# #write(Count_row)
# #len(df.index)

# #len(data.index)

# datasum1 = 0

# for i in range(0, len(data1) ):
# 	datasum1 = datasum1 + data1[i]

# for i in range(0, len(data1)):
# 	data1[i] = data1[i]/datasum1

# #datatowrite = np.genfromtxt(fname='/Users/obawany/Desktop/GItHub Repositories/Normalizing-data-using-python/test.txt')
# #s=datatowrite[:,1]
# ''''
# with open("test.csv", "wa") as f:
# 	f.write ("Letter\tNumber\tNormalized\n")
# 	for k,v,x in 
# '''
# file = open("/Users/obawany/Desktop/GItHub Repositories/Normalizing-data-using-python/test.txt", "r").readline
# output = ["%s \t %s \t %s" % (item.strip(), 1) for item in file]
# f = open("/Users/obawany/Desktop/GItHub Repositories/Normalizing-data-using-python/test.txt", "w")
# f.write("\n".join(output))
# f.close()
# #int n = data.length()
# #data1 = data1/data1[1]
# np.savetxt('testnew.txt', data1)

# datasum = 0


# for i in range(1, len(data) ):
# 	datasum = datasum + data[i]

# for i in range(1, len(data)):
# 	data[i] = data[i]/datasum
#for n in sys.argv

with open ('/Users/obawany/Desktop/GItHub Repositories/Normalizing-data-using-python//3f42ef68-68d9-428b-be89-48da95336f3e.htseq.counts.normalized.txt', 'w') as g, open('/Users/obawany/Desktop/GItHub Repositories/Normalizing-data-using-python//3f42ef68-68d9-428b-be89-48da95336f3e.htseq.counts.txt') as f:

	#to sum all the values of that file/experiment 	
	sumofvalues = 0
	numberofvalues = 0

	#split line by line for each gene/miRNA
	content = f.read().splitlines()

	#this for loop is for getting the sum mainly 
	for line in content:
		contentlinebyline = line.split(" ")
		#print (line)
		#if statement to ignore lines with extra data and headings
		if (line[0] == 'E'):
			values = line.split("\t")[1]
			#print(values)
			value = int(values)
#			print(value)
#			print(line)
			sumofvalues = sumofvalues + value
			numberofvalues = numberofvalues + 1
			#print(contentlinebyline)
			#print(contentlinebyline[1])
			#values = contentlinebyline.split("\t")[1]
			#print(values)

			# line['A'], line['B'] = line['AB'].str.split(' ', 1).str
			# print(lin)
#	print(sumofvalues)

	#this sum is for normalizing, concatenating and creating new file
	for line in content:
		contentlinebyline = line.split(" ")
		#if statement to ignore lines with extra data and headings
		if (line[0] == 'E'):
			values = line.split("\t")[1]
			value = int(values)
		#	print(value)
			normalizedvalue = value/sumofvalues
			line = line + "\t" + str(normalizedvalue)
			g.write(line + ("\n"))
		#print(normalizedvalue)
		print(line)


#data = data/data[600]
#np.savetxt('new.txt', data)


