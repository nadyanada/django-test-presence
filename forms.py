from django import forms
from .models import AttendanceShortTerm

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = AttendanceShortTerm
        fields = ['name', 'phone_number']