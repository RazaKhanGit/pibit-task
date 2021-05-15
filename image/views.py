from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
import pytesseract
from PIL import Image

# Create your views here.
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
def main(request):
    if request.method == 'GET':
        all_image = ImageM.objects.all()
        return render(request, 'home.html', {'all_img': all_image})

def form(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data.get('image')
            new_img = ImageM(
                image = img,
                )
            new_img.title = new_img.image.name
            new_img.save()
            imgFile = Image.open('media/images/'+new_img.title)
            extractedInfo = pytesseract.image_to_string(imgFile)
            new_img.info = extractedInfo

            new_img.save()          
            return redirect('home')
    else:
        form = ImageForm()
    return render(request, 'form.html', {'form' : form})

def edit(request, id):

     

    image = ImageM.objects.get(id=id)
    form = EditForm(request.POST, instance = image, initial = { "title" : image.title,"info" : image.info})

    if form.is_valid():
            title = form.cleaned_data.get('title')
            info = form.cleaned_data.get('info')
            img = ImageM.objects.get(id=id) 
            img.title = title
            img.info = info
            img.save()          
            return redirect('home')
    return render(request,'edit.html', {'form': form, 'img': image})    