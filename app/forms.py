from django import forms
from app.models import *

class StudentForm(forms.ModelForm):
    class Meta():
        model=Student
        fields='__all__'
    

    Email=forms.EmailField()
    ReenterEmail=forms.EmailField()
    botcatcher=forms.CharField(max_length=10,required=False,widget=forms.HiddenInput)

    def clean(self):
        E=self.cleaned_data['Email']
        RE=self.cleaned_data['ReenterEmail']
        if E!=RE:
            raise forms.ValidationError('Email not match')


    def clean_botcatcher(self):
        b=self.cleaned_data['botcatcher']
        if len(b)>0:
            raise forms.ValidationError('Bot')


    
    def clean(self):
        m=self.cleaned_data['Smobile']
        AM=self.cleaned_data['Alternative_mobile']
        if m==AM:
            raise forms.ValidationError('Not be same')
        




        
