from django.db import models

class Site(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"

class Review(models.Model):
    topic = models.TextField()
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='reviews')
    def __str__(self):
        return f"{self.review}"