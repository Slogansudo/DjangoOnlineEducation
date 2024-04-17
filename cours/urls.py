from django.urls import path
from .views import CourseView, MentorView
urlpatterns = [
    path('course/', CourseView.as_view(), name='courses'),
    path('mentor/', MentorView.as_view(), name='mentors'),
]