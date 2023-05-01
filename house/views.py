from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from house.models import Project


# Create your views here.

def index(request):
    return render(request, 'house/index.html')


def projectsPage(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'house/projects.html', context=context)


def project(request, pk):
    project = Project.objects.get(id=pk)
    print(project)
    context = {
        'project': project
    }
    return render(request, 'house/project.html', context=context)


def contacts(request   ):
    return render(request, 'house/contacts.html', )


def calculator(request):
    context = {

    }
    return render(request, 'house/calculator.html', context=context)


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
