from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class event(models.Model):
    name=models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    event_name=models.CharField(max_length=150)
    date=models.DateTimeField()
    time=models.TimeField(null=True)
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='eventimages')
    is_liked = models.BooleanField(default=False)
#    many to many field This allows you to associate multiple instances of one model with multiple instances of another model. 
    liked_by_users = models.ManyToManyField(User, related_name='liked_events', blank=True)
    
    def __str__(self):
        return self.event_name
    
    
