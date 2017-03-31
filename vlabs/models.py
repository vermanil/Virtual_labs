from django.db import models

class problemSolving_course(models.Model):
    stream = models.TextField()
    introduction = models.TextField()
    # list_of_labs = models.TextField()
    target_audience = models.TextField()
    topic = models.TextField()

class List_of_labs(models.Model):
    list_of_labs = models.TextField()
    Introduction = models.TextField()
    # task = models.TextField()
    objective = models.TextField()

class Task(models.Model):
     labNo = models.ForeignKey(List_of_labs)
     Question = models.TextField()
     input = models.TextField()
     output = models.TextField()
     answer = models.TextField()


# Create your models here.
