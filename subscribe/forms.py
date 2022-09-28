from dataclasses import field
import email
from enum import unique
from traceback import format_exception
from django import forms
from django.utils.translation import gettext_lazy as _
from subscribe.models import Subscribe

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        #fields = ['first_name', 'last_name', 'email']
        fields="__all__"
        labels = {"first_name":_('Enter First Name')}
        error_messages={'first_name':{'required':_('First name required')}}
        help_text = {"first_name":_('100 char')}
        
# def validate_comma(value):
#     if ',' in value:
#         raise forms.ValidationError('Invalid first name')
#     return value

# class SubscribeForm(forms.Form):
#     first_name=forms.CharField(max_length=100, required=False, label='First Name', help_text='Characters only')
#     last_name=forms.CharField(max_length=100, disabled=False, validators=[validate_comma])
#     email=forms.EmailField(max_length=100, validators=[validate_comma])
    
    # def clean_first_name(self):
    #     data =self.cleaned_data['first_name']
    #     if "," in data:
    #         raise forms.ValidationError('Invalid first name')
    #     return data