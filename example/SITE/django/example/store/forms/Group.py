from django import forms
from .. import models

class Group(forms.ModelForm):
    class Meta:
        model = models.Group
        exclude = []
        # указываются поля которые не будут редактироваться
        # можно еще указать список fields, в котором описывается что выводить в форму

