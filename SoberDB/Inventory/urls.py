from django.conf.urls import url
from django.urls import path, re_path
from . import views

app_name= 'Inventory'
urlpatterns = [
# ex: domain/inventory
	re_path('^$', views.index, name = 'index2'),
# ex: domain/inventory/search_form
    re_path('^/search_form/$', views.search_form, name = 'search_form'),
# ex: domain/inventory/search_result
    re_path('^/search_result$', views.search_result, name = 'search_result'),
]
