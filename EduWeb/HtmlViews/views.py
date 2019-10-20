'''
Created on 16 Oct, 2019

@author: as404g
'''
from django.shortcuts import render

def htmlhello(request):
   return render(request, "welcome.html", {})