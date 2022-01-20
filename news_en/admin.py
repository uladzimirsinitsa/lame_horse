from django.contrib import admin
from news_en.models import NewsEn, TagNewsEn


@admin.register(NewsEn)
class NewsAdmin(admin.ModelAdmin):
    """Новость"""
    model = NewsEn

    list_display = ["title", "author", "date", "published", "id"]
    list_editable = ["published", ]
    search_fields = ["title", ]
    list_filter = ["author", "published", ]


admin.site.register(TagNewsEn)
