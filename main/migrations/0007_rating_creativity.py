# Generated by Django 3.1 on 2020-08-19 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200819_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='creativity',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0),
        ),
    ]
