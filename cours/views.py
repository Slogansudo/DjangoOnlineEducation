from django.shortcuts import render, redirect
from .models import Course, Mentor, Speciality
from django.views import View

# Create your views here.


class CourseView(View):
    def get(self, request):
        search = request.GET.get('search')
        if not search:
            courses = Course.objects.all()
            return render(request, 'online_course/course.html', {'courses': courses})
        else:
            courses = Course.objects.filter(title__icontains=search)
            return render(request, 'online_course/course.html', {'courses': courses, 'search': search})
class MentorView(View):
    def get(self, request):
        mentors = Mentor.objects.all()
        return render(request, 'online_course/teacher.html', {'mentors': mentors})


class CourseDetailView(View):
    def get(self, request, slug):
        course = Course.objects.get(slug=slug)
        return render(request, 'online_course/course_detail.html', {'course': course})


class CourseUpdateView(View):
    def get(self, request, id):
        course = Course.objects.get(id=id)
        return render(request, 'online_course/course_update.html', {'course': course})

    def post(self, request, id):
        new_title = request.POST.get('title')
        new_description = request.POST.get('description')
        new_price = request.POST.get('price')
        course = Course.objects.get(id=id)
        course.title = new_title
        course.description = new_description
        course.price = new_price
        course.save()
        return redirect('courses')


class CourseDeleteView(View):
    def get(self, request, id):
        course = Course.objects.get(id=id)
        course.delete()
        return redirect('courses')


class AddCourseView(View):
    def get(self, request):
        return render(request, 'online_course/add_course.html')

    def post(self, request):
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.POST.get('image')
        rating = request.POST.get('rating')
        print(image)
        course = Course(title=title, description=description, price=price, rating=rating, image=f"media/cours/courses/{image}")
        course.save()
        return redirect('courses')


class SpecialityDetailView(View):
    def get(self, request, id):
        speciality = Speciality.objects.get(id=id)
        return render(request, 'online_course/speciality_detail.html', {'speciality': speciality})


class SpecialityUpdateView(View):
    def get(self, request, id):
        speciality = Speciality.objects.get(id=id)
        return render(request, 'online_course/speciality_update.html', {'speciality': speciality})

    def post(self, request, id):
        speciality = Speciality.objects.get(id=id)
        title = request.POST.get('title')
        speciality.title = title
        speciality.save()
        return redirect('index')


class SpecialityDeleteView(View):
    def get(self, request, id):
        speciality = Speciality.objects.get(id=id)
        speciality.delete()
        return redirect('index')
