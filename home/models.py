from django.db import models

# Create your models here.


class Project(models.Model):
    tag = models.CharField(max_length=100, default=None)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    project_description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name





