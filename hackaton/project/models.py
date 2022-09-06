from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Project'
    def __str__(self):
        return self.title

class Job(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100, default='Job Saagie')
    technologie = models.CharField(max_length=150)
    description = models.TextField()
    status = models.BooleanField()
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title