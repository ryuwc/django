from django.db import models


# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=30)
    comment = models.TextField()

    def __str__(self) -> str:
        return f'{self.title}-{self.director}'

