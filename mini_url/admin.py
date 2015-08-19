from django.contrib import admin

# Register your models here.

from .models import MiniURL

class MiniURLAdmin(admin.ModelAdmin):
    list_display = ('url', 'code', 'date', 'pseudo', 'nb_acces')
    list_filter = ('pseudo', )
    date_hierarchy = 'date'
    ordering = ('date', )
    search_fields = ('url', )

    class Media:
        js = [
        '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
        '/static/grappelli/tinymce_setup/tinymce_setup.js',

    ]


admin.site.register(MiniURL, MiniURLAdmin)