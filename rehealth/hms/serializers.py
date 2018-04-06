from rest_framework import serializers
from .models import Doctor, Patient, Appointment, Tips

class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        #fileds = ('','')
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = '__all__'

class TipsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tips
        fields = '__all__'
