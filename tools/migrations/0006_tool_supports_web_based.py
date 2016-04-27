# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0005_auto_20150401_0836'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='supports_web_based',
            field=models.BooleanField(default=False, verbose_name=b'Support for Web-based access'),
            preserve_default=True,
        ),
    ]
