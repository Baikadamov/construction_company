from django.urls import path

from house.views import *

urlpatterns = [
    path('', index, name='home'),
    path('projects/', projectsPage, name='projectsPage'),
    path('search', search, name='search'),
    path('project/<str:pk>', project, name='project'),
    path('calculator/', calculator, name='calculator'),
    path('contacts/', contacts, name='contacts'),
    path('profile/<str:pk>', profile, name='profile'),
    path('myprofile/', myprofile, name='myprofile'),
    path('order', order, name='order'),
    path('moder/', moder, name='moder'),
    path('updateorder', updateorder, name='updateorder'),

    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),
    path('signin/', signin, name='signin'),
]
