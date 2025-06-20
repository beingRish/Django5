# Generated by Django 5.2.1 on 2025-05-29 18:09

import django.core.validators
import student.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='my_file',
            field=models.FileField(blank=True, upload_to='doc'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mobile',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(regex='^\\d{10}$')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pin',
            field=models.PositiveIntegerField(validators=[student.models.validate_pin_length]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='profileimg'),
        ),
    ]
