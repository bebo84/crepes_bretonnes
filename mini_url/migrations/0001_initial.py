# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiniURL',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('url', models.URLField(verbose_name='URL a reduire', unique=True)),
                ('code', models.CharField(max_length=6, unique=True)),
                ('date', models.DateTimeField(verbose_name="Date d'enregistrement", auto_now_add=True)),
                ('pseudo', models.CharField(max_length=255, null=True, blank=True)),
                ('nb_acces', models.IntegerField(default=0, verbose_name="Nombre d'acces a l'URL")),
            ],
            options={
                'verbose_name_plural': 'Minis URL',
                'verbose_name': 'Mini URL',
            },
        ),
    ]
