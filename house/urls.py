from django.urls import path

from house.views import *

urlpatterns = [
    path('', index, name='home'),
    path('projects/', projectsPage, name='projectsPage'),
    path('projects/<str:pk>', project, name='project'),
    path('calculator/', calculator, name='calculator'),
    path('contacts/', contacts, name='contacts'),
]
