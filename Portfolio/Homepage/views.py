from __future__ import unicode_literals
from django.template import loader 
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render

# Models importing

from .models import Question # For the blog page
from .models import Content1Model
from .models import Contact

# generic views
from django.views.generic import ListView
from django.views.generic import CreateView

# Raising a 404 error

def index(request):
    # Now to work with the models stated
    latest_question_list  = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('Homepage/index.html')
    context = {
        'latest_question_list': latest_question_list,
        }
    return HttpResponse(template.render(context,request))

def homepage(request):
    Paperlist = Content1Model.objects.all()
    output = ", ".join([paper.Journal_title for paper in Paperlist])
    return HttpResponse(output)

# research reference list of journals 
def research1(request,question_id):
    research_list = Content1Model.objects.order_by('-pub_date')[:5]
    template = loader.get_template('Homepage/content1.html')
    context = {
        'research_list' : research_list,
    }
    return HttpResponse(template.render(context,request))

"""
Need to adapt this to suit my own website
"""
