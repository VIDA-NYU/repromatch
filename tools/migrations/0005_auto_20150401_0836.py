# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0004_auto_20150331_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='paper',
            field=models.URLField(default=b'', verbose_name=b'Link To Paper', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tool',
            name='source',
            field=models.URLField(default=b'', verbose_name=b'Source Code Repository', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tool',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tool',
            name='website',
            field=models.URLField(default=b'', verbose_name=b'Website', blank=True),
            preserve_default=True,
        ),
    ]
