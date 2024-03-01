from django.db import models
from django import forms
from django.forms import ModelForm


class Rgann(models.Model):
    string1 = models.CharField(max_length=100, null=True, blank=True, db_comment='string1 in database')
    datefrom = models.DateField(null=True, blank=True)
    rgapattern = models.CharField(max_length=400, null=True, blank=True)
    rgatext = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        managed = True


class RgannModelForm(forms.ModelForm):
    rgatext = forms.CharField(required=False, widget=forms.Textarea)
    body = forms.CharField(required=False, widget=forms.widgets.Textarea(attrs={'placeholder':'value of placeholder'}) )
    class Meta:
        model = Rgann
        fields = ['rgatext', 'rgapattern' ]    # '__all__'

class RgannForm(forms.Form):
    rginfo = forms.CharField(max_length=40, label='Information')
    rgapattern = forms.CharField(max_length=40, label='Pattern')
    rgatext = forms.CharField(max_length=40, label='Text for regex')


class StudentNoModel:
    first_name: str
    last_name: str
    email: str

    def isempty(self):
        return self.first_name=='' & self.last_name=='' & self.email==''
    def secinit(self, fname, lname, email):
        self.first_name = fname
        self.last_name = lname
        self.email = email


class Student(models.Model):
    first_name = models.CharField(max_length=200, verbose_name="Person's First Name ")
    last_name = models.CharField(max_length=200, verbose_name="Last Name")
    email = models.EmailField(unique=True, verbose_name="Email")
    address = models.CharField(max_length=200, verbose_name="Address")
    index_no = models.CharField(max_length=20, verbose_name="Index Number")
    mother_name = models.CharField(max_length=200, verbose_name="Mother Name")
    father_name = models.CharField(max_length=200, verbose_name="Father Name")

    def secinit(self, fname, lname, email):
        self.first_name = fname
        self.last_name = lname
        self.email = email

    class Meta:
        managed = False
