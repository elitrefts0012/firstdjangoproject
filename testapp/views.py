from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Allcourses
from django.template import loader

def Courses(request):
    ac=Allcourses.objects.all()
    template=loader.get_template('testapp/Courses.html')
    context={
        'ac':ac,

    }
    return HttpResponse(template.render(context, request))
    #return HttpResponse('<h1>This is the homepage<h1>')

def detail(request, couse_id):
    try:
        course=Allcourses.objects.get(pk=couse_id)
    except Allcourses.DoesNotExist:
        raise Http404('Course Not Available')
    return HttpResponse('<h2>These are the course details for course id: <h2>' +str(couse_id) +'</h2>')