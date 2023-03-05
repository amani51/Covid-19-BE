from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Record(models.Model):
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    country=models.CharField(max_length=255)
    date = models.DateTimeField()

    def __str__(self):
        return self.country
