from cms.models.pluginmodel import CMSPlugin

from django.db import models

# Create your models here.

class CopyrightPluginModel(CMSPlugin):
    source = models.CharField(max_length=32, blank=True)
    source_url = models.URLField(blank=True)
    license = models.CharField(max_length=32, blank=True)
    license_url = models.URLField(blank=True)
