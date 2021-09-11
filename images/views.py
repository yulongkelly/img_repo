from django.shortcuts import render

from .models import Image

def image_create_view(request):
    if request.method == 'POST':
        Image.objects.create(name=request.POST.get('imgName'), upload=request.POST.get('img'))
        print(Image.objects.all())

    
    return render(request, "image_create.html")