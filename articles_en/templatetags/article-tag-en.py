import random

from django import template
from articles_en.models import Article_en


register = template.Library()


@register.inclusion_tag('article-list-main-en.html')
def show_latest_articles_en():
    latest_articles = Article_en.objects.filter(published=True)[2:20:1]
    context = {'latest_articles': latest_articles}
    return context


@register.inclusion_tag('latest_four_article_en.html')
def show_four_latest_articles_en(count=2):
    latest_four_articles = Article_en.objects.filter(published=True)[:count]
    context = {'latest_four_articles': latest_four_articles}
    return context



