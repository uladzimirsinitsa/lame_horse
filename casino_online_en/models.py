from __future__ import unicode_literals
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.db.models import Q


class CasinoManager(models.Manager):
	def search(self, query=None):
		qs = self.get_queryset()
		if query is not None:
			or_lookup = (Q(title__icontains=query) |
						Q(description__icontains=query) |
						Q(slug__icontains=query) |
						Q(text__icontains=query) |
						Q(text_withdrawal_times__icontains=query) |
						Q(text_withdrawal_limit__icontains=query) |
						Q(text_restricted_countries__icontains=query) |
						Q(text_languages__icontains=query) |
						Q(text_licences__icontains=query) |
						Q(text_contact__icontains=query))
			qs = qs.filter(or_lookup).distinct()# distinct() is often necessary with Q lookups
		return qs


class Casino_en(models.Model):
	alternate_ru = models.CharField(max_length=300, blank=True, default="#")
	alternate_en = models.CharField(max_length=300, blank=True, default="#")
	title_meta = models.CharField(max_length=300, blank=True, default="#")
	canonical = models.CharField(max_length=300, blank=True, default="#")
	description = models.TextField(max_length=250)
	url_affilate = models.CharField(max_length=300, blank=True, default="#")
	logo834100 = models.CharField(max_length=300, blank=True, default="#")
	alt_logo = models.CharField(max_length=300, blank=True, default="#")
	keywords = models.CharField("Ключевые слова", max_length=500)
	title = models.CharField("Заголовок", max_length=160)
	slug = models.SlugField("slug", max_length=160, default="", null=True, blank=True)
	search_img = models.CharField(max_length=300, blank=True, default="#")
	youtube = models.CharField(max_length=300, blank=True, default="#")
	youtube_img = models.CharField(max_length=300, blank=True, default="#")
	youtube_img_alt = models.CharField(max_length=300, blank=True, default="#")
	text = RichTextUploadingField()
	published = models.BooleanField("Опубликовать?", default=True)
	text_website = RichTextUploadingField(null=True, blank=True)
	text_deposit = RichTextUploadingField(null=True, blank=True)
	text_withdrawal_methods = RichTextUploadingField(null=True, blank=True)
	text_withdrawal_times = RichTextUploadingField(null=True, blank=True)
	text_withdrawal_limit = RichTextUploadingField(null=True, blank=True)
	text_restricted_countries = RichTextUploadingField(null=True, blank=True)
	text_languages = RichTextUploadingField(null=True, blank=True)
	text_licences = RichTextUploadingField(null=True, blank=True)
	text_live_chat = RichTextUploadingField(null=True, blank=True)
	text_contact = RichTextUploadingField(null=True, blank=True)
	date_update = models.DateTimeField(auto_now=True)
	objects = CasinoManager()

	class Meta:
		verbose_name = "Обзор"
		verbose_name_plural = "Обзоры"
		ordering = [
			'-date_update'
		]

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('casino_detail_en', kwargs={"slug": self.slug})



