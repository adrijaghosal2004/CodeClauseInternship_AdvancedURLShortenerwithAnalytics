from django.db import models

# Create your models here.
class Short(models.Model):
    originalUrl = models.URLField(max_length=700)
    shortUrl = models.CharField(max_length=100)
    date_and_time = models.DateTimeField()

    def __str__(self):
        return self.originalUrl