from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    #url(r'^(?P<question_id>[0-9]+)/research/$', views.research1, name = 'research1'),
]
