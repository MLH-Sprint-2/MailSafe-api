from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Aliases(models.Model):
    alias = models.CharField(max_length=200)
    # auto_now_add = True sets the time when we craeted the object
    date_created = models.DateTimeField(auto_now_add=True)
    # if user deleted the post gets deleted not the other way around
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, default='working')
