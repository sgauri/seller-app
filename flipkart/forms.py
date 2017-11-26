from django.forms import ModelForm
from flipkart.models import Palazzo


class PalazzoForm(ModelForm):
	class Meta:
		model = Palazzo
		fields = '__all__'