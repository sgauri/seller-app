from import_export import resources
from .models import Palazzo

class PalazzoResource(resources.ModelResource):
	class Meta:
		model = Palazzo
		fields = ('sku', 'item_name', 'color', 'material')