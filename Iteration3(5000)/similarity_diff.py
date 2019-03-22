import csv
import difflib
file = open("fname-lname-dob(5001-10000).csv","r+",encoding='utf-8',errors='ignore',newline='')
file2 = open("test_fname-lname-dob(5001-10000).csv","w",encoding='utf-8',errors='ignore',newline='')
csv_reader = csv.reader(file,delimiter=',')
csv_writer = csv.writer(file2)

for row in csv_reader:
	fname_seq = difflib.SequenceMatcher(None,row[0],row[3])
	lname_seq = difflib.SequenceMatcher(None,row[1],row[3])
	dob_seq = difflib.SequenceMatcher(None,row[2],row[3])
	
	f = fname_seq.ratio()*100
	l = lname_seq.ratio()*100
	d = dob_seq.ratio()*100
	csv_writer.writerow([row[0],row[1],row[2],row[3],f,l,d])
file.close()
file2.close()

