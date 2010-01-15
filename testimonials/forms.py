# -*- coding: utf-8 -*-

from django import forms
from testimonials.models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ('title', 'text', 'author',) 
