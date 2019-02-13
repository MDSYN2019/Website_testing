from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url('', views.newpage, name='newpage'),
]
