import sqlite3
import csv
from pathlib import Path


path_name=str(Path.cwd())

con = sqlite3.connect('expenseDB.db')
outfile = open('20230310_mydump.csv', 'w')
outcsv = csv.writer(outfile)

cursor = con.execute('select * from IncomeExpenses')

# dump column titles (optional)
outcsv.writerow(x[0] for x in cursor.description)
# dump rows
outcsv.writerows(cursor.fetchall())

outfile.close()