import os # ...
import csv # involved in loading a csv file
import datetime # ...

from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse # Standard website response you want
from django.http import HttpResponseNotFound
from django.conf import settings
from django.http import HttpResponseRedirect

# from django.http import Http404 # 404 error library
# import database from .models

from .models import Science 
from .models import linktopapers

# HTML & CSS loader

from django.template import loader
from django.contrib.staticfiles.storage import staticfiles_storage
# Importing forms from forms.py

from .forms import NameForm 
from .forms import UploadFileForm

# Part of the file upload tutorial

"""
Each views here defines variables that can connect to the models.py databases, and 
using django code {% %} in the html template, one can refer to these array databases
"""



def Chemiinformatics1(request):
    """Reference to the ieee.html """
    template = loader.get_template('ScienceBlog/chemi1.html')
    context = {}
    return HttpResponse(template.render(context, request))

def NP_article(request):
    """Reference to the ieee.html """
    template = loader.get_template('ScienceBlog/phile_phobe.html')
    context = {}
    return HttpResponse(template.render(context, request))

def lipid(request):
    """Reference to the ieee.html """
    template = loader.get_template('ScienceBlog/lipid.html')
    context = {}
    return HttpResponse(template.render(context, request))

def replacement(request):
    """Reference to the ieee.html """
    template = loader.get_template('ScienceBlog/replacement.html')
    context = {}
    return HttpResponse(template.render(context, request))

# First article

def first_article(request):
    """Reference to the article.html """
    template = loader.get_template('ScienceBlog/main_blog.html')
    context = {}
    return HttpResponse(template.render(context, request))

# d3 multiplot

def multiplot(request):
    """Reference to the article.html """
    template = loader.get_template('ScienceBlog/multiplot.html')
    context = {}
    return HttpResponse(template.render(context, request))

# d3 gridplot

def gridplot(request):
    """Reference to the article.html """
    template = loader.get_template('ScienceBlog/gridplot.html')
    context = {}
    return HttpResponse(template.render(context, request))

# django-nvd3 - piechart

def piechart(request):
    """ constructing a rudimentary piechart """
    template = loader.get_template('ScienceBlog/piechart.html')    
    xdata = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries", "Blueberries", "Dates", "Grapefruit", "Kiwi", "Lemon"]
    ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]
    chartdata = {'x': xdata, 'y': ydata}
    charttype = "pieChart"
    chartcontainer = 'piechart_container'
    data = {
            'charttype': charttype,
            'chartdata': chartdata,
            'chartcontainer': chartcontainer,
            'extra': {
                        'x_is_date': False,
                        'x_axis_format': '',
                        'tag_script_js': True,
                        'jquery_on_ready': False,
                    }
        }
    return HttpResponse(template.render(data,request))
    


# Some csv files to read into the first_article template - article.html

def paper1_data(request):     

    """
    Reference linked to the data in the first_article 
    
    topic_id refers to the id (or pk) or the index of each entry in the database.
    To make sure that we have the right data that is avaliable, we need to make sure
    that a 404 errror page is installed in case the databse enttry is not there

    """
    # form data 
    # If this is a POST request then process the Form data
    

    # Simple datetime 

    now = datetime.datetime.now()
    # col0 = [1,2,3,4,5,6] # testing array to test whether the value prints out correctly 

    # arrays to work with after reading the csv file in 

    col0 = []
    col1 = []
    col2 = []
    col3 = []

    # Find the file path to
    # csv files we want to work with 

    file_path = os.path.join(settings.STATIC_ROOT, '/var/www/staticfiles/ScienceBlog/csv/morley.csv')
    cereal_path = os.path.join(settings.STATIC_ROOT, 'ScienceBlog/csv/cereal.csv')
    
    with open(file_path) as f:

        reader = csv.reader(f, delimiter=',')
        
        for row in reader:
            col1.append(row[0])
            col2.append(row[1])
            col3.append(row[2])

    # Now, zip the values
    list_of_values = zip(col1,col2,col3)    
    all_Science = Science.objects.all()
    all_papers = linktopapers.objects.all()
   
    template = loader.get_template('ScienceBlog/JEarticle.html') # refer to JEarticle.html inside the templates
    
    context = {
        'all_Science' : all_Science, # adding the context for the sql database 
        'col0' : col0,
        'col1' : col1,
        'col2' : col2,
        'col3' : col3,
        'list_of_values' : list_of_values,
        'form': NameForm,
        'papers': all_papers,
    }
    # Now add the  
    return HttpResponse(template.render(context,request))


def second_article(request):
    """ Referencing the second article """
    template = loader.get_template('ScienceBlog/testplot.html')
    context = {}
    return HttpResponse(template.render(context, request))

# Getting the csv file
def get_csv(request):
    template = loader.get_template('ScienceBlog/index.html')
    return HttpResponse(template.render(context, request))

# getting from urls.py = "views.index" - so now, we have to write a index function!


# importing the forms data to the views method

#def form_deadline(request,pk):
#   
#    # What is the difference between the POST and GET?
#    # POST method - should always be used if the data is going to result in a chaangee in the servers database
#    # GET method - should be used for forms that  dont change user data ( e.g. a search form). It is recommeneded when ou want to bookmark
#    # or rshare a URL
#    
#    if request.method == 'POST': 
#        # Create form instance and populate it with data for the request (binding):
#        form = NameForm(request.POST)
#
#        # Check if the form is valid:
#        if form.is_valid():
#            # process the data in NameForm.clean_deadline_date as required 
#            

def upload_file(request):    
    template = loader.get_template('ScienceBlog/upload.html')

    """
    Function to use the UploadFileForm(forms.Form) in forms.py

    Notice that we have to pass request.FILES into the form's constructor; this 
    is how file data gets bound into a form

    """
    if request.method == 'POST':
        # upload the data upload information onto form 
        form = UploadFileForm(request.POST, request.FILES) # forms.UploadFileForm
        if form.is_valid():
            handle_uploaded_file(request.FILE['file'])
            return HttpResponseRedirect('/success/url')
        else:
            form = UploadFileForm() 
        context = {'form':form}
        return HttpResponse(template.render(context,request))

    
def linkpapers(request):
    all_papers = linktopapers.objects.all()
    papercontext = {
        'all_papers': all_papers,
    }
    return HttpResponse(template.render(context,request))

def pieChart(request):
    """

    """
    template = loader.get_template('ScienceBlog/JEarticle.html')
    xdata = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries", "Blueberries", "Dates", "Grapefruit", "Kiwi", "Lemon"]
    ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]
    chartdata = {'x': xdata, 'y': ydata}
    charttype = "pieChart"
    chartcontainer = 'piechart_container'
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
    'extra': {
                        'x_is_date': False,
                        'x_axis_format': '',
                        'tag_script_js': True,
                        'jquery_on_ready': False,
                    }
    }

    context = {
        'xdata' : xdata, # adding the context for the sql database 
        'ydata' : ydata,
        'chartdata' : chartdata,
        'charttype' : charttype,
        'data' : data,
    }

    
    return HttpResponse(template.render(context,request))


# Forms

"""
Form data sent back to a Django website is processed by the view, generally the 
same view which published the form. 

To handle the form we need to instantiate it in the view for the URL where we want it to be 
published

"""
# At this point, we have new information received from the customer
# via the form

