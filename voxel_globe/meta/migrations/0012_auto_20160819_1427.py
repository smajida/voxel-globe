# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0011_remove_blank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='_attributes',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='cameraset',
            name='_attributes',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='controlpoint',
            name='_attributes',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='coordinatesystem',
            name='_attributes',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='coordinatetransform',
            name='_attributes',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='image',
            name='_attributes',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='imageset',
            name='_attributes',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='pointcloud',
            name='_attributes',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='satteleventresult',
            name='_attributes',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='satteleventtrigger',
            name='_attributes',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='sattelgeometryobject',
            name='_attributes',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='sattelsite',
            name='_attributes',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='scene',
            name='_attributes',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='tiepoint',
            name='_attributes',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='tiepointset',
            name='_attributes',
            field=models.TextField(blank=True, default=b''),
        ),
        migrations.AlterField(
            model_name='voxelworld',
            name='_attributes',
            field=models.TextField(blank=True, default=b''),
        ),
    ]
