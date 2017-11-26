# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Palazzo


class PalazzoAdmin(admin.ModelAdmin):
	list_display = ('sku', 'item_name', 'color', 'qty', 'size', 'image_pal')
	search_fields = ('item_name',)

admin.site.register(Palazzo, PalazzoAdmin)