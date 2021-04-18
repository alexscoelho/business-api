from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='')
    ocupation = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.name