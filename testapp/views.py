from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Course
from django.template import loader

def Courses(request):
    ac=Course.objects.all()
    template=loader.get_template('testapp/Courses.html')
    context={
        'all_courses': ac,

    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse('<h1>This is the homepage<h1>')

def detail(request, course_id):
    try:
        course=Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        raise Http404('Course Not Available')
    template=loader.get_template('testapp/courses_detail.html')
    context={
        'course': course,
    }
    return HttpResponse(template.render(context, request))
    #return HttpResponse('<h2>These are the course details for course id: <h2>' +str(course_id) +'</h2>')