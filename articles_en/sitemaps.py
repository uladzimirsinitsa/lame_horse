from django.contrib.sitemaps import Sitemap
from .models import Article_en
from django.urls import reverse


class ArticleenSitemap(Sitemap):
    priority = 0.9
    protocol = "https"
    changefreq = 'weekly'

    def items(self):
        return Article_en.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.date_update

    def location(self, obj):
        return obj.get_absolute_url()


class ArticleListEnSitemap(Sitemap):
    priority = 0.9
    protocol = "https"
    changefreq = 'weekly'

    def items(self):
        return ['article_list_en']

    def location(self, item):
        return reverse(item)
