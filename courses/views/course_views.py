from rest_framework import *
from django.http import *
from courses.models.course import Course
from django.shortcuts   import *
from courses.serializers.CourseSerializer import CourseSerializer

def course_list(request):
    courses = Course.objects.all()

    serializer = CourseSerializer(courses, many=True)
    return JsonResponse(serializer.data, safe=False)

def course_detail(request, pk):
    course = get_object_or_404(Course, pk = pk)

    serializer = CourseSerializer(course)
    return JsonResponse(serializer.data)