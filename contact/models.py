from django.db import models

# Create your models here.
class Contact(models.Model):
    fname = models.CharField()
    lname = models.CharField()
    email = models.EmailField()
    phone = models.CharField()
    message = models.TextField()
    def __str__(self):
        return self.fname