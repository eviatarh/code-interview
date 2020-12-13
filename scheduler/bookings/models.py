from django.db import models

# Create your models here.


class Speciality(models.Model):
    type = models.CharField(max_length=100, unique = True)


class Provider(models.Model):
    name = models.CharField(max_length = 200, primary_key = True)
    specialities = models.ManyToManyField(Speciality)
    score = models.DecimalField(decimal_places=1, max_digits=3)


class Availabilities(models.Model):
    from_time = models.PositiveBigIntegerField()
    to_time = models.PositiveBigIntegerField()
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
