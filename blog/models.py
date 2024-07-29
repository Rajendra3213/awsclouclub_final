from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.
class AWSBlog(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False)
    position=models.CharField(max_length=100,null=False,blank=False)
    date_of_publish=models.DateField(auto_now=True)
    profile=models.ImageField(upload_to='blog_profile',null=False,blank=False)
    blog_image=models.ImageField(upload_to='blog_image',null=False,blank=False)
    title=models.CharField(max_length=200,null=False,blank=False)
    summary=models.TextField(max_length=200,null=False,blank=False)
    detail=CKEditor5Field('Text',config_name='extends')
    read_time=models.IntegerField(default=2,null=False,blank=False)

    def __str__(self):
        return self.name