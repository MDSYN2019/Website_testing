# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from .models import Question, Choice, Contact

class ContactsTest(TestCase):
    """ Contact model tests """
    def test_str(self):
        contact = Contact(first_name = "Blad", last_name="ibla")

        self.assertEquals(
            str(contact),
            "Blad ibla",
        )

class QuestionTest(TestCase):
    """Question Model Test"""
    def test_question(self):
        question = Question(question_text="What is your name")
        self.assertEquals(
            str(question),
            "What is your name",
        )


