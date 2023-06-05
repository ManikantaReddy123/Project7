from django.db import models

# Create your models here.
class Reg(models.Model):
    FirstName=models.CharField(max_length=20)
    LastName=models.CharField(max_length=20)
    UserName=models.CharField(max_length=20,primary_key=True)
    Password=models.CharField(max_length=8)
    ConfirmPassword=models.CharField(max_length=8)
    EmailId=models.EmailField()
    MobileNo=models.IntegerField()
