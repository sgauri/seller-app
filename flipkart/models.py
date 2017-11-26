from __future__ import unicode_literals

from django.db import models

SIZE_CHOICES = (
	("S", "S"),
	("M", "M"),
	("L", "L"),
	("XL", "XL"),
	("XXL", "XXL"),
)

MATERIAL_CHOICES = (
	("Crepe", 'Crepe'),
	("Cotton", 'Cotton'),
	("Rayon", "Rayon"),
	("Silk", "Silk"),
)

COLOR_CHOICES = (('White', 'White'), ("Black", "Black"), ("Green", "Green"), ("Blue", "Blue"),
	('Red', 'Red'), ('Orange', 'Orange'),
)

WEIGHT_UNIT = (
	('kg', 'kg'),
	('gm', 'gm'),
)

class Palazzo(models.Model):
	sku = models.SlugField()
	item_name = models.CharField(max_length=100)
	color = models.CharField(max_length=30, choices = COLOR_CHOICES)
	material = models.CharField(max_length=30, choices = MATERIAL_CHOICES)
	sp = models.IntegerField(verbose_name="Selling Price", default=399)
	mrp = models.IntegerField(verbose_name="MRP", default=899)
	qty = models.PositiveSmallIntegerField(verbose_name="Inventory", default=5)
	description = models.TextField()
	upc = models.CharField(max_length=14, default='0123456789', blank=True)
	weight = models.FloatField(verbose_name="Product Weight", default=0.25)
	weight_unit = models.CharField(max_length=5, choices=WEIGHT_UNIT, default='kg')
	size = models.CharField(max_length=10, choices=SIZE_CHOICES, default='M')
	key_feature1 = models.CharField(max_length=50, default='Wide Leg Pants')
	key_feature2 = models.CharField(max_length=50, default='Single Side Pocket')
	img = models.ImageField(upload_to='palazzo_img', null=True, blank=True, default="/palazzo_img/optimus.jpg")

	def __str__(self):
		return self.item_name

	def image_pal(self):
		return '<a href="{0}"><img src="{0}" height="80" width="80"></a>'.format(self.img.url)
	image_pal.allow_tags = True
	image_pal.short_description = "p-image"
