from django.db import models

# Create your models here.
class Board(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    content = models.TextField()
    today = models.DateTimeField(auto_now_add=True)
    cnt = models.IntegerField(default=0)
    def __str__(self):
        return self.title