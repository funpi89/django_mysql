from django import forms
from employees.models import Employees

class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ['lastname', 'firstname', 'birthdate']