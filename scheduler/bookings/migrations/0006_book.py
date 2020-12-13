# Generated by Django 3.1.4 on 2020-12-13 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_auto_20201213_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.availabilities')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.provider')),
            ],
        ),
    ]