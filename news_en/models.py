from __future__ import unicode_literals
import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from myproject.utils import unique_slug_generator
from django.db.models import Q
from django.conf import settings


class NewsEnManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(title__icontains=query) |
                        Q(description__icontains=query) |
                         Q(keywords__icontains=query) |
                        Q(body__icontains=query))
            qs = qs.filter(or_lookup).distinct()    # distinct() is often necessary with Q lookups
        return qs


class TagNewsEn(models.Model):
    title = models.CharField("Тег", max_length=50)
    slug = models.SlugField("url", max_length=100, unique=True)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def get_absolute_url(self):
        return reverse("tag_news_detail_url_en", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class NewsEn(models.Model):
    title = models.CharField(max_length=80, db_index=True)
    keywords = models.CharField(max_length=600, blank=True, default="#")
    slug = models.SlugField("Слаг", max_length=80, unique=True, default=uuid.uuid4)
    body = RichTextUploadingField()
    tags = models.ManyToManyField(TagNewsEn, verbose_name="Теги", blank=True, related_name='news')
    date = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    published = models.BooleanField("Опубликовано", default=True)
    description = models.TextField(max_length=160)
    localization_ru = models.CharField(max_length=100, blank=True, default="#")
    objects = NewsEnManager()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='news_liked_en',
                                        blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail_en', kwargs={
            "slug": self.slug
        }
                       )

    def save(self, *args, **kwargs):
        self.slug = unique_slug_generator(self, self.title)
        super(NewsEn, self).save(*args, **kwargs)

    class Meta:
        ordering = [
            '-date'
        ]


