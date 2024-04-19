from django.shortcuts import render, redirect
from django.views import View
from cours.models import Course, Speciality, Mentor
from blog.models import Blog
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


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


class UserRegisterView(View):
    def get(self, request):
        return render(request, 'login-register/register_user.html')

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password_1']
        password2 = request.POST['password_2']
        if password1 != password2:
            return redirect('register')
        else:
            user = User(first_name=first_name, last_name=last_name, email=email, username=username)
            user.set_password(password1)
            user.save()
            return redirect('login')


class UsersLoginView(View):
    def get(self, request):
        return render(request, 'login-register/login_users.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        data = {'username': username,
                'password': password
                }
        login_form = AuthenticationForm(data=data)
        print(login_form.is_valid())
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login-register/login_users.html')


class UsersLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')

