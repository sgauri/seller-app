# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipkart', '0003_delete_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='palazzo',
            name='img',
            field=models.ImageField(blank=True, default='logo_emeros.jpg', null=True, upload_to='palazzo_img'),
        ),
    ]
