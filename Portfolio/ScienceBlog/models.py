from django.db import models
from django import forms 

"""
SQL models to store data for the blogpage/other online articles
"""
class Science(models.Model):#inherit from models.model 
    topic = models.CharField(max_length=200) # what type of data?  we also need to characterise maxlengths
    lab_involvment = models.CharField(max_length=200)
    popularity = models.CharField(max_length=100)
    picture = models.CharField(max_length=10000) # max_length has to be long as we are dealing with other websites
    def __str__(self): # "A string representation of the object" 
        """Define the definition of the object"""
        return self.topic + '-' + self.popularity # Now when you call the object, it will simply print out it's topic in question and it's general popularity. 
    
class subfield(models.Model): # How to associate the above class with this class?
    # topic needs to be related to computational chemistry
    subtopic = models.ForeignKey(Science, on_delete = models.CASCADE) # when you need to delete the album, models.CASCADE allows the computer to delete the songs too automatically
    maths_heavy = models.CharField(max_length = 10)
    time_to_be_competent = models.CharField(max_length = 250)

    def __str__(self):
        """Define the subfield of science - i.e. whether it is chemistry, physics or mathematics"""
        return self.subtopic

# Reference to other papers

class linktopapers(models.Model):
    title = models.CharField(max_length=200) # Title of the paper 
    authorshortcut = models.CharField(max_length=100) # author of the paper 
    date = models.DateField()
    webpage = models.CharField(max_length=200)

## Upload files model

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class Target(models.Model):
    """A Django model to define a given protein target"""
    UniProt = models.CharField(max_length=20,unique=True)
    InitDate = models.DateTimeField(auto_now_add=True)
    Title = models.CharField(max_length=10)
