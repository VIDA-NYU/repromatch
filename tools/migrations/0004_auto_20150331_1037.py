# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0003_auto_20150331_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='paper',
            field=models.URLField(default=b'', verbose_name=b'Link To Paper'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tool',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'Software name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tool',
            name='source',
            field=models.URLField(default=b'', verbose_name=b'Source Code Repository'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tool',
            name='website',
            field=models.URLField(default=b'', verbose_name=b'Website'),
            preserve_default=True,
        ),
    ]
