from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import Http404
from articles_en.models import Article_en
from django.shortcuts import redirect


class ArticleListView(ListView):
    model = Article_en
    template_name = 'articles_en/article_list_en.html'

    def get_queryset(self):
        queryset = super(ArticleListView, self).get_queryset()
        return queryset.filter(published=True)


class ArticleDetailView(DetailView):
    model = Article_en
    template_name = 'articles_en/article_detail_en.html'

    def get_object(self, queryset=None):
        object = super(ArticleDetailView, self).get_object(queryset)
        if object.published:
            return object
        else:
            raise Http404("Not found!")


def slash_redirect_slug(request, slug):
    url = request.build_absolute_uri()[:-1]
    return redirect(url, permanent=True, slug=slug)


def slash_redirect(request):
    url = request.build_absolute_uri()[:-1]
    return redirect(url, permanent=True)
