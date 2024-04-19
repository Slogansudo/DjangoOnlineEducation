from django.urls import path
from .views import CourseView, MentorView, CourseDetailView, CourseUpdateView, CourseDeleteView, AddCourseView, SpecialityDetailView, SpecialityUpdateView, SpecialityDeleteView
urlpatterns = [
    path('course/', CourseView.as_view(), name='courses'),
    path('mentor/', MentorView.as_view(), name='mentors'),
    path('course/<int:id>/', CourseDetailView.as_view(), name='course-detail'),
    path('course/<int:id>/update/', CourseUpdateView.as_view(), name='course-update'),
    path('course/<int:id>/delete/', CourseDeleteView.as_view(), name='course-delete'),
    path('course/add_course/', AddCourseView.as_view(), name='add-course'),
    path('speciality/<int:id>/', SpecialityDetailView.as_view(), name='speciality-detail'),
    path('speciality/<int:id>/update/', SpecialityUpdateView.as_view(), name='speciality-update'),
    path('speciality/<int:id>/delete/', SpecialityDeleteView.as_view(), name='speciality-delete')
]