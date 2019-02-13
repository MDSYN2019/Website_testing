# Standard django imports #  

from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect 
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.urls import reverse
import datetime

from django.views import generic
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from django.http.response import HttpResponse
from django.template import loader
from django.contrib.staticfiles.storage import staticfiles_storage

from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def newpage(request):
    """Reference to the ieee.html """
    template = loader.get_template('Contact/new.html')
    context = {}
    return HttpResponse(template.render(context, request))



