from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404 



app_name = 'shop'
handler404 = views.error_404

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^profile/',views.profile, name='profile'),
    url(r'^about/', views.about, name='about'),
    url(r'^notfound/', views.notfound, name='notfound'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^edit/', views.edit, name='edit'),
    url(r'^newsletter/', views.newsletter, name='newsletter'),
    url(r'^shop/', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
  


        ] 




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
