from django.shortcuts import render,get_object_or_404
from django.views import View
from .models import AWSBlog
# Create your views here.
class BlogList(View):
    def get(self,request):
        blogs=AWSBlog.objects.all()
        return render(request,'blog/list_of_blogs.html',{'blogs':blogs})
class BlogDetail(View):
    def get(self,request,id):
        blog=get_object_or_404(AWSBlog,id=id)
        return render(request,'blog/blog_detail.html',{'blog':blog})