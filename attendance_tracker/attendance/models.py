from django.db import models
from django.contrib.auth.models import User

class subject(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="user")
    sub_name = models.CharField(max_length=100)
    present=models.IntegerField(default=0)
    absent=models.IntegerField(default=0)
    totalclasses=models.IntegerField(default=0)

    def __str__(self):
        return self.sub_name
    def att_perc(self):
        return self.present/self.totalclasses*100
