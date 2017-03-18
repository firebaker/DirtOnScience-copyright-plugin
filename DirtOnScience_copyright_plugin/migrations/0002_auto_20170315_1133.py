# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('DirtOnScience_copyright_plugin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CopyrightPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(to='cms.CMSPlugin', parent_link=True, serialize=False, primary_key=True, related_name='dirtonscience_copyright_plugin_copyrightpluginmodel', auto_created=True)),
                ('source', models.CharField(max_length=20)),
                ('source_url', models.URLField()),
                ('license', models.CharField(max_length=20)),
                ('license_url', models.URLField()),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.RemoveField(
            model_name='doscopyrightpluginmodel',
            name='cmsplugin_ptr',
        ),
        migrations.DeleteModel(
            name='DOSCopyrightPluginModel',
        ),
    ]
