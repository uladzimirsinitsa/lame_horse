from django.views.generic.detail import DetailView
from django.views.generic import ListView
from casino_online_en.models import Casino_en
from django.shortcuts import redirect


class CasinoDetailView(DetailView):
    """Вывод страницы"""
    model = Casino_en
    template_name = 'casino_detail_en.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CasinoListView_en(ListView):
    model = Casino_en
    template_name = 'casino/casino_list_en.html'

    def get_queryset(self):
        queryset = super(CasinoListView_en, self).get_queryset()
        return queryset.filter()


def slash_redirect_slug(request, slug):
    url = request.build_absolute_uri()[:-1]
    return redirect(url, permanent=True, slug=slug)


def slash_redirect(request):
    url = request.build_absolute_uri()[:-1]
    return redirect(url, permanent=True)