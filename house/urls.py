from django.urls import path

from house.views import index, projectsPage

urlpatterns = [
    path('', index, name='home'),
    path('projects/', projectsPage, name='projectsPage'),
]
