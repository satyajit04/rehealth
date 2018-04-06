from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.generic import View
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.db.models import Q
#from .forms import UserForm
from .models import Patient, Doctor, Appointment, Tips
#from apt.models import Appointment
import operator
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PatientSerializer, DoctorSerializer, AppointmentSerializer, TipsSerializer
from rest_framework import status
from rest_framework import renderers

# Create your views here.

def index(request):
    return render(request, 'hms/index.html')

class PatientIndex(APIView):
    def get(self, request: object) -> object:
        patients = Patient.objects.all()
        patientserializer = PatientSerializer(patients, many=True)
        return Response(patientserializer.data, status=status.HTTP_200_OK)

class DoctorIndex(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()
        doctorserializer = DoctorSerializer(doctors, many=True)
        return Response(doctorserializer.data, status=status.HTTP_200_OK)

class AppointmentIndex(APIView):
    def get(self, request):
        appointments = Appointment.objects.all()
        appointmentserializer = AppointmentSerializer(appointments, many=True)
        return Response(appointmentserializer.data, status=status.HTTP_200_OK)

class TipsIndex(APIView):
    def get(self, request):
        tips = Tips.objects.all()
        tipsserializer = TipsSerializer(tips, many=True)
        return Response(tipsserializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        data = request.data

        form = Tipsform(request.POST or None, request.FILES or None)
        tips = form.save(commit=False)

        tips.type = data.get('type')
        tips.title = data.get('title')
        tips.image = data.get('image')
        tips.description = data.get('description')

