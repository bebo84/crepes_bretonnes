# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mini_url', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='miniurl',
            name='ghi_chu',
            field=models.TextField(blank=True, verbose_name='Ghi chu'),
        ),
    ]
