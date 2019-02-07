# -*- coding: utf-8 -*-

from django.test import TestCase
from .models import Science

class ScienceTestCase(TestCase):
    """ Testing the Science model """
    def setup(self):
        Science.objects.create(topic="Chemistry", lab_involvement="20 hours", popularity="not so popular", picture="..")
        Science.objects.create(topic="Physics", lab_involvement="10 hours", popularity="very popular", picture="")
