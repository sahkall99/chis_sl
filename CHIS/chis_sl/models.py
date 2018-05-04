# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from django.db.models.signals import post_save

User = get_user_model()     # definition of the user model used in the CHIS_SL App


# Definition for the Doctor Model/table
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctors', null=True, db_column="userID")
    first_name = models.CharField("doctor's first name", max_length=150, db_column="docFN")
    middle_name = models.CharField("doctor's middle name", max_length=150, default=" ", db_column="docMN", blank=True)
    last_name = models.CharField("doctor's last name", max_length=150, db_column="docLN")
    username = models.CharField("doctor's username", max_length=100, db_column="docUName")
    email = models.EmailField("doctor's email address", db_column="docEmail", null=True, blank=True, max_length=100)
    MALE = 'M'
    FEMALE = 'F'
    DOCTOR_SEX_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    sex = models.CharField("select sex", max_length=1, choices=DOCTOR_SEX_CHOICES, default=MALE, db_column="docSex")
    date_of_birth = models.DateField("date of birth", db_column="docDOB", help_text="yyyy-mm-dd")
    address = models.CharField("doctor's address", max_length=200, db_column="docAddr")
    BO = 'Bo'
    BONTHE = 'Bonthe'
    FALABA = 'Falaba'
    FREETOWN = 'Freetown'
    KABALA = 'Kabala'
    KAILAHUN = 'Kailahun'
    KAMBIA = 'Kambia'
    KARENA = 'Karene'
    KENEMA = 'Kenema'
    MAGBURAKA = 'Magburaka'
    MAKENI = 'Makeni'
    MOYAMBA = 'Moyamba'
    PORT_LOKO = 'Port Loko'
    PUJEHUN = 'Pujehun'
    SEFADU = 'Sefadu'
    WATERLOO = 'Waterloo'
    DOCTOR_CITY_CHOICES = (
        (BO, 'Bo City'),
        (BONTHE, 'Bonthe City'),
        (FALABA, 'Falaba City'),
        (FREETOWN, 'Freetown City'),
        (KABALA, 'Kabala City'),
        (KAILAHUN, 'Kailahun City'),
        (KAMBIA, 'Kambia City'),
        (KARENA, 'Karena City'),
        (KENEMA, 'Kenema City'),
        (MAGBURAKA, 'Magburaka City'),
        (MAKENI, 'Makeni City'),
        (MOYAMBA, 'Moyamba City'),
        (PORT_LOKO, 'Port Loko City'),
        (PUJEHUN, 'Pujehun City'),
        (SEFADU, 'Sefadu City'),
        (WATERLOO, 'Waterloo City'),
    )
    city = models.CharField("select city", max_length=20, choices=DOCTOR_CITY_CHOICES, default=FREETOWN,
                            db_column="docCity")
    EASTERN_REGION = 'Eastern Region'
    NORTHERN_REGION = 'Northern Region'
    NORTH_WEST = 'North West'
    SOUTHERN_REGION = 'Southern Region'
    WESTERN_RURAL = 'Western Rural'
    WESTERN_URBAN = 'Western Urban'
    DOCTOR_REGION_CHOICES = (
        (EASTERN_REGION, 'Eastern Region'),
        (NORTHERN_REGION, 'Northern Region'),
        (NORTH_WEST, 'North West'),
        (SOUTHERN_REGION, 'Southern Region'),
        (WESTERN_RURAL, 'Western Rural'),
        (WESTERN_URBAN, 'Western Urban'),
    )
    region = models.CharField("doctor's region", max_length=20, choices=DOCTOR_REGION_CHOICES, default=WESTERN_URBAN,
                              db_column="docRegion")
    phone_regex = RegexValidator(regex=r'^\+\d{8,15}$',
                                 message="Phone number must be entered in the format: "
                                         "'+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField("doctor's contact", validators=[phone_regex], max_length=16, db_column="docPhone",
                                    help_text="doctor's phone number")
    qualification = models.CharField("doctor's medical qualification", max_length=150, db_column="docQualif",
                                     null=True, blank=True)
    speciality = models.CharField("doctor's speciality", max_length=200, db_column="docSpe", null=True, blank=True)
    PERMANENT = 'Permanent'
    TRAINEE = 'Trainee'
    VISITING = 'Visiting'
    DOCTOR_CATEGORY_CHOICES = (
        (PERMANENT, 'Permanent'),
        (TRAINEE, 'Trainee'),
        (VISITING, 'Visiting')
    )
    category = models.CharField("select category", max_length=20, choices=DOCTOR_CATEGORY_CHOICES, default=PERMANENT,
                                db_column="docCat")
    work_experience = models.PositiveIntegerField(verbose_name="doctor's work experience in years", db_column="docExp",
                                                  null=True, blank=True)
    photo = models.ImageField("upload photo", upload_to='doctor/', null=True, blank=True, editable=True,
                              help_text="doctor's Profile Photo", max_length=250, db_column="docPhoto")

    hospital = models.ForeignKey('chis_sl.Hospital', on_delete=models.CASCADE, related_name='doctor_hospital',
                                 verbose_name="select related hospital", db_column="hosID", null=True, blank=True)
    the_staff = models.ForeignKey('chis_sl.Staff', on_delete=None, related_name='doctor_staff', db_column="staID",
                                  verbose_name="the staff who added the doctor", null=True, blank=True)

    # the database table name for the Doctor's Model
    class Meta:
        db_table = "doctor"

    # the string representation of the Doctor's Model
    def __str__(self):
        return 'Dr. %s %s %s' % (self.first_name, self.middle_name, self.last_name)

    # this function redirects to another page when create doctor button on the Add Doctor Form is clicked.
    # doctor_detail is from the context_object_name from the DoctorDetailView
    def get_absolute_url(self):
        return reverse("chis_sl:doctor_detail", kwargs={'pk': self.pk})


def create_profile(sender, **kwargs):
    if kwargs['created']:
        doctor = Doctor.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


# Definition for the Patient Model/table
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patients', null=True, db_column="userID")
    first_name = models.CharField("patient's first name", max_length=150, db_column="patFN")
    middle_name = models.CharField("patient's middle name", max_length=150, default=" ", db_column="patMN", blank=True)
    last_name = models.CharField("patient's last name", max_length=150, db_column="patLN")
    username = models.CharField("patient's username", max_length=100, db_column="patUName")
    email = models.EmailField("patient's email address", db_column="patEmail", null=True, blank=True, max_length=100)
    MALE = 'M'
    FEMALE = 'F'
    PATIENT_SEX_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    sex = models.CharField("select sex", max_length=1, choices=PATIENT_SEX_CHOICES, default=MALE, db_column="patSex")
    date_of_birth = models.DateField("patient's date of birth", db_column="patDOB", help_text="yyyy-mm-dd")
    address = models.CharField("patient's address", max_length=200, db_column="patAddr")
    BO = 'Bo'
    BONTHE = 'Bonthe'
    FALABA = 'Falaba'
    FREETOWN = 'Freetown'
    KABALA = 'Kabala'
    KAILAHUN = 'Kailahun'
    KAMBIA = 'Kambia'
    KARENA = 'Karene'
    KENEMA = 'Kenema'
    MAGBURAKA = 'Magburaka'
    MAKENI = 'Makeni'
    MOYAMBA = 'Moyamba'
    PORT_LOKO = 'Port Loko'
    PUJEHUN = 'Pujehun'
    SEFADU = 'Sefadu'
    WATERLOO = 'Waterloo'
    PATIENT_CITY_CHOICES = (
        (BO, 'Bo City'),
        (BONTHE, 'Bonthe City'),
        (FALABA, 'Falaba City'),
        (FREETOWN, 'Freetown City'),
        (KABALA, 'Kabala City'),
        (KAILAHUN, 'Kailahun City'),
        (KAMBIA, 'Kambia City'),
        (KARENA, 'Karena City'),
        (KENEMA, 'Kenema City'),
        (MAGBURAKA, 'Magburaka City'),
        (MAKENI, 'Makeni City'),
        (MOYAMBA, 'Moyamba City'),
        (PORT_LOKO, 'Port Loko City'),
        (PUJEHUN, 'Pujehun City'),
        (SEFADU, 'Sefadu City'),
        (WATERLOO, 'Waterloo City'),
    )
    city = models.CharField("select city", max_length=20, choices=PATIENT_CITY_CHOICES, default=FREETOWN,
                            db_column="patCity")
    EASTERN_REGION = 'Eastern Region'
    NORTHERN_REGION = 'Northern Region'
    NORTH_WEST = 'North West'
    SOUTHERN_REGION = 'Southern Region'
    WESTERN_RURAL = 'Western Rural'
    WESTERN_URBAN = 'Western Urban'
    PATIENT_REGION_CHOICES = (
        (EASTERN_REGION, 'Eastern Region'),
        (NORTHERN_REGION, 'Northern Region'),
        (NORTH_WEST, 'North West'),
        (SOUTHERN_REGION, 'Southern Region'),
        (WESTERN_RURAL, 'Western Rural'),
        (WESTERN_URBAN, 'Western Urban'),
    )
    region = models.CharField("choose region", max_length=20, choices=PATIENT_REGION_CHOICES, default=WESTERN_URBAN,
                              db_column="patRegion")
    phone_regex = RegexValidator(regex=r'^\+\d{8,15}$',
                                 message="Phone number must be entered in the format: "
                                         "'+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField("patient's contact", validators=[phone_regex], max_length=16, db_column="patPhone",
                                    help_text="patient's phone number")
    age = models.PositiveSmallIntegerField("patient's age", help_text="age of the patient in years", db_column="patAge",
                                           default=0)
    O_POSITIVE = 'O - Positive'
    O_NEGATIVE = 'O - Negative'
    A_POSITIVE = 'A - Positive'
    A_NEGATIVE = 'A - Negative'
    B_POSITIVE = 'B - Positive'
    B_NEGATIVE = 'B - Negative'
    AB_POSITIVE = 'AB - Positive'
    AB_NEGATIVE = 'AB - Negative'
    PATIENT_BLOOD_TYPE = (
        (O_POSITIVE, 'O - Positive'),
        (O_NEGATIVE, 'O - Negative'),
        (A_POSITIVE, 'A - Positive'),
        (A_NEGATIVE, 'A - Negative'),
        (B_POSITIVE, 'B - Positive'),
        (B_NEGATIVE, 'B - Negative'),
        (AB_POSITIVE, 'AB - Positive'),
        (AB_NEGATIVE, 'AB - Negative'),
    )
    blood_type = models.CharField("choose blood type", max_length=20, choices=PATIENT_BLOOD_TYPE, default=O_POSITIVE,
                                  db_column="patBGroup", null=True, blank=True)
    INPATIENT = 'Inpatient'
    OUTPATIENT = 'Outpatient'
    PATIENT_CATEGORY_CHOICES = (
        (INPATIENT, 'Inpatient'),
        (OUTPATIENT, 'Outpatient'),
    )
    category = models.CharField("select category", max_length=12, choices=PATIENT_CATEGORY_CHOICES, db_column="patCat",
                                default=OUTPATIENT)
    date_diagnosed = models.DateTimeField("patient diagnosis' date", db_column="patDiagDate", default=timezone.now,
                                          null=True, blank=True)
    admission_date = models.DateTimeField("patient's admission date", null=True, blank=True, db_column="patADate")
    discharge_date = models.DateTimeField("patient's discharged date", null=True, blank=True, db_column="patDDate")
    photo = models.ImageField("patient's photo", upload_to='patient/', null=True, blank=True, editable=True,
                              help_text="patient's Profile Photo", max_length=250, db_column="patPhoto")
    doctor = models.ForeignKey('chis_sl.Doctor', on_delete=None, related_name='patient_doctor', null=True, blank=True,
                               verbose_name="the assigned doctor", db_column="docID", )
    hospital = models.ForeignKey('chis_sl.Hospital', on_delete=models.CASCADE, null=True, blank=True, db_column="hosID",
                                 related_name='patient_hospital', verbose_name="the related hospital")
    the_staff = models.ForeignKey('chis_sl.Staff', on_delete=None, related_name='patient_staff', db_column="staID",
                                  verbose_name="the staff who created the patient", null=True, blank=True)
    ward = models.ForeignKey('chis_sl.Ward', on_delete=models.CASCADE, related_name='patient_ward', null=True,
                             verbose_name="ward in which the patient is admitted", db_column="wardID", blank=True)

    # the database table name for the Patient's Model
    class Meta:
        db_table = "patient"

    # the string representation of the Patient's Model
    def __str__(self):
        return '%s %s %s' % (self.first_name, self.middle_name, self.last_name)

    # this function redirects to another page when create patient button on the Add Patient Form is clicked.
    # patient_detail is from the context_object_name from the PatientDetailView
    def get_absolute_url(self):
        return reverse("chis_sl:patient_detail", kwargs={'pk': self.pk})


def create_profile(sender, **kwargs):
    if kwargs['created']:
        patient = Patient.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


# Definition for the Hospital_Staff Model/table
class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staffs', null=True, db_column="userID")
    first_name = models.CharField("staff's first name", max_length=150, db_column="staFN")
    middle_name = models.CharField("staff's middle name", max_length=150, default=" ", db_column="staMN", blank=True)
    last_name = models.CharField("staff's last name", max_length=150, db_column="staLN")
    username = models.CharField("staff's username", max_length=100, db_column="staUName")
    email = models.EmailField("staff's email address", db_column="staEmail", null=True, blank=True, max_length=100)
    MALE = 'M'
    FEMALE = 'F'
    STAFF_SEX_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    sex = models.CharField("select sex", max_length=1, choices=STAFF_SEX_CHOICES, default=MALE, db_column="staSex")
    date_of_birth = models.DateField("staff's date of birth", db_column="staDOB", help_text="yyyy-mm-dd")
    address = models.CharField("staff's address", max_length=200, db_column="staAddr")
    BO = 'Bo'
    BONTHE = 'Bonthe'
    FALABA = 'Falaba'
    FREETOWN = 'Freetown'
    KABALA = 'Kabala'
    KAILAHUN = 'Kailahun'
    KAMBIA = 'Kambia'
    KARENA = 'Karene'
    KENEMA = 'Kenema'
    MAGBURAKA = 'Magburaka'
    MAKENI = 'Makeni'
    MOYAMBA = 'Moyamba'
    PORT_LOKO = 'Port Loko'
    PUJEHUN = 'Pujehun'
    SEFADU = 'Sefadu'
    WATERLOO = 'Waterloo'
    STAFF_CITY_CHOICES = (
        (BO, 'Bo City'),
        (BONTHE, 'Bonthe City'),
        (FALABA, 'Falaba City'),
        (FREETOWN, 'Freetown City'),
        (KABALA, 'Kabala City'),
        (KAILAHUN, 'Kailahun City'),
        (KAMBIA, 'Kambia City'),
        (KARENA, 'Karena City'),
        (KENEMA, 'Kenema City'),
        (MAGBURAKA, 'Magburaka City'),
        (MAKENI, 'Makeni City'),
        (MOYAMBA, 'Moyamba City'),
        (PORT_LOKO, 'Port Loko City'),
        (PUJEHUN, 'Pujehun City'),
        (SEFADU, 'Sefadu City'),
        (WATERLOO, 'Waterloo City'),
    )
    city = models.CharField("select city", max_length=20, choices=STAFF_CITY_CHOICES, default=FREETOWN,
                            db_column="staCity")
    EASTERN_REGION = 'Eastern Region'
    NORTHERN_REGION = 'Northern Region'
    NORTH_WEST = 'North West'
    SOUTHERN_REGION = 'Southern Region'
    WESTERN_RURAL = 'Western Rural'
    WESTERN_URBAN = 'Western Urban'
    STAFF_REGION_CHOICES = (
        (EASTERN_REGION, 'Eastern Region'),
        (NORTHERN_REGION, 'Northern Region'),
        (NORTH_WEST, 'North West'),
        (SOUTHERN_REGION, 'Southern Region'),
        (WESTERN_RURAL, 'Western Rural'),
        (WESTERN_URBAN, 'Western Urban'),
    )
    region = models.CharField("choose region", max_length=20, choices=STAFF_REGION_CHOICES, default=WESTERN_URBAN,
                              db_column="staRegion")
    phone_regex = RegexValidator(regex=r'^\+\d{8,15}$',
                                 message="Phone number must be entered in the format: "
                                         "'+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField("staff's contact", validators=[phone_regex], max_length=16, db_column="staPhone",
                                    help_text="staff's phone number")
    photo = models.ImageField("staff's photo", upload_to='staff/', null=True, blank=True, editable=True,
                              help_text="staff's Profile Photo", max_length=250, db_column="staPhoto")
    hospital = models.ForeignKey('chis_sl.Hospital', on_delete=models.CASCADE, related_name='staff_hospital',
                                 verbose_name="staff's related hospital", db_column="hosID")

    # the database table name for the Staff's data Model
    class Meta:
        db_table = "hospital_staff"

    # the string representation of the Staff's data Model
    def __str__(self):
        return '%s %s %s' % (self.first_name, self.middle_name, self.last_name)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        staff = Staff.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


# Definition for the Official_User Model/table
class Official(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='officials', null=True, db_column="userID")
    first_name = models.CharField("official's first name", max_length=150, db_column="offFN")
    middle_name = models.CharField("official's middle name", max_length=100, default=" ", db_column="offMN", blank=True)
    last_name = models.CharField("official's last name", max_length=150, db_column="offLN")
    username = models.CharField("official's username", max_length=100, db_column="offUName")
    email = models.EmailField("official's email address", db_column="offEmail", null=True, blank=True, max_length=100)
    MALE = 'M'
    FEMALE = 'F'
    OFFICIAL_SEX_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    sex = models.CharField("select sex", max_length=1, choices=OFFICIAL_SEX_CHOICES, default=MALE, db_column="offSex")
    date_of_birth = models.DateTimeField("official's date of birth", db_column="offDOB", help_text="yyyy-mm-dd",
                                         default=timezone.now)
    address = models.CharField("official's address", max_length=200, db_column="offAddr")
    BO = 'Bo'
    BONTHE = 'Bonthe'
    FALABA = 'Falaba'
    FREETOWN = 'Freetown'
    KABALA = 'Kabala'
    KAILAHUN = 'Kailahun'
    KAMBIA = 'Kambia'
    KARENA = 'Karene'
    KENEMA = 'Kenema'
    MAGBURAKA = 'Magburaka'
    MAKENI = 'Makeni'
    MOYAMBA = 'Moyamba'
    PORT_LOKO = 'Port Loko'
    PUJEHUN = 'Pujehun'
    SEFADU = 'Sefadu'
    WATERLOO = 'Waterloo'
    OFFICIAL_CITY_CHOICES = (
        (BO, 'Bo City'),
        (BONTHE, 'Bonthe City'),
        (FALABA, 'Falaba City'),
        (FREETOWN, 'Freetown City'),
        (KABALA, 'Kabala City'),
        (KAILAHUN, 'Kailahun City'),
        (KAMBIA, 'Kambia City'),
        (KARENA, 'Karena City'),
        (KENEMA, 'Kenema City'),
        (MAGBURAKA, 'Magburaka City'),
        (MAKENI, 'Makeni City'),
        (MOYAMBA, 'Moyamba City'),
        (PORT_LOKO, 'Port Loko City'),
        (PUJEHUN, 'Pujehun City'),
        (SEFADU, 'Sefadu City'),
        (WATERLOO, 'Waterloo City'),
    )
    city = models.CharField("select city", max_length=20, choices=OFFICIAL_CITY_CHOICES, default=FREETOWN,
                            db_column="offCity")
    EASTERN_REGION = 'Eastern Region'
    NORTHERN_REGION = 'Northern Region'
    NORTH_WEST = 'North West'
    SOUTHERN_REGION = 'Southern Region'
    WESTERN_RURAL = 'Western Rural'
    WESTERN_URBAN = 'Western Urban'
    OFFICIAL_REGION_CHOICES = (
        (EASTERN_REGION, 'Eastern Region'),
        (NORTHERN_REGION, 'Northern Region'),
        (NORTH_WEST, 'North West'),
        (SOUTHERN_REGION, 'Southern Region'),
        (WESTERN_RURAL, 'Western Rural'),
        (WESTERN_URBAN, 'Western Urban'),
    )
    region = models.CharField("choose region", max_length=20, choices=OFFICIAL_REGION_CHOICES, default=WESTERN_URBAN,
                              db_column="offRegion")
    phone_regex = RegexValidator(regex=r'^\+\d{8,15}$',
                                 message="Phone number must be entered in the format: "
                                         "'+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField("official's contact", validators=[phone_regex], max_length=16, db_column="offPhone",
                                    help_text="official's phone number")
    photo = models.ImageField("official's photo", upload_to='official/', null=True, blank=True, editable=True,
                              help_text="official's Profile Photo", max_length=250, db_column="offPhoto")
    unit = models.CharField("official's unit", max_length=200, db_column="offUnit", null=True, blank=True)

    # the database table name for the Official's data Model
    class Meta:
        db_table = "official_user"

    # the string representation of the Official's data Model
    def __str__(self):
        return '%s %s %s' % (self.first_name, self.middle_name, self.last_name)

    # this function redirects to another page when create official button on the Add Official Form is clicked.
    # official_detail is from the context_object_name from the OfficialDetailView
    def get_absolute_url(self):
        return reverse("chis_sl:official_detail", kwargs={'pk': self.pk})


def create_profile(sender, **kwargs):
    if kwargs['created']:
        official = Official.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)


# Definition for the Appointment Model/table
class Appointment(models.Model):
    date = models.DateTimeField("date and time of appointment", db_column="appDate")
    doctor = models.ForeignKey('chis_sl.Doctor', on_delete=models.CASCADE, db_column="docID",
                               related_name='appointment_doctor', verbose_name="the designated doctor")
    patient = models.ForeignKey('chis_sl.Patient', on_delete=models.CASCADE, db_column="patID",
                                related_name='appointment_patient', verbose_name="the designated patient")
    staff = models.ForeignKey('chis_sl.Staff', on_delete=None, related_name='appointment_staff', db_column="staID",
                              verbose_name="the designated staff",  null=True, blank=True)

    # the database table name for the Appointment's Model
    class Meta:
        db_table = "appointment"

    # the string representation of the Appointment's Model
    def __str__(self):
        return '%s %s and %s' % (self.date, self.doctor, self.patient)

    # this function redirects to another page when the create appointment button on the Add Appointment Form is clicked.
    # appointment_detail is from the context_object_name from the AppointmentDetailView
    def get_absolute_url(self):
        return reverse("chis_sl:appointment_detail", kwargs={'pk': self.pk})


# Definition for the Hospital Model/table
class Hospital(models.Model):
    name = models.CharField("hospital's name", max_length=200, db_column="hosName")
    address = models.CharField("hospital's address", max_length=200, db_column="hosAddr")
    EASTERN_REGION = 'Eastern Region'
    NORTHERN_REGION = 'Northern Region'
    NORTH_WEST = 'North West'
    SOUTHERN_REGION = 'Southern Region'
    WESTERN_RURAL = 'Western Rural'
    WESTERN_URBAN = 'Western Urban'
    HOSPITAL_REGION_CHOICES = (
        (EASTERN_REGION, 'Eastern Region'),
        (NORTHERN_REGION, 'Northern Region'),
        (NORTH_WEST, 'North West'),
        (SOUTHERN_REGION, 'Southern Region'),
        (WESTERN_RURAL, 'Western Rural'),
        (WESTERN_URBAN, 'Western Urban'),
    )
    region = models.CharField("hospital's region", max_length=20, choices=HOSPITAL_REGION_CHOICES, default=WESTERN_URBAN,
                              db_column="hosRegion")
    BO = 'Bo'
    BONTHE = 'Bonthe'
    FALABA = 'Falaba'
    FREETOWN = 'Freetown'
    KABALA = 'Kabala'
    KAILAHUN = 'Kailahun'
    KAMBIA = 'Kambia'
    KARENA = 'Karene'
    KENEMA = 'Kenema'
    MAGBURAKA = 'Magburaka'
    MAKENI = 'Makeni'
    MOYAMBA = 'Moyamba'
    PORT_LOKO = 'Port Loko'
    PUJEHUN = 'Pujehun'
    SEFADU = 'Sefadu'
    WATERLOO = 'Waterloo'
    HOSPITAL_CITY_CHOICES = (
        (BO, 'Bo City'),
        (BONTHE, 'Bonthe City'),
        (FALABA, 'Falaba City'),
        (FREETOWN, 'Freetown City'),
        (KABALA, 'Kabala City'),
        (KAILAHUN, 'Kailahun City'),
        (KAMBIA, 'Kambia City'),
        (KARENA, 'Karena City'),
        (KENEMA, 'Kenema City'),
        (MAGBURAKA, 'Magburaka City'),
        (MAKENI, 'Makeni City'),
        (MOYAMBA, 'Moyamba City'),
        (PORT_LOKO, 'Port Loko City'),
        (PUJEHUN, 'Pujehun City'),
        (SEFADU, 'Sefadu City'),
        (WATERLOO, 'Waterloo City'),
    )
    city = models.CharField("hospital's location", max_length=20, choices=HOSPITAL_CITY_CHOICES, default=FREETOWN,
                            db_column="hosCity")
    email = models.EmailField("hospital's email address", max_length=100, db_column="hosEmail", unique=True)
    phone_regex = RegexValidator(regex=r'^\+\d{8,15}$',
                                 message="Phone number must be entered in the format: "
                                         "'+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField("hospital's contact", validators=[phone_regex], max_length=16, db_column="hosPhone")
    photo = models.ImageField("hospital's photo", upload_to='hospital/', max_length=250, db_column="hosPhoto",
                              null=True, blank=True, editable=True, help_text="A picture of the hospital")

    # the database table name for the Hospital's Model
    class Meta:
        db_table = "hospital"

    # the string representation of the Hospital's model
    def __str__(self):
        return '%s %s %s' % (self.name, self.address, self.city)

    # this function redirects to another page when the create hospital button on the Add Hospital Form is clicked.
    # hospital_detail is from the context_object_name from the HospitalDetailView
    def get_absolute_url(self):
        return reverse("chis_sl:hospital_detail", kwargs={'pk': self.pk})


# Definition for the Ward Model/table
class Ward(models.Model):
    name = models.CharField("ward's name", max_length=200, db_column="wardName")
    number = models.IntegerField("ward's numerical identifier", db_column="wardNum", null=True)
    hospital = models.ForeignKey('chis_sl.Hospital', on_delete=models.CASCADE, related_name='ward',
                                 verbose_name="the related hospital", db_column="hosID")

    # the database table name for the Ward's Model
    class Meta:
        db_table = "ward"

    # the string representation of a Ward in a hospital
    def __str__(self):
        return '%s %s' % (self.name, self.hospital)

    # this function redirects to another page when the create ward button on the Add Ward Form is clicked.
    # ward_detail is from the context_object_name from the WardDetailView
    def get_absolute_url(self):
        return reverse("chis_sl:ward_detail", kwargs={'pk': self.pk})


# Definition for the Bed Model/table
class Bed(models.Model):
    name = models.CharField("the name of the bed", max_length=100, help_text="ward name with specific number",
                            db_column="bedName")
    AVAILABLE = 'Available'
    BOOKED = 'Booked'
    FAULTY = 'Faulty'
    OCCUPIED = 'Occupied'
    BED_STATUS_CHOICES = (
        (AVAILABLE, 'Bed is Available'),
        (BOOKED, 'Bed is Booked'),
        (FAULTY, 'Bed is Faulty'),
        (OCCUPIED, 'Bed is Occupied'),
    )
    status = models.CharField("bed's current status", max_length=10, choices=BED_STATUS_CHOICES, default=AVAILABLE,
                              db_column="bedStatus")
    assigned_patient = models.ForeignKey('chis_sl.Patient', on_delete=models.CASCADE, related_name='bed_patient',
                                         verbose_name="the assigned patient", db_column="patID", null=True, blank=True)
    contained_ward = models.ForeignKey('chis_sl.Ward', on_delete=models.CASCADE, related_name='bed_ward',
                                       verbose_name="ward containing the bed", db_column="wardID")

    # the database table name for the Bed's Model
    class Meta:
        db_table = "bed"

    # the string representation of the Bed's Model
    def __str__(self):
        return '%s %s' % (self.name, self.status)

    # this function redirects to another page when the create bed button on the Add Bed Form is clicked.
    # bed_detail is from the context_object_name from the BedDetailView
    def get_absolute_url(self):
        return reverse("chis_sl:bed_detail", kwargs={'pk': self.pk})


# Definition for the Pharmacy Model/table
class Pharmacy(models.Model):
    name = models.CharField("pharmacy's name", max_length=200, db_column="phaName")
    address = models.CharField("pharmacy's address", max_length=250, db_column="phaAddr")
    EASTERN_REGION = 'Eastern Region'
    NORTHERN_REGION = 'Northern Region'
    NORTH_WEST = 'North West'
    SOUTHERN_REGION = 'Southern Region'
    WESTERN_RURAL = 'Western Rural'
    WESTERN_URBAN = 'Western Urban'
    PHARMACY_REGION_CHOICES = (
        (EASTERN_REGION, 'Eastern Region'),
        (NORTHERN_REGION, 'Northern Region'),
        (NORTH_WEST, 'North West'),
        (SOUTHERN_REGION, 'Southern Region'),
        (WESTERN_RURAL, 'Western Rural'),
        (WESTERN_URBAN, 'Western Urban'),
    )
    region = models.CharField("pharmacy's region", max_length=20, choices=PHARMACY_REGION_CHOICES,
                              default=WESTERN_URBAN, db_column="phaRegion")
    BO = 'Bo'
    BONTHE = 'Bonthe'
    FALABA = 'Falaba'
    FREETOWN = 'Freetown'
    KABALA = 'Kabala'
    KAILAHUN = 'Kailahun'
    KAMBIA = 'Kambia'
    KARENA = 'Karene'
    KENEMA = 'Kenema'
    MAGBURAKA = 'Magburaka'
    MAKENI = 'Makeni'
    MOYAMBA = 'Moyamba'
    PORT_LOKO = 'Port Loko'
    PUJEHUN = 'Pujehun'
    SEFADU = 'Sefadu'
    WATERLOO = 'Waterloo'
    PHARMACY_CITY_CHOICES = (
        (BO, 'Bo City'),
        (BONTHE, 'Bonthe City'),
        (FALABA, 'Falaba City'),
        (FREETOWN, 'Freetown City'),
        (KABALA, 'Kabala City'),
        (KAILAHUN, 'Kailahun City'),
        (KAMBIA, 'Kambia City'),
        (KARENA, 'Karena City'),
        (KENEMA, 'Kenema City'),
        (MAGBURAKA, 'Magburaka City'),
        (MAKENI, 'Makeni City'),
        (MOYAMBA, 'Moyamba City'),
        (PORT_LOKO, 'Port Loko City'),
        (PUJEHUN, 'Pujehun City'),
        (SEFADU, 'Sefadu City'),
        (WATERLOO, 'Waterloo City'),
    )
    city = models.CharField("pharmacy's location", max_length=20, choices=PHARMACY_CITY_CHOICES, default=FREETOWN,
                            db_column="phaCity")
    photo = models.ImageField("pharmacy's photo", upload_to='pharmacy/', help_text="A picture of the pharmacy",
                              null=True, blank=True, editable=True, max_length=250, db_column="phaPhoto")
    phone_regex = RegexValidator(regex=r'^\+\d{8,15}$',
                                 message="Phone number must be entered in the format: "
                                         "'+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField("pharmacy's contact", validators=[phone_regex], max_length=16, db_column="phaPhone")
    email = models.EmailField("pharmacy's email address", max_length=100, db_column="phaEmail", null=True, blank=True)
    pharmacist = models.CharField("pharmacist's full name", max_length=100, db_column="pharmacist")
    hospital = models.ForeignKey('chis_sl.Hospital', on_delete=None, related_name='pharmacy', null=True, blank=True,
                                 verbose_name="the related hospital", db_column="hosID")

    # the database table name for the Pharmacy's Model
    class Meta:
        db_table = "pharmacy"

    # the string representation of the Pharmacy's Model
    def __str__(self):
        return '%s %s %s' % (self.name, self.address, self.city)

    # this function redirects to another page when the create pharmacy button on the Add Pharmacy Form is clicked.
    # pharmacy_detail is from the context_object_name from the PharmacyDetailView
    def get_absolute_url(self):
        return reverse("chis_sl:pharmacy_detail", kwargs={'pk': self.pk})


# Definition for the Drug Model/table
class Drug(models.Model):
    name = models.CharField("name of drug", max_length=200, db_column="drugName")
    type = models.CharField("the type of drug", max_length=100, db_column="drugType")
    description = models.TextField("drug's description", null=True, blank=True, db_column="drugDesc")
    quantity = models.PositiveIntegerField("the quantity of a specific drug", db_column="drugQty")
    manufacture_date = models.DateField("drug's manufacture date", db_column="drugMDate")
    expiry_date = models.DateField("drug's expiry date", db_column="drugEDate")
    patient = models.ForeignKey('chis_sl.Patient', on_delete=None, related_name='patient_drug',
                                verbose_name="the patient's drug", db_column="patID", null=True, blank=True)
    pharmacy = models.ForeignKey('chis_sl.Pharmacy', on_delete=models.CASCADE, related_name='pharmacy_drug',
                                 verbose_name="the pharmacy's drugs", db_column="phaID")
    prescription = models.ForeignKey('chis_sl.Prescription', on_delete=None, related_name='prescription_drug',
                                     verbose_name="prescription of drugs", db_column="presID", null=True, blank=True)

    # the database table name for the Drug's Model
    class Meta:
        db_table = "drug"

    # the string representation of the Drug's Model
    def __str__(self):
        return '%s %s' % (self.name, self.type)

    # this function redirects to another page when the create drug button on the Add Drug Form is clicked.
    # drug_detail is from the context_object_name from the DrugDetailView
    def get_absolute_url(self):
        return reverse("chis_sl:drug_detail", kwargs={'pk': self.pk})


# Definition for the Illness Model/table
class Illness(models.Model):
    name = models.CharField("name of illness", max_length=200, db_column="illName")
    type = models.CharField("the type illness", max_length=200, db_column="illType")
    patient = models.ForeignKey('chis_sl.Patient', related_name='illness_patient',
                                verbose_name="the affected patient", db_column="patID", null=True, blank=True)

    # the database table name for the Illness' Model
    class Meta:
        db_table = "illness"

    # the string representation of the Illness' Model
    def __str__(self):
        return self.name

    # this function redirects to another page when the create illness button on the Add Illness Form is clicked.
    # illness_detail is from the context_object_name from the IllnessDetailView
    def get_absolute_url(self):
            return reverse("chis_sl:illness_detail", kwargs={'pk': self.pk})


# Definition for the Prescription Model/table
class Prescription(models.Model):
    name = models.CharField("name of prescription", max_length=200, db_column="presName",
                            help_text="give a suitable name to the prescription")
    date = models.DateTimeField("date of prescription", default=timezone.now, db_column="presDate")
    drug_dosage = models.CharField("drug's dosage", max_length=200, db_column="drugDos")
    doctor = models.ForeignKey('chis_sl.Doctor', on_delete=models.CASCADE, related_name='prescription_doctor',
                               verbose_name="prescription issued by doctor", db_column="docID")
    illness = models.ForeignKey('chis_sl.Illness', on_delete=models.CASCADE, related_name='prescription_illness',
                                verbose_name="illness' prescription", db_column="illID")
    patient = models.ForeignKey('chis_sl.Patient', on_delete=models.CASCADE, related_name='prescription_patient',
                                verbose_name="patient's prescription", db_column="patID", null=True, blank=True)

    # the database table name for the Prescription's data Model
    class Meta:
        db_table = "prescription"

    # the string representation of the Prescription's data Model
    def __str__(self):
        return '%s %s %s' % (self.name, self.illness, self.patient)

    # this function redirects to another page when the create prescription button on the
    # Add Prescription Form is clicked.
    # prescription_detail is from the context_object_name from the PrescriptionDetailView
    def get_absolute_url(self):
            return reverse("chis_sl:prescription_detail", kwargs={'pk': self.pk})


# Definition for the History Model/table
class History(models.Model):
    number = models.CharField("history's number", db_column="hisNum", max_length=100,
                              help_text="contains alpha-numeric characters")
    description = models.TextField("brief description", db_column="hisDesc")
    appointment = models.ForeignKey('chis_sl.Appointment', on_delete=None, related_name='history_appointment',
                                    verbose_name="Select Appointment", db_column="appID")
    doctor = models.ForeignKey('chis_sl.Doctor', on_delete=None, related_name='history_doctor',
                               verbose_name="Select Doctor", db_column="docID")
    illness = models.ForeignKey('chis_sl.Illness', on_delete=None, related_name='history_illness',
                                verbose_name="Choose Illness", db_column="illID")
    patient = models.ForeignKey('chis_sl.Patient', on_delete=models.CASCADE, related_name='history_patient',
                                verbose_name="Select Patient", db_column="patID", null=True, blank=True)
    prescription = models.ForeignKey('chis_sl.Prescription', on_delete=None, related_name='history_prescription',
                                     verbose_name="Prescription", db_column="presID", null=True, blank=True)

    # the database table name for the History's data Model
    class Meta:
        db_table = "history"

    # the string representation of the History's data Model
    def __str__(self):
        return self.number

    # this function redirects to another page when the create history button on the Add History Form is clicked.
    # history_detail is from the context_object_name from the HistoryDetailView
    def get_absolute_url(self):
        return reverse("chis_sl:history_detail", kwargs={'pk': self.pk})


# Definition for the Report Model/table
class Report(models.Model):
    name = models.CharField("name of report", max_length=150, db_column="rptName")
    content = models.TextField("report's content", db_column="rptCont")
    date = models.DateTimeField("report's date", default=timezone.now, db_column="rptDate")
    doctor = models.ForeignKey('chis_sl.Doctor', on_delete=None, related_name='report_doctor',
                               verbose_name="doctor in report", db_column="docID")
    patient = models.ForeignKey('chis_sl.Patient', on_delete=None, related_name='report_patient',
                                verbose_name="patient in report", db_column="patID")
    history = models.ForeignKey('chis_sl.History', on_delete=None, related_name='report_history',
                                verbose_name="history containing report", db_column="hisID", null=True, blank=True)
    staff = models.ForeignKey('chis_sl.Staff', on_delete=None, related_name='report_staff',
                              verbose_name="report generated by staff", db_column="staID", null=True, blank=True)

    # the database table name for the Report's data Model
    class Meta:
        db_table = "report"

    # the string representation of the Report's data Model
    def __str__(self):
        return '%s %s' % (self.name, self.date)

    # this function redirects to another page when the create report button on the Add Report Form is clicked.
    # report_detail is from the context_object_name from the ReportDetailView
    def get_absolute_url(self):
            return reverse("chis_sl:report_detail", kwargs={'pk': self.pk})


# Definition for the Medical_Test Model/table
class MedicalTest(models.Model):
    name = models.CharField("name of medical test", max_length=200, db_column="testName")
    date = models.DateTimeField("date of medical test", default=timezone.now, db_column="testDate")
    unit = models.CharField("medical test's unit", max_length=200, db_column="testUnit", null=True, blank=True)
    doctor = models.ForeignKey('chis_sl.Doctor', on_delete=models.CASCADE, related_name='test_doctor',
                               verbose_name="test prescribed by doctor", db_column="docID")
    patient = models.ForeignKey('chis_sl.Patient', on_delete=models.CASCADE, related_name='test_patient',
                                verbose_name="test prescribed for patient", db_column="patID")

    # the database table name for the MedicalTest's data Model
    class Meta:
        db_table = "medical_test"

    # the string representation of the MedicalTest's data Model
    def __str__(self):
        return '%s %s' % (self.name, self.date)

    # this function redirects to another page when create medical test button on the Add Medical Test Form is clicked.
    # medical_test_detail is from the context_object_name from the MedicalTestDetailView
    def get_absolute_url(self):
            return reverse("chis_sl:medical_detail", kwargs={'pk': self.pk})


# Definition for the Recommendation Model/table
class Recommendation(models.Model):
    number = models.CharField("medical recommendation number", max_length=50, db_column="recNum",
                              help_text="contains alpha-numeric characters")
    doctor = models.ForeignKey('chis_sl.Doctor', on_delete=models.CASCADE, db_column="docID",
                               related_name='recommendation_doctor', verbose_name="doctor making recommendation")
    patient = models.ForeignKey('chis_sl.Patient', on_delete=models.CASCADE, related_name='recommendation_patient',
                                db_column="patID", verbose_name="patient receiving medical recommendation")
    medical_rec = models.TextField(verbose_name="medical recommendations", db_column="recText")
    date = models.DateTimeField(verbose_name="date recommendation is issued", db_column="recDate", default=timezone.now)
    NEW = 'New'
    PENDING = 'Pending'
    APPLIED = 'Applied'
    RECOMMENDATION_STATUS_CHOICES = (
        (NEW, 'New Medical Recommendation'),
        (PENDING, 'Medical Recommendation not yet Applied'),
        (APPLIED, 'Medical Recommendation already Applied'),
    )
    status = models.CharField("status of medical recommendation", max_length=50, default=NEW,
                              choices=RECOMMENDATION_STATUS_CHOICES, db_column="recStatus")

    # the database table name for the Recommendation's data Model

    class Meta:
        # acting as composite primary keys
        unique_together = ('number', 'doctor', 'patient')
        db_table = "medical_recommendation"

    # the string representation of the Recommendation's data Model
    def __str__(self):
        return '%s | %s | %s' % (self.doctor, self.patient, self.status)

    # this function redirects to another page when create medical recommendation button on the Add Medical
    # Recommendation Form is clicked.
    # recommendation_detail is from the context_object_name from the RecommendationDetailView
    def get_absolute_url(self):
        return reverse("chis_sl:recommendation_detail", kwargs={'pk': self.pk})
