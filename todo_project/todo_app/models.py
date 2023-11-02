from django.db import models

# Create your models here.
class task_table(models.Model):
    t_name=models.CharField(max_length=250)
    priority=models.CharField(max_length=250)
    date=models.DateField()
    def __str__(self):
        return self.t_name
