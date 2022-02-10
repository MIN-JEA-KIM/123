from django.db import models

class login(models.Model):

    id = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=10)
    birth = models.DateTimeField(blank=True, null=True)
    sex = models.CharField(max_length=5)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'login'

# Create your models here.
