from django.shortcuts import render
from django.views import View
from .models import Blog
# Create your views here.


class BlogListView(View):
    def get(self, request):
        blogs = Blog.objects.all()
        return render(request, 'online_course/blog.html', {"blogs": blogs})


class BlogDetailView(View):
    def get(self, request):
        blogs = Blog.objects.all()
        a = 0
        for blog in blogs:
            data = blog
            for comment in data.comments.all():
                a += 1
        return render(request, 'online_course/single.html', {"blogs": blogs, 'a': a})
