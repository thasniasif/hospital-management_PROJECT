from django.db import models

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
    # p_id = models.ForeignKey(doctor, on_delete=models.CASCADE)
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