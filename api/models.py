from django.db import models

# Create your models here.


class message(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    subject = models.CharField(max_length=40)
    write = models.TextField()

    def __str__(self):
        return self.name


class image(models.Model):
    description = models.CharField(max_length=40)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.description
