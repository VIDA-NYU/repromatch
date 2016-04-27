# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0002_tool_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='description',
            field=models.CharField(max_length=1024, verbose_name=b'Description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tool',
            name='document_linkage_note',
            field=models.CharField(default=b'', max_length=1024, verbose_name=b'Note', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tool',
            name='experiment_sharing_note',
            field=models.CharField(default=b'', max_length=1024, verbose_name=b'Note', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tool',
            name='longevity_note',
            field=models.CharField(default=b'', max_length=1024, verbose_name=b'Note', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tool',
            name='modifiability_note',
            field=models.CharField(default=b'', max_length=1024, verbose_name=b'Note', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tool',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'Tool name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tool',
            name='portability_note',
            field=models.CharField(default=b'', max_length=1024, verbose_name=b'Note', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tool',
            name='replicability_note',
            field=models.CharField(default=b'', max_length=1024, verbose_name=b'Note', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tool',
            name='representation_note',
            field=models.CharField(default=b'', max_length=1024, verbose_name=b'Note', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tool',
            name='supports_note',
            field=models.CharField(default=b'', max_length=1024, verbose_name=b'Note', blank=True),
            preserve_default=True,
        ),
    ]
