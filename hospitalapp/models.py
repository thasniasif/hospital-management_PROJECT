from django.db import models
from datetime import date
# Create your models here.
class admin(models.Model):
    first_name=models.CharField(max_length=100,blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    user_name = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)

class doctor(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    specialisation = models.CharField(max_length=100, blank=True)
    mobile = models.CharField(max_length=100, blank=True)
    user_name = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    profile = models.ImageField(upload_to='doc_profile/')
    status= models.CharField(max_length=100, blank=True,default='On Hold')
    join_date=models.DateTimeField('Created', auto_now=True)


class patient(models.Model):

    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    symptom = models.CharField(max_length=100, blank=True)
    mobile = models.CharField(max_length=100, blank=True)
    user_name = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    doc_dep= models.CharField(max_length=100, blank=True)
    profile = models.ImageField(upload_to='doc_profile/')
    status= models.CharField(max_length=100, blank=True,default='On Hold')
    join_date = models.DateTimeField('Created', auto_now=True)
    op_num=models.CharField(max_length=100, blank=True)

class appointment(models.Model):
    doctor_user_name=models.CharField(max_length=200,blank=True)
    patient_user_name=models.CharField(max_length=200,blank=True)
    patient_name=models.CharField(max_length=200,blank=True)
    description=models.CharField(max_length=10000,blank=True)
    doctor_name=models.CharField(max_length=200,blank=True)
    join_date = models.DateTimeField('Created', auto_now=True)

    app_date = models.DateField("Date", default=date.today)
    status = models.CharField(max_length=100, blank=True, default='Processing')
class discharge_tb(models.Model):
    p_id = models.ForeignKey(patient, on_delete=models.CASCADE)
    patient_user_name = models.CharField(max_length=200, blank=True)
    # patient_name = models.CharField(max_length=200, blank=True)
    doctor_user_name = models.CharField(max_length=200, blank=True)

    release_date = models.DateTimeField('Created', auto_now=True)
    room_charge=models.IntegerField(default=0)
    doc_fee= models.IntegerField(default=0)
    medicine_cost = models.IntegerField(default=0)
    other_charge = models.IntegerField(default=0)
    total_charge =models.IntegerField(default=0)
