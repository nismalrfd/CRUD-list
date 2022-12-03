from django.db import models

# Create your models here.
class Taks(models.Model):
    title = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title
