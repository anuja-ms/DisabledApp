from django.db import models
from GuestApp.models import Tbl_institution,Tbl_disabledperson
from AdminApp.models import Tbl_equipment,Tbl_scholarship



# Create your models here.
class Tbl_enquiry(models.Model):
    enquiryid = models.AutoField(primary_key=True)
    enquiry = models.CharField(max_length=25)
    institutionid = models.ForeignKey(Tbl_institution,on_delete=models.CASCADE)
    personid = models.ForeignKey(Tbl_disabledperson,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True,null=True)
    status = models.CharField(max_length=25,default='')
class Tbl_request(models.Model):
    requestid = models.AutoField(primary_key=True)
    personid = models.ForeignKey(Tbl_disabledperson,on_delete=models.CASCADE)
    equipmentid = models.ForeignKey(Tbl_equipment,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True,null=True)
    status = models.CharField(max_length=25,default='')
    requesteddate = models.DateField(null=True)
    count=models.IntegerField(null=True)
    totalamount=models.IntegerField(null=True)
class Tbl_payment(models.Model):
    paymentid = models.AutoField(primary_key=True)
    requestid = models.ForeignKey(Tbl_request,on_delete=models.CASCADE)
    paymentdate = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=25)
    amount = models.IntegerField() 
class Tbl_scholarshipreq(models.Model):
    requestid = models.AutoField(primary_key=True)
    personid = models.ForeignKey(Tbl_disabledperson,on_delete=models.CASCADE)
    scholarshipid = models.ForeignKey(Tbl_scholarship,on_delete=models.CASCADE)
    institutionid = models.ForeignKey(Tbl_institution,on_delete=models.CASCADE)
    status = models.CharField(max_length=25,default='')
    course = models.CharField(max_length=25)
    income = models.IntegerField() 
    accountno = models.BigIntegerField() 



   

