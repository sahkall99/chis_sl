# This file contains all of the forms based on the models

from django.forms import ModelForm
from django import forms
from .models import Appointment, Bed, Doctor, Drug, History, Hospital, Illness, MedicalTest, Official, \
    Patient, Pharmacy, Prescription, Report, Staff, Ward


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True, max_length=200)
    message = forms.CharField(widget=forms.Textarea, required=True)


# This form is based off from the Appointment Model
class NewAppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'


# This form is based off from the Bed Model
class NewBedForm(ModelForm):
    class Meta:
        model = Bed
        fields = '__all__'


# This form is based off from the Doctor Model
class NewDoctorForm(ModelForm):
    class Meta:
        model = Doctor
        exclude = ['user']


# This form is based off from the Drug Model
class NewDrugForm(ModelForm):
    class Meta:
        model = Drug
        fields = '__all__'


# This form is based off from the History Model
class NewHistoryForm(ModelForm):
    class Meta:
        model = History
        fields = '__all__'


# This form is based off from the Hospital Model
class NewHospitalForm(ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'


# This form is based off from the Illness Model
class NewIllnessForm(ModelForm):
    class Meta:
        model = Illness
        fields = '__all__'


# This form is based off from the MedicalTest Model
class NewMedicalTestForm(ModelForm):
    class Meta:
        model = MedicalTest
        fields = '__all__'


# This form is based off from the Official Model
class NewOfficialForm(ModelForm):
    class Meta:
        model = Official
        exclude = ['user']


# This form is based off from the Patient Model
class NewPatientForm(ModelForm):
    class Meta:
        model = Patient
        exclude = ['user']


# This form is based off from the Pharmacy Model
class NewPharmacyForm(ModelForm):
    class Meta:
        model = Pharmacy
        fields = '__all__'


# This form is based off from the Prescription Model
class NewPrescriptionForm(ModelForm):
    class Meta:
        model = Prescription
        fields = '__all__'


# This form is based off from the Report Model
class NewReportForm(ModelForm):
    class Meta:
        model = Report
        fields = '__all__'


# This form is based off from the Staff Model
class NewStaffForm(ModelForm):
    class Meta:
        model = Staff
        exclude = ['user']


# This form is based off from the Ward Model
class NewWardForm(ModelForm):
    class Meta:
        model = Ward
        fields = '__all__'
