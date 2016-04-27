# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Tool name')),
                ('description', models.CharField(max_length=400, verbose_name=b'Description')),
                ('website', models.URLField(verbose_name=b'Website')),
                ('source', models.URLField(verbose_name=b'Source Repository')),
                ('capture', models.BooleanField(default=False, verbose_name=b'Capture')),
                ('capture_os', models.BooleanField(default=False, verbose_name=b'OS-Based Capture')),
                ('capture_code', models.BooleanField(default=False, verbose_name=b'Code-Based Capture')),
                ('capture_workflow', models.BooleanField(default=False, verbose_name=b'Workflow-Based Capture')),
                ('capture_data', models.BooleanField(default=False, verbose_name=b'Data-Based Capture')),
                ('capture_note', models.CharField(default=b'', max_length=200, verbose_name=b'Note', blank=True)),
                ('representation', models.BooleanField(default=False, verbose_name=b'Representation')),
                ('representation_descriptive_only', models.BooleanField(default=False, verbose_name=b'Descriptive-Only')),
                ('representation_executable', models.BooleanField(default=False, verbose_name=b'Executable')),
                ('representation_note', models.CharField(default=b'', max_length=200, verbose_name=b'Note', blank=True)),
                ('replicability', models.BooleanField(default=False, verbose_name=b'Replicability')),
                ('replicability_note', models.CharField(default=b'', max_length=200, verbose_name=b'Note', blank=True)),
                ('modifiability', models.BooleanField(default=False, verbose_name=b'Modifiability')),
                ('modifiability_note', models.CharField(default=b'', max_length=200, verbose_name=b'Note', blank=True)),
                ('portability', models.CharField(default=b'NONE', max_length=6, verbose_name=b'Portability', choices=[(b'NONE', b'None'), (b'LOW', b'Low'), (b'MEDIUM', b'Medium'), (b'HIGH', b'High')])),
                ('portability_note', models.CharField(default=b'', max_length=200, verbose_name=b'Note', blank=True)),
                ('longevity', models.BooleanField(default=False, verbose_name=b'Longevity')),
                ('longevity_archiving', models.BooleanField(default=False, verbose_name=b'Archiving')),
                ('longevity_upgrading', models.BooleanField(default=False, verbose_name=b'Upgrading')),
                ('longevity_note', models.CharField(default=b'', max_length=200, verbose_name=b'Note', blank=True)),
                ('document_linkage', models.BooleanField(default=False, verbose_name=b'Document Linkage')),
                ('document_linkage_by_reference', models.BooleanField(default=False, verbose_name=b'By Reference')),
                ('document_linkage_inline', models.BooleanField(default=False, verbose_name=b'Inline')),
                ('document_linkage_note', models.CharField(default=b'', max_length=200, verbose_name=b'Note', blank=True)),
                ('experiment_sharing', models.BooleanField(default=False, verbose_name=b'Experiment Sharing')),
                ('experiment_sharing_archival', models.BooleanField(default=False, verbose_name=b'Archival')),
                ('experiment_sharing_hosted_execution', models.BooleanField(default=False, verbose_name=b'Hosted Execution')),
                ('experiment_sharing_note', models.CharField(default=b'', max_length=200, verbose_name=b'Note', blank=True)),
                ('supports_osx', models.BooleanField(default=False, verbose_name=b'Support for OSX')),
                ('supports_windows', models.BooleanField(default=False, verbose_name=b'Support for Windows')),
                ('supports_linux', models.BooleanField(default=False, verbose_name=b'Support for Linux')),
                ('supports_note', models.CharField(default=b'', max_length=200, verbose_name=b'Note', blank=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
