from django.db import models
from django.utils import timezone

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
    
class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    due_date = models.DateField(blank=True, null=True) 
    
    
    def __str__(self):
        return self.title

