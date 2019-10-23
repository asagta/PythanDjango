'''
Created on Oct 22, 2019

@author: as404g
'''
from django import forms  
from HtmlViews.models import Employee  
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__" 