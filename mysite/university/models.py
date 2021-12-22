from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Teacher(models.Model):
    user = models.ManyToManyField(User)
    teacher_name = models.CharField(max_length=70)
    subject = models.CharField(max_length=70)

    def students(self):
        return ",".join([str(p) for p in self.user.all()])

