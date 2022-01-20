from django.contrib.sitemaps import Sitemap
from .models import PromoEn
from django.urls import reverse


class PromoSitemapEn(Sitemap):
    priority = 0.7
    protocol = "https"
    changefreq = 'weekly'

    def items(self):
        return PromoEn.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.date_update

    def location(self, obj):
        return obj.get_absolute_url()


class PromoListEnSitemap(Sitemap):
    priority = 0.7
    protocol = "https"
    changefreq = 'weekly'

    def items(self):
        return ['promo_list_en']

    def location(self, item):
        return reverse(item)