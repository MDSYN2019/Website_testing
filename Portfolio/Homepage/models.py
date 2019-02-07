from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Mathematical Models
from django.forms import ModelForm

""" 
postgres models that will be used to represent the data on the homepage 
"""

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return self.choice_text 

class Content1Model(models.Model):
    Journal_title = models.CharField(max_length=500)
    slug = models.SlugField(
        max_length=31,
        unique = True,
        help_text = 'A label for the publication config'
    )
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    
# Django models map (roughly) to a database able, and provide a place to encapsulate
# business logic

class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    def __str__(self):
        return ' '.join([self.first_name,self.last_name,])
