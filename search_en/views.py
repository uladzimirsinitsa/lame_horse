from articles_en.models import Article_en
from casino_online_en.models import Casino_en
from news_en.models import NewsEn
from promo_en.models import PromoEn
from django.views.generic import ListView
from itertools import chain
from django.shortcuts import redirect


class SearchViewEn(ListView):
    template_name = 'search/view_en.html'
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            casino_results = Casino_en.objects.search(query)
            blog_results = Article_en.objects.search(query)
            promo_results = PromoEn.objects.search(query)
            news_results = NewsEn.objects.search(query)

            queryset_chain = chain(
                casino_results,
                blog_results,
                promo_results,
                news_results
            )

            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)
            self.count = len(qs)  # since qs is actually a list
            return qs
        return Casino_en.objects.none()  # just an empty queryset as default
