# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DirtOnScience_copyright_plugin', '0003_auto_20170315_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='copyrightpluginmodel',
            name='license',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='copyrightpluginmodel',
            name='source',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]
