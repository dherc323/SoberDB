from django.conf.urls import url, include
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Birds'

urlpatterns = [

# ex: domain/
re_path('^$', views.index, name = 'index'),

# ex: domain/search/
re_path(r'^search/$', views.search),

# ex: domain/all_unclaimed_males
re_path(r'^all_unclaimed_males/$', views.Unc_MaleView.as_view(), name = 'all_unclaimed_males'),

# ex: domain/all_unclaimed_males/<pk by regex>/
re_path('all_unclaimed_males/(?P<pk>[a-z]{2}[0-9]{1,3}[a-z]{2}[0-9]{1,3})/', views.detail, name = 'birdinfo'),

# ex: domain/unclaimed_male/add/
re_path('^unclaimed_male/add/$', views.FinchCreate.as_view(), name = 'Finch-add'),

# ex: domain/unclaimed_male/<pk>/
re_path('^unclaimed_male/(?P<pk>[a-z]{2}[0-9]{1,3}[a-z]{2}[0-9]{1,3})/$', views.FinchUpdate.as_view(), name = 'Finch-update'),

]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


# class Unc_MaleView(generic.ListView):
# 	template_name = 'Birds/all_unclaimed_males.html'
# 	def get_queryset(self):
# 		return Finch.objects.all()
#
#  class DetailsView(generic.DetailView):
# 	 model = Finch
# 	 template_name = 'Birds/details.html'
