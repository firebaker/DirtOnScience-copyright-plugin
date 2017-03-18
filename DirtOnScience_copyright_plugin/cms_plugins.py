from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from djangocms_text_ckeditor.cms_plugins import TextPlugin

from .models import CopyrightPluginModel

class CopyrightPlugin(CMSPluginBase):
    model = CopyrightPluginModel
    module = _("Dirt On Science")
    name = _("Copyright Plugin")
    render_template = "copyright_plugin.html"
    cache = False
    text_enabled = True

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(CopyrightPlugin)
