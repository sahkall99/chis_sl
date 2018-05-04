# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Appointment, Bed, Drug, History, Hospital, Illness, MedicalTest, Pharmacy, Prescription, \
    Recommendation, Report, Ward, Doctor, Official, Patient, Staff

# Register your models here.


admin.site.register(Appointment)
admin.site.register(Bed)
admin.site.register(Doctor)
admin.site.register(Drug)
admin.site.register(History)
admin.site.register(Hospital)
admin.site.register(Illness)
admin.site.register(MedicalTest)
admin.site.register(Official)
admin.site.register(Patient)
admin.site.register(Pharmacy)
admin.site.register(Prescription)
admin.site.register(Recommendation)
admin.site.register(Report)
admin.site.register(Staff)
admin.site.register(Ward)
