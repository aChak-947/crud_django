from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=200)
    course = models.CharField(max_length=100)
    department = models.CharField(max_length=200)
    batch = models.IntegerField()
    auto_increment_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name


