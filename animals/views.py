from django.shortcuts import render, HttpResponse
import json
from animals.models import CatImage
from django.views.decorators.csrf import csrf_exempt

 

# Create your views here.
def index(request):
	cats = CatImage.objects.all()
	return render(request, 'index.html', locals())

@csrf_exempt
def save_cat(request):
	response = {}
	if request.method == 'POST':
		print('entro post', request.POST, request.GET)
		cat = CatImage.objects.create(image_url=request.GET.get('url'))
		response['message'] = 'Imagen almacenada'
		
	return HttpResponse(json.dumps(response), content_type="application/json")