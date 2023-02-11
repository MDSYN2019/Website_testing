"""
Testing in Django
------------------


Automated testing is an extremel useful bug-killing tool for the modern web developer. You can use 
a collection of tess - a test suite, to solve, avoid a number of problems.


=> When you're writing new code, you can use tests to validate your code works as expected

=> When you're refactoring or modifying old code, you can use tests to ensure your changes haent affeced your applications
   bheavior unexpectedly

---

Writing Tests
-------------

Djangos unit tests use a python standard library module - unittest. This module defines tess using a class-based
approach.

"""

from django.test import TestCase
from myapp.models import Animal


class AnimalTestCase(TestCase):  # Inheriting from Testcase
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")
