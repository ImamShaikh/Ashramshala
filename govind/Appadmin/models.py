from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=255)
    teach_sub = models.CharField(max_length=200)
    expertise = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    p_no = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name} is add in Database'