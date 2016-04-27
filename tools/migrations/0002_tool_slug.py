# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='slug',
            field=models.SlugField(default='vistrails', editable=False),
            preserve_default=False,
        ),
    ]
