
from django.conf.urls import include, url
from django.contrib import admin
from plant import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
	url(r'^$', views.index, name = 'index'),
	url(r'^contact/$', views.contact, name = 'contact'),
	url(r'^aboutus/$', views.aboutus, name = 'aboutus'),

	url(r'^herbs/$', views.herbs, name = 'herbs'),
	url(r'^metabolites/$', views.metabolites, name = 'metabolites'),

	#/herbs/123/
	url(r'^herbs/(?P<plant_id>[0-9]+)/$', views.detailherb,name = 'detailherb'),
	url(r'^metabolites/(?P<metabolite_id>[0-9]+)/$', views.detailmetabolite,name = 'detailmetabolite'),
	url(r'^familia/(?P<familia_id>[0-9]+)/$', views.detailfamilia,name = 'detailfamilia'),
	url(r'^genus/(?P<genus_id>[0-9]+)/$', views.detailgenus,name = 'detailgenus'),

	url(r'^table/', include('table.urls')),

	url(r'^search/$', views.search_titles),
]

