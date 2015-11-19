import csv
from collections import Counter
import itertool

#User will identify the input file location, variable to be analyzed and output file location
inputfile = raw_input("Please identify your file directory: ")
fileVariable = raw_input("Please enter your variable of interest: ")
outputfile = raw_input("Please identify where you want this file to be saved: ")
articles =['a', 'an', 'the', 'is', 'are', 'were', 'was']
def main():
	
	#opens file
	with open(inputfile, 'r') as my_file:         
		data = csv.DictReader(my_file, delimiter=',')
		combi = []
		
		#for each row, create a two word combination and append to combi
		for row in data:
			for i in row:
				itertool.ifilter(lambda x:if i in articles, row[fileVariable])
			for w in itertools.permutations(row[fileVariable].split(), 2):
				combi.append(w)
		nodes = Counter(combi)
	
	#creates output file
	with open(outputfile, 'w') as csv_file:
		fieldnames = ['Source','Target', 'Type', 'ID', 'Label', 'Weight']
		data = csv.DictWriter(csv_file, fieldnames = fieldnames)
		data.writeheader()
		types = 'Undirected'
		for combination,count in nodes.most_common():
			for i in range(1, len(nodes)):
				data.writerow({'Source':combination[0], \
				'Target':combination[1], 'Type': 'Undirected' , \
				'ID' :i,'Label':combination, 'Weight':count})
main_py()
