from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    author = models.CharField(max_length=255, null=False, blank=False)
    cover = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name
