from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import *
from django.contrib.sitemaps.views import sitemap
from articles_en.sitemaps import ArticleenSitemap, ArticleListEnSitemap
from casino_online_en.sitemaps import CasinoEnSitemap, CasinoListEnSitemap
from promo_en.sitemaps import PromoSitemapEn, PromoListEnSitemap
from news_en.sitemaps import NewsEnSitemap, NewsListEnSitemap
from django.conf.urls.static import static
from myproject.sitemaps import MainSitemap
from django.shortcuts import redirect
from articles_en.views import ArticleListView
from casino_online_en.views import CasinoListView_en
from search_en.views import SearchViewEn
from promo_en.views import PromoListViewEn
from news_en.views import NewsEnListView
from .views import news_create_main_en
from streams.views import streams_main_page


sitemaps = {
        'articles_en': ArticleenSitemap,
        'casino_online_en': CasinoEnSitemap,
        'promo_en': PromoSitemapEn,
        'news_en': NewsEnSitemap,
        'main': MainSitemap,
        'article_list_en': ArticleListEnSitemap,
        'casino_list_en': CasinoListEnSitemap,
        'news_list_en': NewsListEnSitemap,
        'promo_list_en': PromoListEnSitemap,
}


urlpatterns = [
        path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
             name='django.contrib.sitemaps.views.sitemap'),
        path('admin/', admin.site.urls),
        path('account', lambda request: redirect('login', permanent=True)),
        path('account/', include('account.urls')),
        path('', news_create_main_en, name='main_en'),
        path('article', ArticleListView.as_view(), name='article_list_en'),
        path('article/', include('articles_en.urls')),
        path('reviews', CasinoListView_en.as_view(), name='casino_list_en'),
        path('reviews/', include('casino_online_en.urls')),
        path('contact.html', include('contact_en.urls')),
        path('terms-of-use.html', terms_en),
        path('streams/', streams_main_page),
        path('ckeditor/', include('ckeditor_uploader.urls')),
        path('social-auth/', include('social_django.urls', namespace='social')),
        path('search/', SearchViewEn.as_view(), name='search_en'),
        path('about', about_en, name='about_en'),
        path('blog/comments/', include('fluent_comments.urls')),
        path('promotions', PromoListViewEn.as_view(), name='promo_list_en'),
        path('promotions/', include('promo_en.urls')),
        path('gambling-stories', NewsEnListView.as_view(), name='news_list_en'),
        path('gambling-stories/', include('news_en.urls')),
        path('robots.txt', include('robots.urls')),
        path('accounts/profile/', lambda request: redirect('main_en',
                                                           permanent=True)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
