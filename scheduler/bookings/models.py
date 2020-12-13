from django.db import models

# Create your models here.


class Speciality(models.Model):
    type = models.CharField(max_length=100, unique = True)


class Availabilities(models.Model):
    from_time = models.PositiveBigIntegerField()
    to_time = models.PositiveBigIntegerField()


class Provider(models.Model):
    name = models.CharField(max_length = 200, primary_key = True)
    specialities = models.ManyToManyField(Speciality)
    availableDates = models.ManyToManyField(Availabilities)
    score = models.DecimalField(decimal_places=1, max_digits=3)

class Book(models.Model):
    name = models.ForeignKey(Provider, on_delete=models.CASCADE)
    date = models.ForeignKey(Availabilities, on_delete=models.CASCADE)