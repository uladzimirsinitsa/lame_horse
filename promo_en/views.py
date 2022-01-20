from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import Http404
from .models import PromoEn, TagPromoEn
from django.shortcuts import redirect

def tags_list(request):
    tags = TagPromoEn.objects.all()
    return render(request, 'promo_en/tag_list.html', context={'tags': tags})


class PromoListViewEn(ListView):
    model = PromoEn
    template_name = 'promo_en/promo_list.html'

    def get_queryset(self):
        queryset = super(PromoListViewEn, self).get_queryset()
        return queryset.filter(published=True)


class PromoDetailView(DetailView):
    model = PromoEn
    template_name = 'promo_en/promo_detail.html'

    def get_object(self, queryset=None):
        object = super(PromoDetailView, self).get_object(queryset)
        if object.published:
            return object
        else:
            raise Http404("404!")


def tag_detail(request, slug):
    tag = TagPromoEn.objects.get(slug__iexact=slug)

    return render(request, 'promo_en/tag_detail.html', context={'tag': tag})


def slash_redirect_slug(request, slug):
    url = request.build_absolute_uri()[:-1]
    return redirect(url, permanent=True, slug=slug)


def slash_redirect(request):
    url = request.build_absolute_uri()[:-1]
    return redirect(url, permanent=True)