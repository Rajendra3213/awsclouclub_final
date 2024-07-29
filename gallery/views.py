from django.shortcuts import render
from django.views import View
from .models import AWSGallery
# Create your views here.

class GalleryView(View):
    def get(self,request):
        gallerys=AWSGallery.objects.all()
        gallery_list={}
        j=0
        gallery_list[j]=[]
        for i,v in enumerate(gallerys):
            if i!=0 and i%3==0:
                j=j+1
                gallery_list[j]=[]
            gallery_list[j].append([v.title,v.image.url])
        return render(request,'gallery/gallery.html',{"gallerys":gallery_list})