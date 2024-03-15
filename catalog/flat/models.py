from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
        title = models.CharField(max_length=250)
        text = models.TextField()
        author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        created_at = models.DateTimeField(default=timezone.now)
        published_at = models.DateTimeField(blank=True, null=True)
        image=models.ImageField(upload_to="images/")

        def __str__(self):
            return self.title

# Create your models here.
