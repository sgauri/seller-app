# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Palazzo, Images



class ImagesInline(admin.StackedInline):
	model = Images
	extra = 1

@admin.register(Palazzo)
class PalazzoAdmin(ImportExportModelAdmin):
	list_display = ('sku', 'item_name', 'color', 'qty', 'size', 'image_pal')
	search_fields = ('item_name', 'sku')
	inlines = [ImagesInline]

