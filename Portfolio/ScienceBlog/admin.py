# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Science, Subfield, linktopapers

# Registering the models
admin.site.register(Science)
admin.site.register(Subfield)
admin.site.register(linktopapers)
