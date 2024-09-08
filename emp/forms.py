from django import forms

from emp.models import Employee
from django.forms import Select, modelform_factory, modelformset_factory, TextInput

#Create Form class
class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = '__all__'

        widgets = {
            'birthDate': forms.widgets.DateInput(attrs={'type': 'date'}),
            'hireDate': forms.widgets.DateInput(attrs={'type': 'date'}),
        }

#PartTimeEmployeeForm = modelform_factory(PartTimeEmployee, fields=['firstName', 'lastName', 'titleName'])
