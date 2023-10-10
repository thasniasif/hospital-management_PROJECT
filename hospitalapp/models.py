from django.db import models
from datetime import date
import os
from twilio.rest import Client
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
    pat_id=models.CharField(max_length=100, blank=True)

class appointment(models.Model):

    doctor_user_name=models.CharField(max_length=200,blank=True)
    patient_user_name=models.CharField(max_length=200,blank=True)
    patient_name=models.CharField(max_length=200,blank=True)
    description=models.CharField(max_length=10000,blank=True)
    doctor_name=models.CharField(max_length=200,blank=True)
    join_date = models.DateTimeField('Created', auto_now=True)
    bill_status=models.CharField(max_length=100, blank=True, default='On_Hold')
    app_date = models.DateField("Date", default=date.today)
    status = models.CharField(max_length=100, blank=True, default='Processing')
    pat_id = models.CharField(max_length=100, blank=True)
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

    def save(self, *args, **kwargs):
        if self.total_charge>0:

            account_sid = 'AC73cc8410e7b97d7c9b9b41772959e9e1'
            auth_token = '83836680b8a7fedf6c4c06bd4908a68e'
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                body=f"Hi {self.p_id.first_name} {self.p_id.last_name} You are discharged from the hospital...Your total bill amount is {self.total_charge}",
                from_='+15704378688',
                to='+919747100240'
            )


            print(message.sid)
        return super().save(*args, **kwargs)
