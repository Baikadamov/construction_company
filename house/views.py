from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from house.models import Project


# Create your views here.

def index(request):
    return render(request, 'house/index.html')


def projectsPage(request):
    project = Project.objects.all()
    context = {
        'project': project,
    }
    return render(request, 'house/projects.html', context=context)


def calculator(request):
    return HttpResponse('<h1> There will be calculator</h1>')


# HANDLE ERRORS
def error400(request, exception):
    return HttpResponseNotFound('<h1>Page not found 400</h1>')
    # return render(request, 'messenger/errors/400.html', status=400)


def error403(request, exception):
    return HttpResponseNotFound('<h1>Page not found 403 </h1>')
    # return render(request, 'messenger/errors/403.html', status=403)


def error404(request, exception):
    return HttpResponseNotFound('<h1>Page not found 404</h1>')


def error500(request):
    return HttpResponseNotFound('<h1>Page not found 500</h1>')
    # return render(request, 'messenger/errors/500.html', status=500)
