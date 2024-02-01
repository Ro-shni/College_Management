from django import forms 
from .models import certi
from .models import orders

class OrdersForm(forms.ModelForm):
    class Meta:
        model = orders
        fields = ['certi_name', 'drivelink', 'certi_no', 'start_date', 'end_date', 'credits']

class certiform(forms.ModelForm):
    class Meta:
        model = certi
        fields = ['type','credits','name','score','level','adnum','image']
        
