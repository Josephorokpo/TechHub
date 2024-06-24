from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    body = models.TextField()
    thumbnail = models.ImageField(upload_to='blog_thumbnails')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="blogs")
    featured = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name="blogs")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    article = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment by {self.user} on {self.article}'
    
    def children(self):
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        return self.parent is None
    
    def delete_comment(self):
        # Handle deletion logic, including related replies
        self.delete()

    class Meta:
        ordering = ['-created']
    
    
