from django.db import models

class ScrapedData(models.Model):
    title = models.CharField(max_length=200)
    company = models.TextField()
    location = models.TextField()
    description = models.TextField()
    
