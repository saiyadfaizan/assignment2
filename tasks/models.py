from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default= False)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-create_date',)

    def __str__(self):
        return self.title

