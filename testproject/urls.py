
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^$', views.hello, name='home'),
	url(r'^flipkart/', include('flipkart.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
	url(r'^photologue/', include('photologue.urls', namespace='photologue')),
]