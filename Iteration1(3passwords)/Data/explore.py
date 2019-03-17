import csv

file = open("users.csv","r",encoding='utf-8',errors='ignore') # this file is in the format username, firstname, lastname, gender,email,city,state,password
newfile = open("all_passwords.txt","w")
csv_reader = csv.reader(file,delimiter='\n') #puts each row into a list we can index that by something like csv_reader[0] to get the first element of a row

for row in csv_reader:
	try:
		newfile.write(row[0]+'\n')
	except Exception as e:
		pass
	



file.close()
newfile.close()