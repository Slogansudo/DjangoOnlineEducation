from django.shortcuts import render
from .models import Course, Mentor
from django.views import View
# Create your views here.


class CourseView(View):
    def get(self, request):
        courses = Course.objects.all()
        return render(request, 'online_course/course.html', {'courses': courses})


class MentorView(View):
    def get(self, request):
        mentors = Mentor.objects.all()
        return render(request, 'online_course/teacher.html', {'mentors': mentors})
