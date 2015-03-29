# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('date_created', models.DateField(blank=True, default=None, null=True, verbose_name='date created')),
                ('album_title', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('photo_title', models.CharField(max_length=200)),
                ('date_taken', models.DateField(blank=True, default=None, null=True, verbose_name='date taken')),
                ('photo_img', models.ImageField(default='', upload_to='images/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='album',
            name='photos',
            field=models.ManyToManyField(to='photoViewer.Photo'),
            preserve_default=True,
        ),
    ]
