from django.urls import path
from courses.views.course_views import *


app_name = 'courses'
urlpatterns =[

    path("all", course_list, name="all_courses")
]