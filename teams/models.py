from django.db import models


class AWSTeams(models.Model):
    name = models.CharField(max_length=100)
    roles = models.CharField(max_length=200)
    responsibility = models.CharField(max_length=500)
    profile_image = models.ImageField(upload_to='team_image', null=True, blank=True)
    facebook_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)
    github_link = models.URLField(null=True, blank=True)
    class Meta:
        verbose_name='AWS Team'
        verbose_name_plural='AWS Teams'

    def __str__(self):
        return self.name