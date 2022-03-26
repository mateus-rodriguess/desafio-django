from uuid import uuid4
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from apps.account.models import User


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField("Titulo",max_length=120)
    slug = models.SlugField(max_length=200)
    text = models.TextField("Texto",null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return self.title[:20]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.id)
        self.text = self.text.upper()
        super(Post, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse('post:post_detail', args=[self.slug])
    
    