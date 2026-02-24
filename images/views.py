from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Image
from .forms import ImageForm

def image_list(request):
    images = Image.objects.all().order_by('-uploaded_to')
    context = {'images': images}
    return render(request, 'images/image_list.html', context)

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image uploaded successfully!')
            return redirect('imagelist')
    else:
        form = ImageForm()
    return render(request, 'images/upload_image.html', {'form': form})

def update_image(request,pk):
    image_instance=get_object_or_404(Image,pk=pk)
    
    if request.method==