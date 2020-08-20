# Generated by Django 3.1 on 2020-08-19 19:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200819_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='overall_score',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='rating',
            name='post',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='main.project'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating',
            name='profile',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='main.profile'),
            preserve_default=False,
        ),
    ]
