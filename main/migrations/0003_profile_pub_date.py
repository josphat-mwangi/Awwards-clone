# Generated by Django 3.1 on 2020-08-18 15:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200818_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
