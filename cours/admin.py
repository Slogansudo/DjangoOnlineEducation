from django.contrib import admin
from .models import Speciality, Course, Mentor, Position
# Register your models here.


admin.site.register(Speciality)
admin.site.register(Course)
admin.site.register(Position)
admin.site.register(Mentor)