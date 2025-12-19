from django.db import models
from DisabledPersonApp.models import Tbl_enquiry
from GuestApp.models import Tbl_institution
from AdminApp.models import Tbl_equipment




# Create your models here.
class Tbl_schedule(models.Model):
    scheduleid = models.AutoField(primary_key=True)
    scheduledate = models.DateField()
    status = models.CharField(max_length=25,default='')
    enquiryid = models.ForeignKey(Tbl_enquiry,on_delete=models.CASCADE)
class Tbl_request2(models.Model):
    requestid = models.AutoField(primary_key=True)
    institutionid = models.ForeignKey(Tbl_institution,on_delete=models.CASCADE)
    equipmentid = models.ForeignKey(Tbl_equipment,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True,null=True)
    status = models.CharField(max_length=25,default='')
    requesteddate = models.DateField(null=True)
    count=models.IntegerField(null=True)
    totalamount=models.IntegerField(null=True)

class Tbl_payment2(models.Model):
    paymentid = models.AutoField(primary_key=True)
    requestid = models.ForeignKey(Tbl_request2,on_delete=models.CASCADE)
    paymentdate = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=25)
    amount = models.IntegerField() 
class Tbl_jobposting(models.Model):
    jobid = models.AutoField(primary_key=True)
    institutionid = models.ForeignKey(Tbl_institution,on_delete=models.CASCADE)
    jobtitle = models.CharField(max_length=50)
    jobdesc = models.CharField(max_length=100)
    requirments = models.CharField(max_length=100)
    deadline = models.DateField(null=True)
    contactemail = models.CharField(max_length=50)
    jobimage = models.ImageField()





   
