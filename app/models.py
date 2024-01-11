from django.db import models
from django.core import validators
from django import forms

# Create your models here.
def validate_for_Sname(data):
    if data.lower()[0]=='a':
        raise forms.ValidationError('Cannot start with a')
def validate_for_Sage(data):
    if data<=18:
        raise forms.ValidationError('18 Above')


class Student(models.Model):
    Sname=models.CharField(max_length=100,validators=[validate_for_Sname])
    Sage=models.IntegerField(validators=[validate_for_Sage])
    Smobile=models.CharField(max_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    Alternative_mobile=models.CharField(max_length=10,null=True,validators=[validators.RegexValidator('[6-9]\d{9}')])


    def __str__(self) -> str:
        return self.Sname



    


