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

def homepage(request):
    return HttpResponse("Hello (again) World")
"""
def AuthorView(generic.ListView):
    template_name = 'contact/a.html'
    context_object_name = 'all_authors'
    def get_queryset(self):
        return Author.objects.all()
"""
