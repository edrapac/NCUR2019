import csv
file = open("training.csv","r",encoding='utf-8',errors='ignore') # this file is in the format username, firstname, lastname, gender,email,city,state,password
file2 = open("training2.csv","w",encoding='utf-8',errors='ignore') # this file is in the format username, firstname, lastname, gender,email,city,state,password

passfile = open("badpass.txt","r")
csv_reader = csv.reader(file,delimiter=',') #puts each row into a list we can index that by something like csv_reader[0] to get the first element of a row
csv_writer = csv.writer(file2)
passes = []
entries = {}
for line in passfile:
	
	line = line.strip("\n")
	passes.append(line)

for row in csv_reader:
	
		
	if row[1] in passes:
			
		entries[row[1]] = 'bad'
		
	else:
			
		entries[row[1]] = 'good'
for keys,values in entries.items():
	
	print(keys,values)

file.close()
file2.close()