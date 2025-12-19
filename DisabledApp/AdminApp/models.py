from django.db import models

# Create your models here.
class Tbl_district(models.Model):
    district_id = models.AutoField(primary_key=True)
    district_name = models.CharField(max_length=25)
class Tbl_location(models.Model):
    locationid = models.AutoField(primary_key=True)
    locationname = models.CharField(max_length=25)
    district_id = models.ForeignKey(Tbl_district,on_delete=models.CASCADE)
class Tbl_category(models.Model):
    categoryid = models.AutoField(primary_key=True)
    categoryname = models.CharField(max_length=25)
    categoryimage = models.ImageField()
    categorydesc = models.CharField(max_length=100)
class Tbl_equipment(models.Model):
    equipmentid = models.AutoField(primary_key=True)
    equipmentname = models.CharField(max_length=25)
    equipmentimage = models.ImageField()
    equipmentdesc = models.CharField(max_length=300)
    equipmentstock = models.IntegerField()
    amount = models.IntegerField(default=0)

class Tbl_scholarship(models.Model):
    scholarshipid = models.AutoField(primary_key=True)
    scholarshipname = models.CharField(max_length=25)
    categoryid = models.ForeignKey(Tbl_category,on_delete=models.CASCADE)
    scholarshipdesc = models.CharField(max_length=300)
    criteria = models.CharField(max_length=300)
    startdate = models.DateField(auto_now_add=True)
    enddate = models.DateField()
    link = models.CharField(max_length=300)







