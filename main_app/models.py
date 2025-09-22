from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class ProjectGroup(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('projectgroup-detail', kwargs={'pk': self.id})
    
class Projects(models.Model):
    name = models.CharField(max_length=100)
    where = models.CharField(max_length=100)
    deadline = models.DateField()
    description = models.TextField()
    
    project_group = models.ForeignKey(ProjectGroup, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} should be completed by {self.deadline}"