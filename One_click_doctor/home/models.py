
from django.db import models


# Create your models here.
class Tweet(models.Model):
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    title = models.CharField(max_length=30)
    artical = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name