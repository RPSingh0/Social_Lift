from django.db import models
# Create your models here.
import datetime
import os


def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)


class Post_data(models.Model):
    email = models.TextField(max_length=191)
    password = models.TextField(max_length=50)
    caption = models.TextField(max_length=500, null=True)
    image = models.ImageField(null=True, blank=True)


class Wisher(models.Model):
    email = models.TextField(max_length=191, null=True, blank=True)
    password = models.TextField(max_length=50, null=True, blank=True)
    remail = models.TextField(max_length=191)
    message = models.TextField(max_length=500)
    number = models.TextField(max_length=50)
