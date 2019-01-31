from django import forms

# Uploading file

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length = 50)
    file = forms.FileField()

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text = "Enter a date between now and 4 weeks")
    
