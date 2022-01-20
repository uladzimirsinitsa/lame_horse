import random

from django import template

from promo_en.models import PromoEn

register = template.Library()


@register.inclusion_tag('promo-list-main_en.html')
def show_latest_promo_en():
    latest_promo = PromoEn.objects.filter(published=True, over__iexact='#')[:9]
    context = {'latest_promo': latest_promo}
    return context



@register.inclusion_tag('promo-review-en.html')
def review_promo_betsson():
    latest_promo = PromoEn.objects.filter(published=True,
                                          promo__iexact='betsson',
                                          over__iexact='#')
    context = {'latest_promo': latest_promo}
    return context


@register.inclusion_tag('promo-review-en.html')
def review_promo_betsafe():
    latest_promo = PromoEn.objects.filter(published=True, promo__iexact='betsafe', over__iexact='#')
    context = {'latest_promo': latest_promo}
    return context


@register.inclusion_tag('promo-review-en.html')
def review_promo_wishmaker():
    latest_promo = PromoEn.objects.filter(published=True, promo__iexact='wishmaker', over__iexact='#')
    context = {'latest_promo': latest_promo}
    return context


@register.inclusion_tag('promo-review-en.html')
def review_promo_bitstarz():
    latest_promo = PromoEn.objects.filter(published=True, promo__iexact='bitstarz', over__iexact='#')
    context = {'latest_promo': latest_promo}
    return context


@register.inclusion_tag('promo-review-en.html')
def review_promo_pokerstars():
    latest_promo = PromoEn.objects.filter(published=True, promo__iexact='pokerstars', over__iexact='#')
    context = {'latest_promo': latest_promo}
    return context


@register.inclusion_tag('promo-review-en.html')
def review_promo_william():
    latest_promo = PromoEn.objects.filter(published=True, promo__iexact='william', over__iexact='#')
    context = {'latest_promo': latest_promo}
    return context


@register.inclusion_tag('promo-review-en.html')
def review_promo_snabbis():
    latest_promo = PromoEn.objects.filter(published=True, promo__iexact='snabbis', over__iexact='#')
    context = {'latest_promo': latest_promo}
    return context


@register.inclusion_tag('promo-review-en.html')
def review_promo_energy():
    latest_promo = PromoEn.objects.filter(published=True, promo__iexact='energy', over__iexact='#')
    context = {'latest_promo': latest_promo}
    return context


@register.inclusion_tag('promo-review-en.html')
def review_promo_sportsbet():
    latest_promo = PromoEn.objects.filter(published=True, promo__iexact='sportsbet', over__iexact='#')
    context = {'latest_promo': latest_promo}
    return context
