import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_description = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.post_title
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

