from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime 

"""
What are model forms and why do we need them?

- Django makes the HTML forms for you
- Form validation is done by django

"""

class NameForm(forms.Form):
    """
    This defines a Form class with a single field your_name. We've applied    
    """
    your_name = forms.CharField(label="Your name", max_length=100)
    
""" 
Mozilla bookform
"""

class DeadlineForm(forms.Form):
    deadline_date = forms.DateField(help_text = "Enter a date between now and 4 weeks")

    def clean_deadline_date(self):
        data = self.cleaned_data['deadline_date']

        # Check if the date is not in the past
        if data <= datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))
        
        return data
    
# Uploading file

"""
When Django handles a file upload , the file data ends up placed in request.FILES. 
This document explains how files are stored on disk and in memory, and how to customize 
the default behaviour 
"""

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length = 50)
    file = forms.FileField()
    
class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")    
    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        
        # Check date is not in past.
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))
        
        # Check date is in range librarian allowed to change (+4 weeks).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
        
        # Remember to always return the cleaned data.
        return data

"""

When django handles a file upload, the file data ends up placed in request.FILES. This document explains how files are stored 
on disk and in memory


"""
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField() # a view handling this form will receive the file data in request.FILES which is a dictionary
                             # containing a key for each filefield

                             
    
