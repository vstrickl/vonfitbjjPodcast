from django.db import models

# Create your models here.
class FontFamily(models.Model):
    family_name = models.CharField(max_length=200, null=True, blank=True)
    serif_type = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.family_name

class Hero(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    title_font_size = models.CharField(max_length=200, null=True, blank=True)
    title_font_weight = models.CharField(max_length=200, null=True, blank=True)
    sub_title = models.CharField(max_length=200, null=True, blank=True)
    sub_title_font_size = models.CharField(max_length=200, null=True, blank=True)
    header_font = models.ManyToManyField(FontFamily, blank=True, related_name='headers')
    cta = models.TextField(null=True, blank=True)
    general_font = models.ManyToManyField(FontFamily, blank=True, related_name='general')
    general_font_size = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.title} {self.sub_title}"
    
class SocialMenu(models.Model):
    social = models.CharField(max_length=200, null=True, blank=True)
    font_awesome = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.social