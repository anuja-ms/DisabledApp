from django.db import models
from AdminApp.models import Tbl_category,Tbl_location

# Create your models here.
class Tbl_login(models.Model):
    loginid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    role = models.CharField(max_length=25)
    status = models.CharField(max_length=25,default='')
class Tbl_institution(models.Model):
    institutionid = models.AutoField(primary_key=True)
    institutionname = models.CharField(max_length=25)
    regnumber = models.CharField(max_length=25)
    contactno = models.BigIntegerField()
    email = models.CharField(max_length=25)
    percentage = models.CharField(max_length=25)
    institutiondesc = models.CharField(max_length=300)
    websiteurl = models.CharField(max_length=25)
    institutionimage = models.ImageField()
    categoryid = models.ForeignKey(Tbl_category,on_delete=models.CASCADE)
    locationid = models.ForeignKey(Tbl_location,on_delete=models.CASCADE)
    loginid = models.ForeignKey(Tbl_login,on_delete=models.CASCADE)
class Tbl_disabledperson(models.Model):
    personid = models.AutoField(primary_key=True)
    personname = models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    contactno = models.BigIntegerField()
    email = models.CharField(max_length=50)
    percentage = models.CharField(max_length=25)
    disabilitydetails = models.CharField(max_length=300)
    pname = models.CharField(max_length=25)
    pcontact = models.BigIntegerField()
    dob = models.DateField()
    idproof = models.ImageField()
    categoryid = models.ForeignKey(Tbl_category,on_delete=models.CASCADE)
    locationid = models.ForeignKey(Tbl_location,on_delete=models.CASCADE)
    loginid = models.ForeignKey(Tbl_login,on_delete=models.CASCADE)




    
