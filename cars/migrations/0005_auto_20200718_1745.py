# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-18 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20200714_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image2',
            field=models.ImageField(null=True, upload_to='media/images'),
        ),
        migrations.AlterField(
            model_name='car',
            name='image3',
            field=models.ImageField(null=True, upload_to='media/images'),
        ),
        migrations.AlterField(
            model_name='car',
            name='image4',
            field=models.ImageField(null=True, upload_to='media/images'),
        ),
        migrations.AlterField(
            model_name='car',
            name='image5',
            field=models.ImageField(null=True, upload_to='media/images'),
        ),
    ]
