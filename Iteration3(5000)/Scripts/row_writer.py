import csv
import difflib
file = open("fname-lname-dob-similarities.csv","r+",encoding='utf-8',errors='ignore',newline='')
csv_reader = csv.reader(file,delimiter=',')
csv_writer = csv.writer(file)

for row in csv_reader:
	avg = ((int(row[4])+int(row[5])+int(row[6]))/3)
	csv_writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],avg])
file.close()

