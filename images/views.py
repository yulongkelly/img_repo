from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings

from .models import Image

def image_create_view(request):
    if request.method == 'POST':
        Image.objects.create(name=request.POST.get('imgName'), upload=request.FILES.get('img'))
    
    return render(request, "image_create.html")

def image_detail_view(request):
    image_name = request.GET.get('imgName')
    if not image_name:
        img = Image.objects.all().order_by('name')
    else:
        img = Image.objects.filter(name=request.GET.get('imgName'))
    context = {
        "media_url": settings.MEDIA_URL,
        "img": img
    }
    return render(request, "image_detail.html", context)

def image_delete_view(request):
     Image.objects.all().delete()
     return HttpResponseRedirect("/")
