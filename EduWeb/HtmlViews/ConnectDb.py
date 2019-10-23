'''
Created on Oct 23, 2019

@author: as404g
'''
import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")
cursor = conn.execute("SELECT sno, fld_data from web_data")
for row in cursor:
 print("ID = ",row[0])
 print("NAME = "+ row[1])
print ("Operation done successfully")


conn.close()