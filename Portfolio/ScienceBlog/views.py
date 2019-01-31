import os
import csv # involved in loading a csv file
import datetime

from django.shortcuts import render
from django.http import HttpResponse ## Standard website response you want
from django.http import HttpResponseNotFound
from django.conf import settings

from .models import Science 
from .models import linktopapers
 
# django-rest-pandas - still unused 
from rest_pandas import PandasSimpleView
import pandas as pd 

# HTML & CSS loader
from django.template import loader
from django.contrib.staticfiles.storage import staticfiles_storage

#from .forms import NameForm 

# First article

def first_article(request):
    """Reference to the article.html """
    template = loader.get_template('ScienceBlog/article.html')
    context = {}
    return HttpResponse(template.render(context, request))

# Some csv files to read into the first_article template - article.html

def paper1_data(request):    
    """Reference linked to the data in the first_article """
    # Simple datetime 
    now = datetime.datetime.now()
    # col0 = [1,2,3,4,5,6] # testing array to test whether the value prints out correctly 

    # arrays to work with after reading the csv file in 

    col1 = []
    col2 = []
    col3 = []

    # Find the file path to
    # csv files we want to work with 

    file_path = os.path.join(settings.STATIC_ROOT, 'ScienceBlog/csv/morley.csv')
    cereal_path = os.path.join(settings.STATIC_ROOT, 'ScienceBlog/csv/cereal.csv')
    
    with open(file_path) as f:

        reader = csv.reader(f, delimiter=',')
        
        for row in reader:
            col1.append(row[0])
            col2.append(row[1])
            col3.append(row[2])

    # Now, zip the values
    list_of_values = zip(col1,col2,col3)    
    all_Science = Science.objects.all() # same as in the shell - we ne
    template = loader.get_template('ScienceBlog/JEarticle.html')
    context = {
        'all_Science' : all_Science, # adding the context for the sql database 
        'col0' : col0,
        'col1' : col1,
        'col2' : col2,
        'col3' : col3,
        'list_of_values' : list_of_values, 
    }

    return HttpResponse(template.render(context,request))

def second_article(request):
    """ Referencing the second article """
    template = loader.get_template('ScienceBlog/JEarticle.html')
    context = {}
    return HttpResponse(template.render(context, request))


def paper2_data(request):    
    """Reference linked to the data in the first_article """
    # Simple datetime 
    now = datetime.datetime.now()
    # col0 = [1,2,3,4,5,6] # testing array to test whether the value prints out correctly 

    # arrays to work with after reading the csv file in 

    col1 = []
    col2 = []
    col3 = []

    # Find the file path to
    # csv files we want to work with 

    file_path = os.path.join(settings.STATIC_ROOT, 'ScienceBlog/csv/morley.csv')
    cereal_path = os.path.join(settings.STATIC_ROOT, 'ScienceBlog/csv/cereal.csv')
    
    with open(file_path) as f:

        reader = csv.reader(f, delimiter=',')
        
        for row in reader:
            col1.append(row[0])
            col2.append(row[1])
            col3.append(row[2])

    # Now, zip the values
    list_of_values = zip(col1,col2,col3)    
    all_Science = Science.objects.all() # same as in the shell - we ne
    template = loader.get_template('ScienceBlog/article.html')
    context = {
        'all_Science' : all_Science, # adding the context for the sql database 
        'col0' : col0,
        'col1' : col1,
        'col2' : col2,
        'col3' : col3,
        'list_of_values' : list_of_values, 
    }

    return HttpResponse(template.render(context,request))

 

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
            
def linkpapers(request):
    all_papers = linktopapers.objects.all()
    papercontext = {
        'all_papers': all_papers,
    }
    return HttpResponse(template.render(context,request))

def pieChart(request):
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

