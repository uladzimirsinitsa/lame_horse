from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import Http404
from .models import NewsEn, TagNewsEn
from django.shortcuts import redirect


def tags_list(request):
    tags = TagNewsEn.objects.all()
    return render(request, 'news_en/tags_list.html', context={'tags': tags})


class NewsEnListView(ListView):
    model = NewsEn
    template_name = 'news_en/news_list.html'

    def get_queryset(self):
        queryset = super(NewsEnListView, self).get_queryset()
        return queryset.filter(published=True)


class NewsDetailView(DetailView):
    model = NewsEn
    template_name = 'news_en/news_detail.html'

    def get_object(self, queryset=None):
        object = super(NewsDetailView, self).get_object(queryset)
        if object.published:
            return object
        else:
            raise Http404("Пост не найден!")


def tag_detail(request, slug):
    tag = TagNewsEn.objects.get(slug__iexact=slug)

    return render(request, 'news_en/tag_detail.html', context={'tag': tag})


def slash_redirect_slug(request, slug):
    url = request.build_absolute_uri()[:-1]
    return redirect(url, permanent=True, slug=slug)


def slash_redirect(request):
    url = request.build_absolute_uri()[:-1]
    return redirect(url, permanent=True)
