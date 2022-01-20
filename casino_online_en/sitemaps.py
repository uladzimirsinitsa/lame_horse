from django.contrib.sitemaps import Sitemap
from .models import Casino_en
from django.urls import reverse


class CasinoEnSitemap(Sitemap):
    priority = 1.0
    protocol = "https"
    changefreq = 'weekly'

    def items(self):
        return Casino_en.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.date_update

    def location(self, obj):
        return obj.get_absolute_url()


class CasinoListEnSitemap(Sitemap):
    priority = 0.9
    protocol = "https"
    changefreq = 'weekly'

    def items(self):
        return ['casino_list_en']

    def location(self, item):
        return reverse(item)
