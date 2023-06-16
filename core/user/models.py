from django.db import models

# Create your models here.
class userType(models.Model):
    Type=models.CharField(max_length=20,null=False,unique=True)
    def __str__(self):
        return self.Type
class user(models.Model):
    UserName = models.CharField(max_length=50,null=False,unique=True)
    FirstName=  models.CharField(max_length=50,null=False)
    LasttName=  models.CharField(max_length=50,null=False)
    Password=  models.CharField(max_length=250,null=False)
    Group = models.ForeignKey(userType,on_delete=models.CASCADE)
    is_staff = models.BooleanField(default=False)
    CreatedOn = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.UserName