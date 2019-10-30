'''
Created on 16 Oct, 2019

@author: as404g
'''
import sqlite3
import os
from django.shortcuts import render

def getUsers(request):
        path = os.path.join(os.path.dirname(__file__), 'test.db')
        print(path)
        conn = sqlite3.connect(path)
        cursor = conn.execute("SELECT sno, fld_data from web_data")
        name_list = []
        for x in cursor:
          name_list.append(x[1])            
        return name_list

def htmlhello(request):
   users=getUsers(request) 
   return render(request, "welcome.html", {'users': users})def htmlSel(request):
   return render(request, "sel.html", {})def htmlSelSetup(request):
   return render(request, "sel_setup.html", {})