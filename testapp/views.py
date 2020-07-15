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

def box(request):
    template=loader.get_template('testapp/box.html')
    return HttpResponse(template.render({}, request))

def box_game(request):
    template=loader.get_template('testapp/box_game.html')
    return HttpResponse(template.render({}, request))

def tank_game(request):
    template=loader.get_template('testapp/tank_game.html')
    return HttpResponse(template.render({}, request))