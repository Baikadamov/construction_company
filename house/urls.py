from django.urls import path

from house.views import *

urlpatterns = [
    path('', index, name='home'),
    path('projects/', projectsPage, name='projectsPage'),
    path('calculator/', calculator, name='calculator'),
]
