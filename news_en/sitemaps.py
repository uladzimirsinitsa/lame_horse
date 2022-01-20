from django.contrib.sitemaps import Sitemap
from .models import NewsEn
from django.urls import reverse


class NewsEnSitemap(Sitemap):
    priority = 1.0
    protocol = "https"
    changefreq = 'daily'

    def items(self):
        return NewsEn.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.date_update

    def location(self, obj):
        return obj.get_absolute_url()


class NewsListEnSitemap(Sitemap):
    priority = 1.0
    protocol = "https"
    changefreq = 'daily'

    def items(self):
        return ['news_list_en']

    def location(self, item):
        return reverse(item)
