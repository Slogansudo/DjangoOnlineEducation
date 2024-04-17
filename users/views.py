from django.shortcuts import render
from django.views import View
from cours.models import Course, Speciality, Mentor
from blog.models import Blog


class IndexView(View):
    def get(self, request):
        specialities = Speciality.objects.all()
        courses = Course.objects.all()
        mentors = Mentor.objects.all()
        blogs = Blog.objects.all()
        context = {
            'specialities': specialities,
            'courses': courses,
            'mentors': mentors,
            'blogs': blogs,
        }
        return render(request, 'online_course/index.html', context)


class AboutView(View):
    def get(self, request):
        return render(request, 'online_course/about.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'online_course/contact.html')
