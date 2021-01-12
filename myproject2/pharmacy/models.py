from django.db import models
from datetime import datetime
from datetime import date




class Pharmacy(models.Model):
        pid = models.CharField(max_length=20)
        pname = models.CharField(max_length=100)
        pemail = models.EmailField()
        paddress = models.CharField(max_length=15)
        class Meta:
            db_table = "pharmacy"
      #  def __str__(self):
       #     return self.pname
class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)

  #  def __str__(self):
   #     return self.ename

    class Meta:
        db_table = "employee"

class Tablet(models.Model):
    tid = models.CharField(max_length=20)
    tname =models.CharField(max_length=20)
    tdate =models.DateField()
    tquantity = models.IntegerField(default=0)
    tprice = models.IntegerField(default=0)
    ttprice =models.IntegerField(default=0)

    def yearadded(self):
        return self.tdate.strftime('%Y')
    def monthadded(self):
        return self.tdate.strftime('%b')
    def dayadded(self):
        return self.tdate.strftime('%a')




    class Meta:
         db_table = "tb"







# Create your models here.

