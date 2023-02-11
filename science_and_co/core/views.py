from django.shortcuts import render
from django.http import HttpResponse


from django.views import generic  # django package.

# Create your views here.


class HomeView(generic.TemplateView):
    """
    inheriting from TemplateView

    render a template,
    """

    template_name = "core/index.html"


def index(request) -> HttpResponse:
    """ """

    latest_question_list = Question.objects.order_by("-pub_date")[:5]

    template = loader.get_template("Homepage/index.html")

    context = {
        "latest_question_list": latest_question_list,
    }

    return HttpResponse(template.render(context, request))


def homepage(request) -> HttpResponse:
    """ """
    Paperlist = Content1Model.objects.all()
    output = ", ".join([paper.Journal_title for paper in Paperlist])
    return HttpResponse(output)
