from rest_framework import *
from django.http import *
from courses.models.course import Course

def course_list(request):
    courses = Course.objects.all()
    return  HttpResponse(" ".join([str(course) for course in courses]))
