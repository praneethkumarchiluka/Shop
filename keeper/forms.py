# -*- coding: utf-8 -*-
from django import forms
from .models import items



class Itemsform(forms.ModelForm):
    class Meta:
        model=items
        fields=['itemname','quantity','rate']
