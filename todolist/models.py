from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default= False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
