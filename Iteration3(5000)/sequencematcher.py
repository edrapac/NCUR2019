import csv
import difflib
file = open("firstname-passwords(5000).csv","r+",encoding='utf-8',errors='ignore')
file2 = open("training-passwords_similarities.csv","w",encoding='utf-8',errors='ignore',newline='')
csv_reader = csv.reader(file,delimiter=',')
csv_writer = csv.writer(file2)

for row in csv_reader:
	seq = difflib.SequenceMatcher(None,row[0],row[1])
	
	d = seq.ratio()*100
	csv_writer.writerow([row[0],row[1],d])
file.close()
file2.close()