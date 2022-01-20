from django.contrib import admin

from .models import Casino_en


class CasinoAdmin_en(admin.ModelAdmin):
    """Статичные страницы"""
    list_display = ("title", "published", "id")
    list_editable = ("published", )
    prepopulated_fields = {"slug": ("title", )}


admin.site.register(Casino_en, CasinoAdmin_en)
