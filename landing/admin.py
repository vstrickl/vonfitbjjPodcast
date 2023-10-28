from django.contrib import admin

from .models import Hero, SocialMenu, FontFamily

# Register your models here.
admin.site.register(SocialMenu)

class HeroAdmin(admin.ModelAdmin):

    autocomplete_fields = ['header_font', 'general_font']

admin.site.register(Hero, HeroAdmin)

class FontFamilyAdmin(admin.ModelAdmin):

    list_display = ("family_name", "serif_type")
    search_fields = ['family_name']

admin.site.register(FontFamily, FontFamilyAdmin)