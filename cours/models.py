from django.db import models


# Create your models here.
class Speciality(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/cours/specialities/')
    last_updated = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    class Price_types(models.TextChoices):
        s = "USD", "$"
        sum = "UZS", "so'm"
    title = models.CharField(max_length=50)
    description = models.TextField()
    active_users = models.PositiveIntegerField(default=0)
    price = models.FloatField()
    price_type = models.CharField(max_length=10, choices=Price_types.choices, default=Price_types.sum)
    rating = models.FloatField(default=0)
    image = models.ImageField(upload_to='media/cours/courses/', blank=True)
    speciality = models.ManyToManyField(Speciality)
    last_updated = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Position(models.Model):
    name = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Mentor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/cours/teacher')
    age = models.IntegerField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)
    last_updated = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.first_name

