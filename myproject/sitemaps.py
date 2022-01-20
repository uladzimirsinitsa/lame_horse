from django.contrib import sitemaps
from django.urls import reverse


class MainSitemap(sitemaps.Sitemap):
    priority = 1.0
    protocol = "https"
    changefreq = 'daily'

    def items(self):
        return ['main_en']

    def location(self, item):
        return reverse(item)


