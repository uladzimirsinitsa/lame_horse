from django import template

from news_en.models import NewsEn

register = template.Library()


@register.inclusion_tag('news-list-main_en.html')
def show_latest_news(count=15):
    latest_news = NewsEn.objects.filter(published=True)[:count]
    context = {'latest_news': latest_news}
    return context


@register.inclusion_tag('news-list-main_en.html')
def show_latest_news_three(count=2):
    latest_news = NewsEn.objects.filter(published=True)[:count]
    context = {'latest_news': latest_news}
    return context
