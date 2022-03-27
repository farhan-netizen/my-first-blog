from django.conf import settings
from django.db import models
from django.urls import translate_url
from django.utils import timezone
from ckeditor.fields import RichTextField


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200, blank=True)
    introduction = models.TextField(blank=True)
    text = models.TextField(blank=True)
    body = RichTextField(blank=True, null=True)
    footnotes = models.CharField(max_length=300, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title