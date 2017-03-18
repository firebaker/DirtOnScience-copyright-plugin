# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DirtOnScience_copyright_plugin', '0002_auto_20170315_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='copyrightpluginmodel',
            name='license_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='copyrightpluginmodel',
            name='source_url',
            field=models.URLField(blank=True),
        ),
    ]
