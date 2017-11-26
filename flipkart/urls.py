from django.conf.urls import url
from flipkart import views

app_name = 'flipkart'

urlpatterns = [
	url(r'^products/$', views.all_products, name='products'),
	# url(r'^products/(?P<sku_id>[a-z0-9]+)/$', views.product_detail, name='product_detail'),
	url(r'^products/upload/csv/$', views.uploadcsv, name='upload_csv'),
]


# url(r'^upload/$', views.simple_upload),
# url(r'^model-upload/$', views.model_form_upload),