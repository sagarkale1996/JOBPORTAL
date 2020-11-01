from django import forms

class StudentForm(forms.Form):
    Sid = forms.IntegerField()
    Sname = forms.CharField()
    Saddr = forms.CharField()
    Sscholarship = forms.FloatField()