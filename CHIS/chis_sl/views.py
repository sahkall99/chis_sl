#  # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import StaffuserRequiredMixin, SuperuserRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import Doctor, Patient, Official, Hospital, Pharmacy, Ward, Drug, Illness, Prescription, Bed, Report, \
    Recommendation, Appointment, User, Staff


# A class based list view for listing all of the appointments belonging to a specific doctor
class DoctorAppointmentsList(LoginRequiredMixin, ListView):
    model = models.Appointment
    template_name = 'chis_sl/doctor_appointment_list.html'

    # a queryset that returns all the appointments for a specific doctor
    def get_queryset(self):
        try:
            self.doctor_user = Doctor.objects.prefetch_related('appointment_doctor')\
                .get(username__iexact=self.kwargs.get('username'))
        except Doctor.DoesNotExist:
            raise Http404
        else:
            return self.doctor_user.appointment_doctor.all()


# The view used for updating the details of an Appointment for a specific doctor
class DoctorAppointmentUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = '/edit-doctor-appointment/'
    raise_exception = True
    context_object_name = 'doctor_appointment_update'
    fields = ('date', 'patient')
    model = models.Appointment


# A class based list view for listing all of the recommendations made by a specific doctor
class DoctorRecommendationsListView(LoginRequiredMixin, ListView):
    model = models.Recommendation
    template_name = 'chis_sl/doctor_recommendation_list.html'

    # a queryset that returns all the recommendations made by a specific doctor
    def get_queryset(self):
        try:
            self.doctor_user = Doctor.objects.prefetch_related('recommendation_doctor')\
                .get(username__iexact=self.kwargs.get('username'))
        except Doctor.DoesNotExist:
            raise Http404
        else:
            return self.doctor_user.recommendation_doctor.all()


# The view used for updating the details of a Recommendation for a specific doctor
class DoctorRecommendationUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = '/edit-doctor-recommendation/'
    raise_exception = True
    context_object_name = 'doctor_recommendation_update'
    fields = ('number', 'patient', 'medical_rec', 'date', 'status')
    model = models.Recommendation


# A class based list view for listing all of the medical tests made by a specific doctor
class DoctorMedicalTestsListView(LoginRequiredMixin, ListView):
    model = models.MedicalTest
    template_name = 'chis_sl/doctor_medical_test_list.html'

    # a queryset that returns all the medical tests made by a specific doctor using the related name of the relationship
    def get_queryset(self):
        try:
            self.doctor_user = Doctor.objects.prefetch_related('test_doctor')\
                .get(username__iexact=self.kwargs.get('username'))
        except Doctor.DoesNotExist:
            raise Http404
        else:
            return self.doctor_user.test_doctor.all()


# The view used for updating the details of a Medical Test for a specific doctor
class DoctorMedicalTestUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = '/edit-doctor-medical-test/'
    raise_exception = True
    context_object_name = 'doctor_medical_test_update'
    fields = ('name', 'date', 'unit', 'patient')
    model = models.MedicalTest


# A class based list view for listing all of the medical prescriptions made by a specific doctor
class DoctorPrescriptionsListView(LoginRequiredMixin, ListView):
    model = models.Prescription
    template_name = 'chis_sl/doctor_prescription_list.html'

    # a queryset that returns all the medical prescriptions made by a specific doctor
    # using the related name of the relationship
    def get_queryset(self):
        try:
            self.doctor_user = Doctor.objects.prefetch_related('prescription_doctor')\
                .get(username__iexact=self.kwargs.get('username'))
        except Doctor.DoesNotExist:
            raise Http404
        else:
            return self.doctor_user.prescription_doctor.all()


# The view used for updating the details of a Medical Prescription for a specific doctor
class DoctorPrescriptionUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = '/edit-doctor-prescription-test/'
    raise_exception = True
    context_object_name = 'doctor_prescription_update'
    fields = ('name', 'date', 'drug_dosage', 'doctor', 'illness', 'patient')
    model = models.Prescription


# A class based list view for listing all of the patients seen by a specific doctor
class DoctorPatientsListView(LoginRequiredMixin, ListView):
    model = models.Patient
    template_name = 'chis_sl/doctor_patient_list.html'

    # a queryset that returns all the patients seen by a specific doctor using the related name of the relationship
    def get_queryset(self):
        try:
            self.doctor_user = Doctor.objects.prefetch_related('patient_doctor')\
                .get(username__iexact=self.kwargs.get('username'))
        except Doctor.DoesNotExist:
            raise Http404
        else:
            return self.doctor_user.patient_doctor.all()


# The view used for updating the details of a Medical Patient for a specific doctor
class DoctorPatientUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = '/edit-doctor-patient/'
    raise_exception = True
    context_object_name = 'doctor_patient_update'
    fields = ('first_name', 'middle_name', 'last_name', 'sex', 'date_of_birth', 'address', 'city', 'region',
              'phone_number', 'age', 'blood_type', 'category', 'date_diagnosed', 'admission_date', 'discharge_date',
              'ward')
    model = models.Patient
    success_url = reverse_lazy('chis_sl:patient_list')


# A class based list view for listing all of the appointments belonging to a specific patient
class PatientAppointmentsListView(LoginRequiredMixin, ListView):
    model = models.Appointment
    template_name = 'chis_sl/patient_appointment_list.html'

    # a queryset that returns all the appointments for a specific patient
    def get_queryset(self):
        try:
            self.patient_user = Patient.objects.prefetch_related('appointment_patient')\
                .get(username__iexact=self.kwargs.get('username'))
        except Patient.DoesNotExist:
            raise Http404
        else:
            return self.patient_user.appointment_patient.all()


# A class based list view for listing all of the recommendations belonging to a specific patient
class PatientRecommendationsListView(LoginRequiredMixin, ListView):
    model = models.Recommendation
    template_name = 'chis_sl/patient_recommendation_list.html'

    # a queryset that returns all the recommendations for a specific patient
    def get_queryset(self):
        try:
            self.patient_user = Patient.objects.prefetch_related('recommendation_patient')\
                .get(username__iexact=self.kwargs.get('username'))
        except Patient.DoesNotExist:
            raise Http404
        else:
            return self.patient_user.recommendation_patient.all()


# A class based list view for listing all of the medical tests for a specific patient
class PatientMedicalTestsListView(LoginRequiredMixin, ListView):
    model = models.MedicalTest
    template_name = 'chis_sl/patient_medical_test_list.html'

    # a queryset that returns all the medical tests for a specific patient using the related name of the relationship
    def get_queryset(self):
        try:
            self.patient_user = Patient.objects.prefetch_related('test_patient')\
                .get(username__iexact=self.kwargs.get('username'))
        except Patient.DoesNotExist:
            raise Http404
        else:
            return self.patient_user.test_patient.all()


# A class based list view for listing all of the prescriptions for a specific patient
class PatientPrescriptionsListView(LoginRequiredMixin, ListView):
    model = models.Prescription
    template_name = 'chis_sl/patient_prescription_list.html'

    # a queryset that returns all the prescriptions for a specific patient using the related name of the relationship
    def get_queryset(self):
        try:
            self.patient_user = Patient.objects.prefetch_related('prescription_patient')\
                .get(username__iexact=self.kwargs.get('username'))
        except Patient.DoesNotExist:
            raise Http404
        else:
            return self.patient_user.prescription_patient.all()


# A class based list view for listing all of the medical history for a specific patient
class PatientHistoryListView(LoginRequiredMixin, ListView):
    model = models.History
    template_name = 'chis_sl/patient_histoy_list.html'

    # a queryset that returns all the medical history for a specific patient using the related name of the relationship
    def get_queryset(self):
        try:
            self.patient_user = Patient.objects.prefetch_related('history_patient')\
                .get(username__iexact=self.kwargs.get('username'))
        except Patient.DoesNotExist:
            raise Http404
        else:
            return self.patient_user.history_patient.all()


# A class based list view for listing all of the medical reports for a specific patient
class PatientReportListView(LoginRequiredMixin, ListView):
    model = models.Report
    template_name = 'chis_sl/patient_report_list.html'

    # a queryset that returns all the medical reports for a specific patient using the related name of the relationship
    def get_queryset(self):
        try:
            self.patient_user = Patient.objects.prefetch_related('report_patient')\
                .get(username__iexact=self.kwargs.get('username'))
        except Patient.DoesNotExist:
            raise Http404
        else:
            return self.patient_user.report_patient.all()


#######################################################################################################
#                                   VIEWS FOR APPOINTMENT MODEL                                       #
#######################################################################################################

""" This section contains the following class based views for the Appointment model within the chis_sl app: 
    List View:      for listing all of the data objects found in the Appointment model
    Detail View:    this view presents a detailed information page on each object of the Appointment model 
    Create View:    this view is used for creating a new Appointment object within the Appointment model 
    Update View:    this view allows privileged users to be able to make modifications on the content of an existing 
                    record or object within the Appointment model 
    Delete View:    with the delete view, it allows only users with superuser status to access it. It requires the 
                    highest of privileges because it is used for deleting or removing records from the model. 
"""


# The class based view for listing all Appointments between patients and doctors
class AppointmentListView(ListView):
    context_object_name = 'appointments'
    model = models.Appointment
    select_related = ('doctor', 'patient', 'date')

    def get_queryset(self):     # a query for sorting the details of Appointments by date
        return Appointment.objects.order_by('-date')


# A detailed class based view for the Appointments
class AppointmentDetailView(DetailView):
    context_object_name = 'appointment_detail'
    model = models.Appointment
    template_name = 'chis_sl/appointment_detail.html'


# The view used for creating an Appointment
class AppointmentCreateView(LoginRequiredMixin, StaffuserRequiredMixin, SuccessMessageMixin, CreateView):
    redirect_field_name = '/new-appointment/'
    raise_exception = True
    context_object_name = 'appointment_create'
    fields = ('date', 'doctor', 'patient', 'staff')
    model = models.Appointment
    success_url = reverse_lazy("chis_sl:appointment_list")
    success_message = "Appointment slated for %(date)s successfully added!"


# The view used for updating the details of an Appointment
class AppointmentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    redirect_field_name = '/edit-appointment/'
    raise_exception = True
    context_object_name = 'appointment_update'
    fields = ('date', 'doctor', 'patient', 'staff')
    model = models.Appointment
    success_url = reverse_lazy("chis_sl:appointment_list")
    success_message = "Appointment slated for %(date)s successfully updated!"


# The view used for deleting a specific Appointment from the chis_sl app
class AppointmentDeleteView(LoginRequiredMixin, SuperuserRequiredMixin, SuccessMessageMixin, DeleteView):
    redirect_field_name = '/remove-appointment/'
    raise_exception = True
    context_object_name = 'appointment_delete'
    model = models.Appointment
    # redirects to the appointment list after deleting an appointment
    success_url = reverse_lazy("chis_sl:appointment_list")
    success_message = "Appointment on %(date)s successfully removed!"

    # a delete function for displaying success messages to the user
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(AppointmentDeleteView, self).delete(request, *args, **kwargs)


#######################################################################################################
#                                   VIEWS FOR BED MODEL                                               #
#######################################################################################################

""" This section contains the following class based views for the Bed model within the chis_sl app: 
    List View:      for listing all of the data objects found in the Bed model
    Detail View:    this view presents a detailed information page on each object of the Bed model 
    Create View:    this view is used for creating a new Bed object within the Bed model 
    Update View:    this view allows privileged users to be able to make modifications on the content of an existing 
                    record or object within the Bed model 
    Delete View:    with the delete view, it allows only users with superuser status to access it. It requires the 
                    highest of privileges because it is used for deleting or removing records from the model. 
"""


# The class based view for listing Beds in a ward within the hospital
class BedListView(ListView):
    context_object_name = 'beds'
    model = models.Bed

    def get_queryset(self):     # a query for sorting the beds based on their status
        return Bed.objects.order_by('status')


# A detailed class based view for Beds
class BedDetailView(DetailView):
    context_object_name = 'bed_detail'
    model = models.Bed
    template_name = 'chis_sl/bed_detail.html'


# The view used for creating a Bed
class BedCreateView(LoginRequiredMixin, StaffuserRequiredMixin, SuccessMessageMixin, CreateView):
    redirect_field_name = '/new-bed/'
    raise_exception = True
    context_object_name = 'bed_create'
    fields = ('name', 'status', 'assigned_patient', 'contained_ward')
    model = models.Bed
    success_url = reverse_lazy("chis_sl:bed_list")
    success_message = "%(name)s successfully added!"


# The view used for updating the details of a Bed
class BedUpdateView(LoginRequiredMixin, StaffuserRequiredMixin, SuccessMessageMixin, UpdateView):
    redirect_field_name = '/edit-bed/'
    raise_exception = True
    context_object_name = 'bed_update'
    fields = ('name', 'status', 'assigned_patient', 'contained_ward')
    model = models.Bed
    success_url = reverse_lazy("chis_sl:bed_list")
    success_message = "%(name)s successfully updated!"


# The view used for deleting a specific Bed from the chis_sl app
class BedDeleteView(LoginRequiredMixin, SuperuserRequiredMixin, SuccessMessageMixin, DeleteView):
    redirect_field_name = '/remove-bed/'
    raise_exception = True
    context_object_name = 'bed_delete'
    model = models.Bed
    # redirects to the bed list after deleting a ward
    success_url = reverse_lazy("chis_sl:bed_list")
    success_message = "%(name)s successfully removed!"

    # a delete function for displaying success messages to the user
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(BedDeleteView, self).delete(request, *args, **kwargs)


#######################################################################################################
#                                   VIEWS FOR DOCTOR MODEL                                            #
#######################################################################################################

""" This section contains the following class based views for the Doctor model within the chis_sl app: 
    List View:      for listing all of the data objects found in the Doctor model
    Detail View:    this view presents a detailed information page on each object of the Doctor model 
    Create View:    this view is used for creating a new Doctor object within the Doctor model 
    Update View:    this view allows privileged users to be able to make modifications on the content of an existing 
                    record or object within the Doctor model 
    Delete View:    with the delete view, it allows only users with superuser status to access it. It requires the 
                    highest of privileges because it is used for deleting or removing records from the model. 
"""


# A class based view for listing all the registered Doctors
class DoctorListView(ListView):
    context_object_name = 'doctors'
    model = models.Doctor

    # a method for using the username of the doctor as a parameter to the url mapping instead of pk or <slug>
    # this method helps with displaying user profile info for different username objects
    def get_object(self):
        object = get_object_or_404(Doctor, username=self.kwargs['username'])
        return object

    def get_queryset(self):     # a query for sorting the names of doctors alphabetically.
        return Doctor.objects.order_by('first_name', 'last_name')


# A detailed class based view for Doctors
class DoctorDetailView(DetailView):
    context_object_name = 'doctor_detail'
    model = models.Doctor
    template_name = 'chis_sl/doctor_detail.html'

    # a method for using the username of the doctor as a parameter to the url mapping instead of pk or <slug>
    # this method helps with displaying user profile info for different username objects
    def get_object(self):
        object = get_object_or_404(Doctor, username=self.kwargs['username'])
        return object


# The view used for creating a Medical Doctor
class DoctorCreateView(SuccessMessageMixin, CreateView):
    context_object_name = 'doctor_create'
    model = models.Doctor
    fields = ('first_name', 'middle_name', 'last_name', 'username', 'email', 'sex', 'date_of_birth', 'address', 'city',
              'region', 'phone_number', 'qualification', 'speciality', 'category', 'work_experience', 'photo',
              'hospital')
    success_url = reverse_lazy("chis_sl:doctor_list")
    success_message = "Dr. %(first_name)s %(middle_name)s %(last_name)s successfully added! Your login details will be " \
                      "sent to %(email)s shortly."


# The view used for updating the details of a Medical Doctor
class DoctorUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = '/edit-doctor/'
    raise_exception = True
    context_object_name = 'doctor_update'
    model = models.Doctor
    fields = ('first_name', 'middle_name', 'last_name', 'username', 'email', 'sex', 'date_of_birth', 'address', 'city',
              'region', 'phone_number', 'qualification', 'speciality', 'category', 'work_experience', 'photo',
              'hospital')
    success_url = reverse_lazy('home')

    # a method for using the username of the doctor as a parameter to the url mapping instead of pk or <slug>
    # this method helps with displaying user profile info for different username objects
    def get_object(self):
        object = get_object_or_404(Doctor, username=self.kwargs['username'])
        return object


# The view used for deleting a specific Medical Doctor from the chis_sl app
class DoctorDeleteView(LoginRequiredMixin, SuperuserRequiredMixin, SuccessMessageMixin, DeleteView):
    redirect_field_name = '/remove-doctor/'
    raise_exception = True
    context_object_name = 'doctor_delete'
    model = models.Doctor
    # redirects to the doctor list after deleting a doctor
    success_url = reverse_lazy("chis_sl:doctor_list")
    success_message = "Dr. %(first_name)s %(middle_name)s %(last_name)s successfully removed!"

    # a method for using the username of the doctor as a parameter to the url mapping instead of pk or <slug>
    # this method helps with displaying user profile info for different username objects
    def get_object(self):
        object = get_object_or_404(Doctor, username=self.kwargs['username'])
        return object

    # a delete function for displaying success messages to the user
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(DoctorDeleteView, self).delete(request, *args, **kwargs)


#######################################################################################################
#                                   VIEWS FOR DRUG MODEL                                              #
#######################################################################################################

""" This section contains the following class based views for the Drug model within the chis_sl app: 
    List View:      for listing all of the data objects found in the Drug model
    Detail View:    this view presents a detailed information page on each object of the Drug model 
    Create View:    this view is used for creating a new Drug object within the Drug model 
    Update View:    this view allows privileged users to be able to make modifications on the content of an existing 
                    record or object within the Drug model 
    Delete View:    with the delete view, it allows only users with superuser status to access it. It requires the 
                    highest of privileges because it is used for deleting or removing records from the model. 
"""


# The class based view for listing all of the Drugs in a pharmacy
class DrugListView(ListView):
    context_object_name = 'drugs'
    model = models.Drug

    def get_queryset(self):     # a query for sorting the names of drugs alphabetically
        return Drug.objects.order_by('name')


# A detailed class based view for the drugs in a pharmacy
class DrugDetailView(DetailView):
    context_object_name = 'drug_detail'
    model = models.Drug
    template_name = 'chis_sl/drug_detail.html'


# The view used for creating a Drug
class DrugCreateView(LoginRequiredMixin, StaffuserRequiredMixin, SuccessMessageMixin, CreateView):
    redirect_field_name = '/new-drug/'
    raise_exception = True
    context_object_name = 'drug_create'
    fields = ('name', 'type', 'description', 'quantity', 'manufacture_date', 'expiry_date', 'patient', 'pharmacy',
              'prescription')
    model = models.Drug
    success_url = reverse_lazy("chis_sl:drug_list")
    success_message = "%(name)s successfully added!"


# The view used for updating the details of a drug
class DrugUpdateView(LoginRequiredMixin, StaffuserRequiredMixin, UpdateView):
    redirect_field_name = '/edit-drug/'
    raise_exception = True
    context_object_name = 'drug_update'
    fields = ('name', 'type', 'description', 'quantity', 'manufacture_date', 'expiry_date', 'patient', 'pharmacy',
              'prescription')
    model = models.Drug


# The view used for deleting a specific Drug from the chis_sl app
class DrugDeleteView(LoginRequiredMixin, SuperuserRequiredMixin, SuccessMessageMixin, DeleteView):
    redirect_field_name = '/remove-drug/'
    raise_exception = True
    context_object_name = 'drug_delete'
    model = models.Drug
    # redirects to the drug list after deleting a drug
    success_url = reverse_lazy("chis_sl:drug_list")
    success_message = "%(name)s successfully removed!"

    # a delete function for displaying success messages to the user
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(DrugDeleteView, self).delete(request, *args, **kwargs)


#######################################################################################################
#                                   VIEWS FOR MEDICAL HISTORY MODEL                                   #
#######################################################################################################

""" This section contains the following class based views for the History model within the chis_sl app: 
    List View:      for listing all of the data objects found in the History model
    Detail View:    this view presents a detailed information page on each object of the History model 
    Create View:    this view is used for creating a new History object within the History model 
    Update View:    this view allows privileged users to be able to make modifications on the content of an existing 
                    record or object within the History model 
    Delete View:    with the delete view, it allows only users with superuser status to access it. It requires the 
                    highest of privileges because it is used for deleting or removing records from the model. 
"""


# The class based view for listing patients' medical History
class HistoryListView(ListView):
    context_object_name = 'histories'
    model = models.History


# A detailed class based view for patients' medical History
class HistoryDetailView(DetailView):
    context_object_name = 'history_detail'
    model = models.History
    template_name = 'chis_sl/history_detail.html'


# The view used for creating a Medical History
class HistoryCreateView(LoginRequiredMixin, StaffuserRequiredMixin, SuccessMessageMixin, CreateView):
    redirect_field_name = '/new-history/'
    raise_exception = True
    context_object_name = 'history_create'
    fields = ('number', 'description', 'appointment', 'doctor', 'illness', 'patient', 'prescription')
    model = models.History
    success_url = reverse_lazy("chis_sl:history_list")
    success_message = "The Medical History %(number)s successfully added!"


# The view used for updating the details of a Medical History
class HistoryUpdateView(LoginRequiredMixin, StaffuserRequiredMixin, UpdateView):
    redirect_field_name = '/edit-history/'
    raise_exception = True
    context_object_name = 'history_update'
    fields = ('number', 'description', 'appointment', 'doctor', 'illness', 'patient', 'prescription')
    model = models.History


# The view used for deleting a specific Medical History from the chis_sl app
class HistoryDeleteView(LoginRequiredMixin, SuperuserRequiredMixin, SuccessMessageMixin, DeleteView):
    redirect_field_name = '/remove-history/'
    raise_exception = True
    context_object_name = 'history_delete'
    model = models.History
    # redirects to the history list after deleting a Medical History
    success_url = reverse_lazy("chis_sl:history_list")
    success_message = "The Medical History %(number)s successfully removed!"

    # a delete function for displaying success messages to the user
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(HistoryDeleteView, self).delete(request, *args, **kwargs)


#######################################################################################################
#                                   VIEWS FOR HOSPITAL MODEL                                          #
#######################################################################################################

""" This section contains the following class based views for the Hospital model within the chis_sl app: 
    List View:      for listing all of the data objects found in the Hospital model
    Detail View:    this view presents a detailed information page on each object of the Hospital model 
    Create View:    this view is used for creating a new Hospital object within the Hospital model 
    Update View:    this view allows privileged users to be able to make modifications on the content of an existing 
                    record or object within the Hospital model 
    Delete View:    with the delete view, it allows only users with superuser status to access it. It requires the 
                    highest of privileges because it is used for deleting or removing records from the model. 
"""


# The class based view for listing all registered Hospitals
class HospitalListView(ListView):
    context_object_name = 'hospitals'
    model = models.Hospital

    def get_queryset(self):     # a query for sorting the names of hospitals alphabetically
        return Hospital.objects.order_by('name')


# a detailed class based view for hospitals
class HospitalDetailView(DetailView):
    context_object_name = 'hospital_detail'
    model = models.Hospital
    template_name = 'chis_sl/hospital_detail.html'


# The view used for creating Hospitals
class HospitalCreateView(LoginRequiredMixin, SuperuserRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = '/chis_sl/user_login/'
    redirect_field_name = '/new-hospital/'
    # raise_exception = True
    context_object_name = 'hospital_create'
    fields = ('name', 'address', 'region', 'city', 'email', 'phone_number', 'photo')
    model = models.Hospital
    success_url = reverse_lazy("chis_sl:hospital_list")
    success_message = "%(name)s successfully added!"


# The view used for updating the details of an hospital
class HospitalUpdateView(LoginRequiredMixin, SuperuserRequiredMixin, UpdateView):
    redirect_field_name = '/edit-hospital/'
    raise_exception = True
    context_object_name = 'hospital_update'
    fields = ('name', 'address', 'region', 'city', 'email', 'phone_number', 'photo')
    model = models.Hospital


# The view used for deleting a specific Hospital from the chis_sl app
class HospitalDeleteView(LoginRequiredMixin, SuperuserRequiredMixin, SuccessMessageMixin, DeleteView):
    redirect_field_name = '/remove-hospital/'
    raise_exception = True
    context_object_name = 'hospital_delete'
    model = models.Hospital
    success_url = reverse_lazy("chis_sl:hospital_list")  # redirects to the hospital list after deleting an hospital
    success_message = "%(name)s successfully removed!"

    # a delete function for displaying success messages to the user
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(HospitalDeleteView, self).delete(request, *args, **kwargs)


#######################################################################################################
#                                   VIEWS FOR ILLNESS MODEL                                           #
#######################################################################################################

""" This section contains the following class based views for the Illness model within the chis_sl app: 
    List View:      for listing all of the data objects found in the Illness model
    Detail View:    this view presents a detailed information page on each object of the Illness model 
    Create View:    this view is used for creating a new Illness object within the Illness model 
    Update View:    this view allows privileged users to be able to make modifications on the content of an existing 
                    record or object within the Illness model 
    Delete View:    with the delete view, it allows only users with superuser status to access it. It requires the 
                    highest of privileges because it is used for deleting or removing records from the model. 
"""


# The class based view for listing Illnesses affecting patients
class IllnessListView(ListView):
    context_object_name = 'illnesses'
    model = models.Illness

    def get_queryset(self):     # a query for sorting the names of Illnesses alphabetically
        return Illness.objects.order_by('name')


# A detailed class based view for Illnesses
class IllnessDetailView(DetailView):
    context_object_name = 'illness_detail'
    model = models.Illness
    template_name = 'chis_sl/illness_detail.html'


# The view used for creating an Illness
class IllnessCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    redirect_field_name = '/new-illness/'
    raise_exception = True
    context_object_name = 'illness_create'
    fields = ('name', 'type', 'patient')
    model = models.Illness
    success_url = reverse_lazy("chis_sl:illness_list")
    success_message = "%(name)s successfully added!"


# The view used for updating the details of an Illness
class IllnessUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = '/edit-illness/'
    raise_exception = True
    context_object_name = 'illness_update'
    fields = ('name', 'type')
    model = models.Illness


# The view used for deleting a specific Illness from the chis_sl app
class IllnessDeleteView(LoginRequiredMixin, SuperuserRequiredMixin, SuccessMessageMixin, DeleteView):
    redirect_field_name = '/remove-illness/'
    raise_exception = True
    context_object_name = 'illness_delete'
    model = models.Illness
    # redirects to the illness list after deleting a drug
    success_url = reverse_lazy("chis_sl:illness_list")
    success_message = "%(name)s successfully removed!"

    # a delete function for displaying success messages to the user
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(IllnessDeleteView, self).delete(request, *args, **kwargs)


#######################################################################################################
#                                   VIEWS FOR MEDICAL TEST MODEL                                      #
#######################################################################################################
""" This section contains the following class based views for the MedicalTest model within the chis_sl app: 
    List View:      for listing all of the data objects found in the MedicalTest model
    Detail View:    this view presents a detailed information page on each object of the MedicalTest model 
    Create View:    this view is used for creating a new MedicalTest object within the MedicalTest model 
    Update View:    this view allows privileged users to be able to make modifications on the content of an existing 
                    record or object within the MedicalTest model 
    Delete View:    with the delete view, it allows only users with superuser status to access it. It requires the 
                    highest of privileges because it is used for deleting or removing records from the model. 
"""


# The class based view for listing patients' MedicalTest
class MedicalTestListView(ListView):
    context_object_name = 'medical_tests'
    model = models.MedicalTest


# A detailed class based view for presenting patients' MedicalTest
class MedicalTestDetailView(DetailView):
    context_object_name = 'medical_detail'
    model = models.MedicalTest
    template_name = 'chis_sl/medicaltest_detail.html'


# The view used for creating a MedicalTest
class MedicalTestCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    redirect_field_name = '/new-medical/'
    raise_exception = True
    context_object_name = 'medical_create'
    fields = ('name', 'date', 'unit', 'doctor', 'patient')
    model = models.MedicalTest
    success_url = reverse_lazy("chis_sl:medical_list")
    success_message = "The Medical Test %(name)s successfully added!"


# The view used for updating the details of a MedicalTest
class MedicalTestUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = '/edit-medical/'
    raise_exception = True
    context_object_name = 'medical_update'
    fields = ('name', 'date', 'unit', 'doctor', 'patient')
    model = models.MedicalTest


# The view used for deleting a specific MedicalTest from the chis_sl app
class MedicalTestDeleteView(LoginRequiredMixin, SuperuserRequiredMixin, SuccessMessageMixin, DeleteView):
    redirect_field_name = '/remove-medical/'
    raise_exception = True
    context_object_name = 'medical_delete'
    model = models.MedicalTest
    # redirects to the medical test list after deleting a Medical Test
    success_url = reverse_lazy("chis_sl:medical_list")
    success_message = "The Medical Test %(name)s successfully removed!"

    # a delete function for displaying success messages to the user
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(MedicalTestDeleteView, self).delete(request, *args, **kwargs)


#######################################################################################################
#                                   VIEWS FOR OFFICIAL MODEL                                          #
#######################################################################################################
""" This section contains the following class based views for the Official model within the chis_sl app: 
    List View:      for listing all of the data objects found in the Official model
    Detail View:    this view presents a detailed information page on each object of the Official model 
    Create View:    this view is used for creating a new Official object within the Official model 
    Update View:    this view allows privileged users to be able to make modifications on the content of an existing 
                    record or object within the Official model 
    Delete View:    with the delete view, it allows only users with superuser status to access it. It requires the 
                    highest of privileges because it is used for deleting or removing records from the model. 
"""


# The class based view for listing all of the registered Officials
class OfficialListView(ListView):
    context_object_name = 'officials'
    model = models.Official

    def get_queryset(self):     # a query for sorting the names of officials alphabetically
        return Official.objects.order_by('first_name', 'last_name')


# A detailed class based view for the registered Officials
class OfficialDetailView(DetailView):
    context_object_name = 'official_detail'
    model = models.Official
    template_name = 'chis_sl/official_detail.html'

    # a method for using the username of the official as a parameter to the url mapping instead of pk or <slug>
    # this method helps with displaying user profile info for different username objects within the official model
    def get_object(self):
        object = get_object_or_404(Official, username=self.kwargs['username'])
        return object


# The view used for creating an Official
class OfficialCreateView(SuccessMessageMixin, CreateView):
    context_object_name = 'official_create'
    model = models.Official
    fields = ('first_name', 'middle_name', 'last_name', 'sex', 'date_of_birth', 'address', 'city', 'region', 'email',
              'username', 'phone_number', 'photo', 'unit')
    success_url = reverse_lazy("chis_sl:official_list")
    success_message = "Official %(first_name)s %(middle_name)s %(last_name)s successfully added! Your login details " \
                      "will be sent to %(email)s shortly."


# The view used for updating the details of an Official
class OfficialUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = '/edit-official/'
    raise_exception = True
    context_object_name = 'official_update'
    model = models.Official
    fields = ('first_name', 'middle_name', 'last_name', 'sex', 'date_of_birth', 'address', 'city', 'region', 'email',
              'username', 'phone_number', 'photo', 'unit')
    success_url = reverse_lazy("home")

    # a method for using the username of the official as a parameter to the url mapping instead of pk or <slug>
    # this method helps with displaying user profile info for different username objects within the official model
    def get_object(self):
        object = get_object_or_404(Official, username=self.kwargs['username'])
        return object


# The view used for deleting a specific Official from the chis_sl app
class OfficialDeleteView(LoginRequiredMixin, SuperuserRequiredMixin, SuccessMessageMixin, DeleteView):
    redirect_field_name = '/remove-official/'
    raise_exception = True
    context_object_name = 'official_delete'
    model = models.Official
    # redirects to the official list after deleting an official
    success_url = reverse_lazy("chis_sl:official_list")
    success_message = "Official %(first_name)s %(middle_name)s %(last_name)s successfully removed!"

    # a method for using the username of the official as a parameter to the url mapping instead of pk or <slug>
    # this method helps with displaying user profile info for different username objects within the official model
    def get_object(self):
        object = get_object_or_404(Official, username=self.kwargs['username'])
        return object

    # a delete function for displaying success messages to the user
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(OfficialDeleteView, self).delete(request, *args, **kwargs)


#######################################################################################################
#                                   VIEWS FOR PATIENT MODEL                                           #
#######################################################################################################
""" This section contains the following class based views for the Patient model within the chis_sl app: 
    List View:      for listing all of the data objects found in the Patient model
    Detail View:    this view presents a detailed information page on each object of the Patient model 
    Create View:    this view is used for creating a new Patient object within the Patient model 
    Update View:    this view allows privileged users to be able to make modifications on the content of an existing 
                    record or object within the Patient model 
    Delete View:    with the delete view, it allows only users with superuser status to access it. It requires the 
                    highest of privileges because it is used for deleting or removing records from the model. 
"""


# The class based view for listing all the registered Patients from various hospitals
class PatientListView(ListView):
    context_object_name = 'patients'
    model = models.Patient

    def get_queryset(self):     # a query for sorting the names of patients alphabetically
        return Patient.objects.order_by('first_name', 'last_name')


# A detailed class based view for Patients
class PatientDetailView(DetailView):
    context_object_name = 'patient_detail'
    model = models.Patient
    template_name = 'chis_sl/patient_detail.html'

    # a method for using the username of the patient as a parameter to the url mapping instead of pk or <slug>
    # this method helps with displaying user profile info for different username objects within the patient model
    def get_object(self):
        object = get_object_or_404(Patient, username=self.kwargs['username'])
        return object


# The view used for creating a Medical Patient
class PatientCreateView(LoginRequiredMixin, StaffuserRequiredMixin, SuccessMessageMixin, CreateView):
    context_object_name = 'patient_create'
    model = models.Patient
    fields = ('first_name', 'middle_name', 'last_name', 'sex', 'date_of_birth', 'address', 'city', 'region', 'age',
              'phone_number', 'blood_type', 'category', 'email', 'username', 'photo', 'date_diagnosed',
              'admission_date', 'discharge_date', 'doctor', 'hospital', 'ward')
    success_url = reverse_lazy("chis_sl:patient_list")
    success_message = "Patient %(first_name)s %(middle_name)s %(last_name)s successfully added! Your login details " \
                      "will be sent to %(email)s shortly."


# The view used for updating the details of a Medical Patient
class PatientUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = '/edit-patient/'
    raise_exception = True
    context_object_name = 'patient_update'
    model = models.Patient
    fields = ('first_name', 'middle_name', 'last_name', 'sex', 'date_of_birth', 'address', 'city', 'region', 'age',
              'phone_number', 'blood_type', 'category', 'email', 'username', 'photo', 'date_diagnosed',
              'admission_date', 'discharge_date', 'doctor', 'hospital', 'ward')
    success_url = reverse_lazy("home")

    # a method for using the username of the patient as a parameter to the url mapping instead of pk or <slug>
    # this method helps with displaying user profile info for different username objects within the patient model
    def get_object(self):
        object = get_object_or_404(Patient, username=self.kwargs['username'])
        return object


# The view used for updating the profile details of a Medical Patient
class PatientProfileUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = '/edit-patient-profile/'
    raise_exception = True
    context_object_name = 'patient_profile_update'
    model = models.Patient
    fields = ('first_name', 'middle_name', 'last_name', 'date_of_birth', 'address', 'phone_number',
              'email', 'age', 'username', 'region', 'city', 'photo')
    success_url = reverse_lazy("home")

    # a method for using the username of the patient as a parameter to the url mapping instead of pk or <slug>
    # this method helps with displaying user profile info for different username objects within the patient model
    def get_object(self):
        object = get_object_or_404(Patient, username=self.kwargs['username'])
        return object


# The view used for deleting a specific Medical Patient from the chis_sl app
class PatientDeleteView(LoginRequiredMixin, SuperuserRequiredMixin, SuccessMessageMixin, DeleteView):
    redirect_field_name = '/remove-patient/'
    raise_exception = True
    context_object_name = 'patient_delete'
    model = models.Patient
    # redirects to the patient list after deleting a patient
    success_url = reverse_lazy("chis_sl:patient_list")
    success_message = "Patient %(first_name)s %(middle_name)s %(last_name)s successfully removed!"

    # a method for using the username of the patient as a parameter to the url mapping instead of pk or <slug>
    # this method helps with displaying user profile info for different username objects within the patient model
    def get_object(self):
        object = get_object_or_404(Patient, username=self.kwargs['username'])
        return object

    # a delete function for displaying success messages to the user
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(PatientDeleteView, self).delete(request, *args, **kwargs)


#######################################################################################################
#                                   VIEWS FOR PHARMACY MODEL                                          #
#######################################################################################################
""" This section contains the following class based views for the Pharmacy model within the chis_sl app: 
    List View:      for listing all of the data objects found in the Pharmacy model
    Detail View:    this view presents a detailed information page on each object of the Pharmacy model 
    Create View:    this view is used for creating a new Pharmacy object within the Pharmacy model 
    Update View:    this view allows privileged users to be able to make modifications on the content of an existing 
                    record or object within the Pharmacy model 
    Delete View:    with the delete view, it allows only users with superuser status to access it. It requires the 
                    highest of privileges because it is used for deleting or removing records from the model. 
"""


# The class based view for listing all of the registered Pharmacies
class PharmacyListView(ListView):
    context_object_name = 'pharmacies'
    model = models.Pharmacy

    def get_queryset(self):     # a query for sorting the names of pharmacies alphabetically
        return Pharmacy.objects.order_by('name')


# A detailed class based view for registered Pharmacies
class PharmacyDetailView(DetailView):
    context_object_name = 'pharmacy_detail'
    model = models.Pharmacy
    template_name = 'chis_sl/pharmacy_detail.html'


# The view used for creating a Pharmacy
class PharmacyCreateView(LoginRequiredMixin, StaffuserRequiredMixin, SuccessMessageMixin, CreateView):
    redirect_field_name = '/new-pharmacy/'
    raise_exception = True
    context_object_name = 'pharmacy_create'
    fields = ('name', 'address', 'region', 'city', 'phone_number', 'email', 'pharmacist', 'photo', 'hospital')
    model = models.Pharmacy
    success_url = reverse_lazy("chis_sl:pharmacy_list")
    success_message = "%(name)s successfully added!"


# The view used for updating the details of a Pharmacy
class PharmacyUpdateView(LoginRequiredMixin, StaffuserRequiredMixin, UpdateView):
    redirect_field_name = '/edit-pharmacy/'
    raise_exception = True
    context_object_name = 'pharmacy_update'
    fields = ('name', 'address', 'region', 'city', 'photo', 'phone_number', 'email', 'pharmacist', 'hospital')
    model = models.Pharmacy


# The view used for deleting a specific Pharmacy from the chis_sl app
class PharmacyDeleteView(LoginRequiredMixin, SuperuserRequiredMixin, SuccessMessageMixin, DeleteView):
    redirect_field_name = '/remove-pharmacy/'
    raise_exception = True
    context_object_name = 'pharmacy_delete'
    model = models.Pharmacy
    success_url = reverse_lazy("chis_sl:pharmacy_list")  # redirects to the pharmacy list after deleting a pharmacy
    success_message = "%(name)s successfully removed!"

    # a delete function for displaying success messages to the user
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(PharmacyDeleteView, self).delete(request, *args, **kwargs)


#######################################################################################################
#                                   VIEWS FOR PRESCRIPTION MODEL                                      #
#######################################################################################################
""" This section contains the following class based views for the Prescription model within the chis_sl app: 
    List View:      for listing all of the data objects found in the Prescription model
    Detail View:    this view presents a detailed information page on each object of the Prescription model 
    Create View:    this view is used for creating a new Prescription object within the Prescription model 
    Update View:    this view allows privileged users to be able to make modifications on the content of an existing 
                    record or object within the Prescription model 
    Delete View:    with the delete view, it allows only users with superuser status to access it. It requires the 
                    highest of privileges because it is used for deleting or removing records from the model. 
"""


# The class based view for listing all of the registered Prescriptions
class PrescriptionListView(ListView):
    context_object_name = 'prescriptions'
    model = models.Prescription

    def get_queryset(self):     # a query for sorting the details of Prescriptions by date
        return Prescription.objects.order_by('-date')


# A detailed class based view for Prescription
class PrescriptionDetailView(DetailView):
    context_object_name = 'prescription_detail'
    model = models.Prescription
    template_name = 'chis_sl/prescription_detail.html'


# The view used for creating a Prescription
class PrescriptionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    redirect_field_name = '/new-prescription/'
    raise_exception = True
    context_object_name = 'prescription_create'
    fields = ('name', 'date', 'drug_dosage', 'doctor', 'illness', 'patient')
    model = models.Prescription
    success_url = reverse_lazy("chis_sl:prescription_list")
    success_message = "The Medical Prescription %(name)s successfully added!"


# The view used for updating the details of a Prescription
class PrescriptionUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = '/edit-prescription/'
    raise_exception = True
    context_object_name = 'prescription_update'
    fields = ('name', 'date', 'drug_dosage', 'doctor', 'illness', 'patient')
    model = models.Prescription


# The view used for deleting a specific Prescription from the chis_sl app
class PrescriptionDeleteView(LoginRequiredMixin, SuperuserRequiredMixin, SuccessMessageMixin, DeleteView):
    redirect_field_name = '/remove-prescription/'
    raise_exception = True
    context_object_name = 'prescription_delete'
    model = models.Prescription
    # redirects to the prescription list after deleting a prescription
    success_url = reverse_lazy("chis_sl:prescription_list")
    success_message = "%(name)s successfully removed!"

    # A delete function for displaying success messages to the user
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(PrescriptionDeleteView, self).delete(request, *args, **kwargs)


#######################################################################################################
#                                   VIEWS FOR RECOMMENDATION MODEL                                    #
#######################################################################################################
""" This section contains the following class based views for the Recommendation model within the chis_sl app: 
    List View:      for listing all of the data objects found in the Recommendation model
    Detail View:    this view presents a detailed information page on each object of the Recommendation model 
    Create View:    this view is used for creating a new Recommendation object within the Recommendation model 
    Update View:    this view allows privileged users to be able to make modifications on the content of an existing 
                    record or object within the Recommendation model 
    Delete View:    with the delete view, it allows only users with superuser status to access it. It requires the 
                    highest of privileges because it is used for deleting or removing records from the model. 
"""


# The class based view for listing medical Recommendations
class RecommendationListView(ListView):
    context_object_name = 'recommendations'
    model = models.Recommendation

    def get_queryset(self):     # A query for sorting the recommendations by date
        return Recommendation.objects.order_by('-date')


# A detailed class based view for medical Recommendations
class RecommendationDetailView(DetailView):
    context_object_name = 'recommendation_detail'
    model = models.Recommendation
    template_name = 'chis_sl/recommendation_detail.html'


# The view used for creating a Medical Recommendation
class RecommendationCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    redirect_field_name = '/new-recommendation/'
    raise_exception = True
    context_object_name = 'recommendation_create'
    fields = ('number', 'date', 'medical_rec', 'status', 'doctor', 'patient')
    model = models.Recommendation
    success_url = reverse_lazy("chis_sl:recommendation_list")
    success_message = "Medical Recommendation %(number)s successfully added!"


# The view used for updating the details of a Medical Recommendation
class RecommendationUpdateView(LoginRequiredMixin, UpdateView):
    redirect_field_name = '/edit-recommendation/'
    raise_exception = True
    context_object_name = 'recommendation_update'
    fields = ('number', 'date', 'medical_rec', 'status', 'doctor', 'patient')
    model = models.Recommendation


# The view used for deleting a specific Medical Recommendation from the chis_sl app
class RecommendationDeleteView(LoginRequiredMixin, SuperuserRequiredMixin, SuccessMessageMixin, DeleteView):
    redirect_field_name = '/remove-recommendation/'
    raise_exception = True
    context_object_name = 'recommendation_delete'
    model = models.Recommendation
    # redirects to the medical recommendation list after deleting a Medical Recommendation
    success_url = reverse_lazy("chis_sl:recommendation_list")
    success_message = "Medical Recommendation %(number)s successfully removed!"

    # A delete method for displaying success messages to the user
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(RecommendationDeleteView, self).delete(request, *args, **kwargs)


#######################################################################################################
#                                   VIEWS FOR REPORT MODEL                                            #
#######################################################################################################
""" This section contains the following class based views for the Report model within the chis_sl app: 
    List View:      for listing all of the data objects found in the Report model
    Detail View:    this view presents a detailed information page on each object of the Report model 
    Create View:    this view is used for creating a new Report object within the Report model 
    Update View:    this view allows privileged users to be able to make modifications on the content of an existing 
                    record or object within the Report model 
    Delete View:    with the delete view, it allows only users with superuser status to access it. It requires the 
                    highest of privileges because it is used for deleting or removing records from the model. 
"""


# The class based view for listing patients' medical Reports
class ReportListView(ListView):
    context_object_name = 'reports'
    model = models.Report

    def get_queryset(self):     # A query for sorting the medical Reports by date of creation
        return Report.objects.order_by('-date')


# A detailed class based view for patients' medical Reports
class ReportDetailView(DetailView):
    context_object_name = 'report_detail'
    model = models.Report
    template_name = 'chis_sl/report_detail.html'


# The view used for creating a Medical Report
class ReportCreateView(LoginRequiredMixin, StaffuserRequiredMixin, SuccessMessageMixin, CreateView):
    redirect_field_name = '/new-report/'
    raise_exception = True
    context_object_name = 'report_create'
    fields = ('name', 'content', 'date', 'doctor', 'patient', 'history', 'staff')
    model = models.Report
    success_url = reverse_lazy("chis_sl:report_list")
    success_message = "%(name)s successfully added!"


# The view used for updating the details of a Medical Report
class ReportUpdateView(LoginRequiredMixin, StaffuserRequiredMixin, UpdateView):
    redirect_field_name = '/edit-report/'
    raise_exception = True
    context_object_name = 'report_update'
    fields = ('name', 'content', 'date', 'doctor', 'patient', 'history', 'staff')
    model = models.Report


# The view used for deleting a specific Medical Report from the chis_sl app
class ReportDeleteView(LoginRequiredMixin, SuperuserRequiredMixin, SuccessMessageMixin, DeleteView):
    redirect_field_name = '/remove-report/'
    raise_exception = True
    context_object_name = 'report_delete'
    model = models.Report
    # redirects to the report list after deleting a Medical Report
    success_url = reverse_lazy("chis_sl:report_list")
    success_message = "%(name)s successfully removed!"

    # A delete method for displaying success messages to the user
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(ReportDeleteView, self).delete(request, *args, **kwargs)


#######################################################################################################
#                                   VIEWS FOR WARD MODEL                                              #
#######################################################################################################
""" This section contains the following class based views for the Ward model within the chis_sl app: 
    List View:      for listing all of the data objects found in the Ward model
    Detail View:    this view presents a detailed information page on each object of the Ward model 
    Create View:    this view is used for creating a new Ward object within the Ward model 
    Update View:    this view allows privileged users to be able to make modifications on the content of an existing 
                    record or object within the Ward model 
    Delete View:    with the delete view, it allows only users with superuser status to access it. It requires the 
                    highest of privileges because it is used for deleting or removing records from the model. 
"""


# The class based view for listing all the Wards in a given hospital
class WardListView(ListView):
    context_object_name = 'wards'
    model = models.Ward

    def get_queryset(self):     # a query for sorting the names of Wards alphabetically
        return Ward.objects.order_by('name')


# A detailed class based view for wards in a given hospital
class WardDetailView(DetailView):
    context_object_name = 'ward_detail'
    model = models.Ward
    template_name = 'chis_sl/ward_detail.html'


# The view used for creating a Ward in a given hospital
class WardCreateView(LoginRequiredMixin, StaffuserRequiredMixin, SuccessMessageMixin, CreateView):
    redirect_field_name = '/new-ward/'
    raise_exception = True
    context_object_name = 'ward_create'
    fields = ('name', 'number', 'hospital')
    model = models.Ward
    success_url = reverse_lazy("chis_sl:ward_list")
    success_message = "%(name)s in %(hospital)s successfully added!"


# The view used for updating the details of a Ward within a hospital
class WardUpdateView(LoginRequiredMixin, StaffuserRequiredMixin, UpdateView):
    redirect_field_name = '/edit-ward/'
    raise_exception = True
    context_object_name = 'ward_update'
    fields = ('name', 'number', 'hospital')
    model = models.Ward


# The view used for deleting a specific Ward from the chis_sl app
class WardDeleteView(LoginRequiredMixin, SuperuserRequiredMixin, SuccessMessageMixin, DeleteView):
    redirect_field_name = '/remove-ward/'
    raise_exception = True
    context_object_name = 'ward_delete'
    model = models.Ward
    # redirects to the ward list after deleting a ward
    success_url = reverse_lazy("chis_sl:ward_list")
    success_message = "%(name)s in %(hospital)s successfully removed!"

    # A delete method for displaying success messages to the user
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(WardDeleteView, self).delete(request, *args, **kwargs)


# The class based view for listing all the User in the chis_sl app
class UserListView(ListView):
    context_object_name = 'users'
    model = models.User

    def get_queryset(self):     # a query for alphabetically sorting the users based on usernames
        return User.objects.order_by('username')


# A detailed class based view for users
class UserDetailView(DetailView):
    context_object_name = 'user_detail'
    model = models.User
    template_name = 'chis_sl/user_detail.html'


# The view used for updating the details of a User
class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    redirect_field_name = '/edit-user/'
    raise_exception = True
    context_object_name = 'user_update'
    fields = ('first_name', 'last_name', 'username', 'email')
    model = models.User
    success_url = reverse_lazy('home')
    success_message = "%(username)s successfully updated!"


# The view used for deleting a specific User from the chis_sl app
class UserDeleteView(LoginRequiredMixin, SuperuserRequiredMixin, SuccessMessageMixin, DeleteView):
    redirect_field_name = '/remove-user/'
    raise_exception = True
    context_object_name = 'user_delete'
    model = models.User
    # redirects to the user list after deletion
    success_url = reverse_lazy("chis_sl:user_list")
    success_message = "%(username)s successfully removed!"

    # A delete method for displaying success messages to the user
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(UserDeleteView, self).delete(request, *args, **kwargs)


#######################################################################################################
#                                   VIEWS FOR STAFF MODEL                                             #
#######################################################################################################
""" This section contains the following class based views for the Staff model within the chis_sl app: 
    List View:      for listing all of the data objects found in the Staff model
    Detail View:    this view presents a detailed information page on each object of the Staff model 
    Create View:    this view is used for creating a new Staff object within the Staff model 
    Update View:    this view allows privileged users to be able to make modifications on the content of an existing 
                    record or object within the Staff model 
    Delete View:    with the delete view, it allows only users with superuser status to access it. It requires the 
                    highest of privileges because it is used for deleting or removing records from the model. 
"""


# The class based view for listing all the registered Staff from various hospitals
class StaffListView(ListView):
    context_object_name = 'staffs'
    model = models.Staff

    def get_queryset(self):     # a query for sorting the names of Staff alphabetically
        return Staff.objects.order_by('first_name', 'last_name')


# A detailed class based view for Staff
class StaffDetailView(DetailView):
    context_object_name = 'staff_detail'
    model = models.Staff
    template_name = 'chis_sl/staff_detail.html'

    # a method for using the username of the staff as a parameter to the url mapping instead of pk or <slug>
    # this method helps with displaying user profile info for different username objects within the staff model
    def get_object(self):
        object = get_object_or_404(Staff, username=self.kwargs['username'])
        return object


# The view used for creating an Hospital Staff
class StaffCreateView(LoginRequiredMixin, SuperuserRequiredMixin, SuccessMessageMixin, CreateView):
    context_object_name = 'staff_create'
    model = models.Staff
    fields = ('first_name', 'middle_name', 'last_name', 'sex', 'date_of_birth', 'address', 'phone_number', 'email',
              'username', 'region', 'city', 'photo', 'hospital')
    success_url = reverse_lazy("chis_sl:staff_list")
    success_message = "Staff %(first_name)s %(middle_name)s %(last_name)s successfully added! Your login details " \
                      "will be sent to %(email)s shortly."


# The view used for updating the details of a Medical Patient
class StaffUpdateView(LoginRequiredMixin, StaffuserRequiredMixin, UpdateView):
    redirect_field_name = '/edit-staff/'
    raise_exception = True
    context_object_name = 'staff_update'
    model = models.Staff
    fields = ('first_name', 'middle_name', 'last_name', 'sex', 'date_of_birth', 'address', 'phone_number', 'email',
              'username', 'region', 'city', 'photo')
    success_url = reverse_lazy("home")

    # a method for using the username of the staff as a parameter to the url mapping instead of pk or <slug>
    # this method helps with displaying user profile info for different username objects within the patient model
    def get_object(self):
        object = get_object_or_404(Staff, username=self.kwargs['username'])
        return object


# The view used for updating the profile details of a Medical Patient
class StaffProfileUpdateView(LoginRequiredMixin, StaffuserRequiredMixin, UpdateView):
    redirect_field_name = '/edit-staff-profile/'
    raise_exception = True
    context_object_name = 'staff_profile_update'
    model = models.Staff
    fields = ('first_name', 'middle_name', 'last_name', 'sex', 'date_of_birth', 'address', 'phone_number', 'email',
              'username', 'region', 'city', 'photo')
    success_url = reverse_lazy("home")

    # a method for using the username of the staff as a parameter to the url mapping instead of pk or <slug>
    # this method helps with displaying user profile info for different username objects within the staff model
    def get_object(self):
        object = get_object_or_404(Staff, username=self.kwargs['username'])
        return object


# The view used for deleting a specific Hospital Staff from the chis_sl app
class StaffDeleteView(LoginRequiredMixin, SuperuserRequiredMixin, SuccessMessageMixin, DeleteView):
    redirect_field_name = '/remove-staff/'
    raise_exception = True
    context_object_name = 'staff_delete'
    model = models.Staff
    # redirects to the staff list after deleting a staff
    success_url = reverse_lazy("chis_sl:staff_list")
    success_message = "Hospital Staff %(first_name)s %(middle_name)s %(last_name)s successfully removed!"

    # a method for using the username of the staff as a parameter to the url mapping instead of pk or <slug>
    # this method helps with displaying user profile info for different username objects within the staff model
    def get_object(self):
        object = get_object_or_404(Staff, username=self.kwargs['username'])
        return object

    # a delete function for displaying success messages to the user
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(StaffDeleteView, self).delete(request, *args, **kwargs)


#######################################################################################################
#                      FUNCTION VIEWS FOR HANDLING USERS' AUTHENTICATION                              #
#######################################################################################################


# The function based view for handling user login process
def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request, 'chis_sl/login.html', {})


# The function based view for handling user logout process
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


# A function based view for changing users' password
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('home')
        else:
            return redirect('chis_sl:change_password')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'change_password.html', args)
