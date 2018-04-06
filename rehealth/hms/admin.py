from django.contrib import admin
from .models import Doctor, Patient, Appointment, Tips

# Register your models here.

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Tips)

