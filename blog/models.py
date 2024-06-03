from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    data_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.FloatField(null=True, blank=True)  
    longitude = models.FloatField(null=True, blank=True)  
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

