from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from accounts.models import CustomUser
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.

class Program(models.Model):
    title = models.CharField(max_length=300)
    body = RichTextField()
    image = models.ImageField(upload_to='programs/images/')
    video = models.FileField(upload_to='programs/videos/', blank=True)
    document = models.FileField(upload_to='programs/documents/')

    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title + ": " + str(self.videofile)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('programs_detail', args=[str(self.id)])