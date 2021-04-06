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

    def __str__(self):
        return f"user: {self.user} \n \
                date_created: {self.date_created} \n \
                alias: {self.alias} \n \
                status: {self.status} \n\n"
# Sample query of getting Alias from username in User Class
# filter using queryset Aliases.objects.filter(user__username='apratim')
# Serializer for model has been added