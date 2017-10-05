from django.db import models

# Create your models here.


class Upload(models.Model):
    url = models.CharField(max_length=1000)
    pin = models.CharField(max_length=20)


# class PIN(models.Model):
#    url = models.ForeignKey(URL, on_delete=models.CASCADE)
#    pin = models.CharField(max_length=20)
