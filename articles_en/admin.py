from django.contrib import admin
from articles_en.models import Article_en
# Register your models here.


@admin.register(Article_en)
class ArticleAdmin(admin.ModelAdmin):
    model = Article_en

    list_display = ["title", "author", "date", "published", "id"]
    list_editable = ["published", ]
    search_fields = ["title", ]
    list_filter = ["author", "published", ]
