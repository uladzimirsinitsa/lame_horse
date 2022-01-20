from django.contrib import admin
from promo_en.models import PromoEn, TagPromoEn
# Register your models here.


@admin.register(PromoEn)
class PromoAdmin(admin.ModelAdmin):
    """Новость"""
    model = PromoEn

    list_display = ["title", "author", "date", "published", "id"]
    list_editable = ["published", ]
    search_fields = ["title", ]
    list_filter = ["author", "published", ]


admin.site.register(TagPromoEn)
