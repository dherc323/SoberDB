from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from Inventory.models import Lab_Item

def index(request):
    return render(request, 'Inventory/index.html')

def search_form(request):
    return render(request, 'Inventory/search_form.html')

# def search_result(request):
#     if 'q' in request.GET:
#         message = 'You searched for: %r' % request.GET['q']
#     else:
#         message = 'You submitted an empty form.'
#     return HttpResponse(message)

def search_result(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        item = Lab_Item.objects.all()
        return render(request, 'Inventory/search_result.html',
                      {'item': item, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')
