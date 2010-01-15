# -*- coding: utf-8 -*-

from django import forms
from facts.models import Fact

class FactForm(forms.ModelForm):
    class Meta:
        model = Fact
        fields = ('text',) 
