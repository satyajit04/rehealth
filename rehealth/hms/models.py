from django.db import models
from django.contrib.auth.models import Permission, User
#from multiselectfield import MultiSelectField

# Create your models here.

#patient
class Patient(models.Model):

    GENDERS = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    name = models.CharField(max_length=250)
    age = models.IntegerField()
    gender = models.CharField(max_length=20, choices=GENDERS)
    contact = models.CharField(max_length=100)
    address = models.TextField()
    image = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    doctorname = models.CharField(max_length=200)
    doctordegree = models.CharField(max_length=200)
    speciality = models.CharField(max_length=100)
    image = models.FileField()
    hospital = models.CharField(max_length=200)
    workingaddress = models.CharField(max_length=250)
    designation = models.CharField(max_length=100)
    contactno = models.IntegerField()

    def __str__(self):
        return self.doctorname + "-" + self.speciality + "-" + self.hospital

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor)
    patient = models.ForeignKey(Patient)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.doctor.doctorname + ' - ' + self.patient.name + ' - ' + self.date + ' - ' + self.time

class Tips(models.Model):
    type = models.CharField(max_length=50)
    title = models.CharField(max_length=500)
    image = models.FileField(null=True)
    description = models.TextField()

    def __str__(self):
        return self.type + ' - ' + self.title
