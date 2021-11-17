from django.db import models


class Recipe(models.Model):
    recipe = models.TextField(max_length=100)
    country = models.TextField(max_length=100)
    image = models.TextField(max_length=1000)
    description = models.TextField(max_length=1000)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description[0:50]

    class Meta:
        ordering = ['-updated']
