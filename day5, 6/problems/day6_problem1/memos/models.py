from django.db import models

# Create your models here.
class Memo(models.Model):
    summury = models.CharField(max_length=20)
    memo = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.memo}-{self.created_at}'