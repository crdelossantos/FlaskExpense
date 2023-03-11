import sqlite3
import csv
#from pathlib import Path


#path_name=str(Path.cwd())

con = sqlite3.connect('expenseDB.db')
cursor = con.cursor()
infile = open('mydumpin.csv')

incsv = csv.reader(infile)

insert_records = "INSERT OR REPLACE INTO IncomeExpenses (id,type,category,date,amount) VALUES(?, ?, ?, ?, ?)"

#cursor = con.execute('select * from IncomeExpenses')
# Importing the contents of the file
# into our person table
cursor.executemany(insert_records, incsv)

con.commit()
con.close()
# dump column titles (optional)
#outcsv.writerow(x[0] for x in cursor.description)
# dump rows
#outcsv.writerows(cursor.fetchall())

infile.close()