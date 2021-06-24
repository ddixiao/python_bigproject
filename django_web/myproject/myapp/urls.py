from django.contrib import admin
from myapp import views
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles

urlpatterns = [
    path('',views.title),
    path('uploadimg',views.uploadimg),
    path('show',views.showimg),
    path("project1",views.Project1),
    path("1",views.Project1),
    path("project2",views.Project2),
    path("2",views.Project2),
    path("project3",views.Project3),
    path("3",views.Project3),
    path("project4",views.Project4),
    path("4",views.Project4),
    #url(r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root':'/home/anna/Documents/django_py/showImg/static'})
]

urlpatterns += staticfiles_urlpatterns()

