# Generated by Django 3.1.4 on 2020-12-13 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availabilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_time', models.PositiveBigIntegerField()),
                ('to_time', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='provider',
            name='availableDates',
            field=models.ManyToManyField(to='bookings.Availabilities'),
        ),
        migrations.AddField(
            model_name='provider',
            name='specialities',
            field=models.ManyToManyField(to='bookings.Speciality'),
        ),
    ]
