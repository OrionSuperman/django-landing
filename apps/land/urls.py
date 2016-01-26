from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
	url(r'^land/', views.land, name='land'),
	url(r'^$', views.index, name='index'),

	)