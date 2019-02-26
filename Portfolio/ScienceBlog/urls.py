from django.conf.urls import url
from .views import PostListView # new import
from . import views

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='first_article'),
    url(r'^Jarzynski_article/$', views.paper1_data, name='Jarzynski_article'), # /ScienceBlog/Jarzynski_article/ 
    url(r'^Jarzynski_article/multiplot/$', views.multiplot, name='multiplot'),
    url(r'^Jarzynski_article/gridplot/$', views.gridplot, name='gridplot'),
    url(r'^Jarzynski_article/piechart/$', views.piechart, name='piechart'),
    url(r'^Jarzynski_article/upload/$', views.upload_file, name='upload_file'),
    url(r'^Jarzynski_article/test/$', views.second_article, name='second_article'),
    url(r'^NP_mechanism/$', views.NP_article, name='NP_article'),
    url(r'^lipid/$', views.lipid, name='lipid'),
    url(r'^replacement/$', views.replacement, name='replacement'),
    url(r'^$', views.linkpapers, name='linkpapers'),
]
