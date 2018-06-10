from Birds.models import Finch
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.template import loader

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from .models import Finch


#domain/
def index(request):
	return render(request, 'Birds/index.html')

#domain/all_unclaimed_males/
class Unc_MaleView(generic.ListView):
	template_name = 'Birds/all_unclaimed_males.html'
	model = Finch
	context_object_name= 'all_birds'
	def get_queryset(self):
		return Finch.objects.all()


def detail(request, pk, **kwargs):
	def get_context_data(self, **kwargs):
		return {"bird": self.get_object()}
	return HttpResponseRedirect(reverse('Birds:birdinfo', kwargs={'pk': birds.pk}))

# #domain/all_unclaimed_males/<BirdID>
# class DetailsView(generic.DetailView):
# 	model = Finch
# 	template_name = 'Birds/details.html'
# 	def get_context_data(self, **kwargs):
# 		return {"bird": self.get_object(),}

class FinchCreate(CreateView):
	model = Finch
	fields = ['BirdID','Location','Procedure','Experimenter','Notes']

class FinchUpdate(UpdateView):
	model = Finch
	fields = ['BirdID','Location','Procedure','Experimenter','Notes']

# def birddetails(request, **kwargs):
# 	if request.method == 'GET':
# 		return render(request, 'Birds/details.html')
# 	if request.method == 'POST':
# 		form = Finch(request.POST)
# 		if form.is_valid():
# 			obj = Finch()
# 			obj.Location = form.cleaned_data['Location']
# 			obj.save()
# 			return HttpResponseRedirect('/')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        birds = Finch.objects.filter(BirdID__icontains=q)
        return render(request, 'Birds/search_result.html',
                      {'birds': birds, 'query': q})
    else:
        return HttpResponse('Please submit a query!')
