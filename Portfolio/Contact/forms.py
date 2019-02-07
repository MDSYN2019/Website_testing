from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime # use for checking dates

"""
Contact form for someone to add in their details to contact me later 
if need be

Generally speaking, GET and POST are the only HTTP methods to use when dealing with forms.

*** -- POST -- ***

Django login form is returned using the POST method, in which the browser bundles up the 
form data, encodes it for transmission, sends it to the server, and then receives back its 
response.

*** -- GET -- ***

GET, by contrast, bundles data into a string, and uses this to compose a 
URL. The URL contains the addresses where the data must be sent, as well 
as the data keys and values. 

--- Django's role in forms ---

Django handles three distinct parts of the work involved in forms:

- Preparing and restructuring data to make it ready for rendering 

- Creating HTML forms for the data

- Receiving and processing submitted forms and data from the client 

-------------------------------------------------------------------

=>  Django form and field validation

Form validation happens when the data is cleaned. If you want to customize this process, there are various places to make changes, each one 
serving a different purpose. 

Three types of cleaning methods are run during form processing. These
are normally executed when you call is_valid() method on a form.

"""

BIRTH_YEAR_CHOICES = [str(i) for i in range(1950, 2010)] # All years ranging from 1950 to 2010 - Should be enough.

FAVOURITE_COLORS_CHOICES = (

    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
)

from django import forms

""" The simplest form """
class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length = 100)
    
""" 
Contact class 

Consider a more useful than our minimal example above, which we could 
use a "contact me" functionality on a personal website

---------------------------------------------------------------------

Working with Django widgets

"""
#class ContactForm(forms.Form):
#    """
#    This time, we have four fields - subject, message, sender, cc_myself
#
#    Widgets - Each form field has a corresponding Widget.class, which in turm 
#    corresponds to an HTML form widget such as <input type = "text">

#    Whatever the data submitted with a form, once it has been successfully 
#    validated by calling is_valid(), the validated form data will be in the 
#    form.cleaned_data dictionary {"subject": subject" etc...}    

#    """
#    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))#

    # Validation method for birth_year
#    def check_birth_year():
#        if birth_year > datetime.date.today():
#            raise ValidationError(_('Invalid - Birthday is on a future date'))
        
#    favourite_colours = forms.MultipleChoiceField(
#        required = False,
#        widget = forms.CheckboxSelectMultiple,
#        choices = FAVOURITE_COLORS_CHOICES,
#    )
#    subject = forms.CharField(max_length = 100)
#    message = forms.CharField(widget = forms.Textarea)
#    sender = forms.EmailField()
#    cc_myself = forms.BooleanField(required=False)

class ContactForm(forms.Form):
    """
    Form for the contact page
    
    By default, a forms.CharField presents itself when rendered in a form 
    as a TextInput widget 

    For triage purposes, we also ask that they tell us what kind of message 
    they are sending: a request for support, general feedback or a correction.

    The way to achieve this is to use a ChoiceField. A ChoiceField defines keys 
    and values, where the keys are typically stored in the database and the values 
    are what the user is presented with. 

    
    To make interacting with a ChoiceField as simple as possible, 
    
    -------------------------------------------------------------


    Finally, we need to program a method on the form to send an email.

    """
    FEEDBACK = 'F'
    CORRECTION = 'C'
    SUPPORT = 'S'
    REASON_CHOICES = (
        (FEEDBACK, 'Feedback'),
        (CORRECTION, 'Correction'),
        (SUPPORT, 'Support',
    )
    reason = forms.ChoiceField(
        choices = REASON_CHOICES,
        initial = FEEDBACK)
    email = forms.EmailField(initial = 'sangyoung123@googlemail.com')
    text = forms.CharField(widget = forms.Textarea)

    def send_email(self):
        reason = self.cleaned_data.get('reason')
        reason_dict = dict(self.REASON_CHOICES)
        full_reason = reason_dict.get(reason)
        email = self.cleaned_data.get('email'),
        



class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text = "Enter a date between now and 4 weeks (default 3)")

    """
    Django provides numerous places where you can validate your data. The easiest way to validate a single field
    is to override the method clean_<fieldname>() for the field you want to check. So for example, we can validate 
    that entered renewal_date values are between now and 4 weeks by implementing clean_renewal_data() 
    """
    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        # Check if data is not in the past
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
        # Remember to always return the cleaned data

        return data
x    

