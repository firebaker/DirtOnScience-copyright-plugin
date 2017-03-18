DirtOnScience-copyright-plugin is a django-cms plugin that provides an easy and intuitive method for diplaying featured work's (e.g. images, videos, music, etc.) copyright information to web users.

This plugin can be used as a standalone plugin or inline text using the djangocms-text-ckeditor.

All model values initialize to an empty string. Use the django-cms admin console to modify values. 

Use "template/copyright_plugin.html" to modify how content is displayed in web browsers. Currently content is displayed using the bootsrap's popover effect, after clicking the "Copyright" text which is in a href tag.

In order to use the plugin as-is (i.e. popover effect), your webpage must include both "tether.js" and "bootstrap.js". Additionally "tether.js" must be imported prior to "bootsrap.js", to work correctly.
