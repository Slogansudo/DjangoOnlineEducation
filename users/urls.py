from django.urls import path
from .views import IndexView, AboutView, ContactView, UserRegisterView, UsersLoginView, UsersLogoutView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UsersLoginView.as_view(), name='login'),
    path('logout/', UsersLogoutView.as_view(), name='logout')
]

