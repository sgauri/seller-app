# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Palazzo, Images


class ImagesInline(admin.StackedInline):
	model = Images
	extra = 1

class PalazzoAdmin(admin.ModelAdmin):
	list_display = ('sku', 'item_name', 'color', 'qty', 'size', 'image_pal')
	search_fields = ('item_name',)
	inlines = [ImagesInline]


admin.site.register(Palazzo, PalazzoAdmin)