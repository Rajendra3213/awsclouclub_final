from django.db import models

# Create your models here.
class AWSGallery(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='gallery')

    def __str__(self):
        return f"Galley Image {self.title}"