from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Image
from .forms import ImageForm

def image_list(request):
    images = Image.objects.all().order_by('-uploaded_to')
    context = {'images': images}
    return render(request, 'images/image_list.html', context)
