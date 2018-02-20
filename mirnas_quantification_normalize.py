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
cancertypes = os.listdir(path)

for cancertype in cancertypes:
	#male_female = os.listdir(path + cancertype)
	#print(cancertype)
	if cancertype != '.DS_Store':
		path_inside_canner = path + cancertype
		#print(path_inside_canner)
		male_female = os.listdir(path_inside_canner)
#		print(male_female) 
#		print(male_female)
		for male_female_dir in male_female:
			#print(male_female)
			#print(male_female_dir)
			if male_female_dir != '.DS_Store':
				path_inside_gender = path_inside_canner + "/" + male_female_dir
#				print(path_inside_gender)
				experiments_within = os.listdir(path_inside_gender)
#				print(experiments_within)
				for experiment in experiments_within:
					if experiment != '.DS_Store':
						experiment_path = path_inside_gender + "/" + experiment
						#print(experiment_path)
						if not experiment_path.endswith('.txt'):
							files_in_exp = os.listdir(experiment_path)
	#						print(files_in_exp)
							#print(files_in_exp[0])
							file_name = files_in_exp[0]
							#print(file_name)
							if file_name.endswith('.quantification.txt'):
								file_path = experiment_path + "/" + file_name
							#	print(file_path)
				# for gender_folder in path_to_male_female:
				# 	if gender_folder != '.DS_Store':
				# 		experiments_path = path_inside_canner + "/" + gender_folder
				# 		experiments = os.listdir(experiments_path)
				# 		#print(experiments)

				#print(check)
		# for male_female in cancertype:
		# 	print(male_female)
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
	# for n in sys.argv

								with open (experiment_path + file_name + '.normalized.txt', 'w') as g, open(file_path, 'r') as f:

									#to sum all the values of that file/experiment 	
									sumofvalues = 0
									numberofvalues = 0

									#split line by line for each gene/miRNA
									content = f.read().splitlines()

									#this for loop is for getting the sum mainly 
									for line in content:
										#print(file_path)
										contentlinebyline = line.split(" ")
										#print (line)
										#print(line)
										#if statement to ignore lines with extra data and headings
										if (line[0] == 'h'):
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
										if (line[0] == 'h'):
											values = line.split("\t")[1]
											value = int(values)
										#	print(line)
										#	print(value)
											normalizedvalue = value/sumofvalues
											line = line + "\t" + str(normalizedvalue)
											g.write(line + ("\n"))
										#	print(line)
								f.close()
								g.close()

									#	print(normalizedvalue)
									#	print(line)


								#data = data/data[600]
								#np.savetxt('new.txt', data)