# Generated by Django 3.0.4 on 2020-04-04 10:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='date_created',
        ),
        migrations.AddField(
            model_name='recipe',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='datetime_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]