import csv
file = open("training2(use this one).csv","r",encoding='utf-8',errors='ignore')
csv_reader = csv.reader(file,delimiter=',')

def ngrams(string, n=3):
	ngrams = zip(*[string[i:] for i in range(n)])
	return [''.join(ngram) for ngram in ngrams]

for row in csv_reader:
	print(ngrams(row[0]))


