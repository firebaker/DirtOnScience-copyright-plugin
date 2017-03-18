# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='DOSCopyrightPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, parent_link=True, primary_key=True, auto_created=True, to='cms.CMSPlugin', related_name='dos_copyright_plugin_doscopyrightpluginmodel')),
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
    ]
