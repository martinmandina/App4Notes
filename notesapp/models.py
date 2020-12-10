from django.db import models

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    createdtime = models.DateTimeField(auto_now_add=True)
    modifiedtime = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
