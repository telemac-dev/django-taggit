from django.db import models
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    tags = TaggableManager()
    
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, max_length=100)

    
    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs): # new
      if not self.slug:
         self.slug = slugify(self.title)
      return super().save(*args, **kwargs)

