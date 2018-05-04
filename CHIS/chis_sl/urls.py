# Django import order
#   1. Standard library imports
#   2. Imports from core Django
#   3. Imports from third-party apps including those unrelated to Django
#   4. Imports from the apps that you created as part of your Django Project

from django.conf.urls import url
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, \
    password_reset_complete
from django.contrib.auth import views as auth_views
from . import views


# APP NAME FOR TEMPLATE TAGGING
app_name = 'chis_sl'

urlpatterns = [
    url(r'^login/$', auth_views.LoginView.as_view(template_name='chis_sl/login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^doctor/$', views.DoctorListView.as_view(), name='doctor_list'),
    url(r'^hospital/$', views.HospitalListView.as_view(), name='hospital_list'),
    url(r'^pharmacy/$', views.PharmacyListView.as_view(), name='pharmacy_list'),
    url(r'^patient/$', views.PatientListView.as_view(), name='patient_list'),
    url(r'^appointment/$', views.AppointmentListView.as_view(), name='appointment_list'),
    url(r'^ward/$', views.WardListView.as_view(), name='ward_list'),
    url(r'^official/$', views.OfficialListView.as_view(), name='official_list'),
    url(r'^drug/$', views.DrugListView.as_view(), name='drug_list'),
    url(r'^illness/$', views.IllnessListView.as_view(), name='illness_list'),
    url(r'^prescription/$', views.PrescriptionListView.as_view(), name='prescription_list'),
    url(r'^bed/$', views.BedListView.as_view(), name='bed_list'),
    url(r'^history/$', views.HistoryListView.as_view(), name='history_list'),
    url(r'^report/$', views.ReportListView.as_view(), name='report_list'),
    url(r'^medical-test/$', views.MedicalTestListView.as_view(), name='medical_list'),
    url(r'^recommendation/$', views.RecommendationListView.as_view(), name='recommendation_list'),
    url(r'^user/$', views.UserListView.as_view(template_name='chis_sl/user_list.html'), name='user_list'),
    url(r'^hospital-staff/$', views.StaffListView.as_view(template_name='chis_sl/staff_list.html'), name='staff_list'),
    url(r'^doctor/(?P<username>[-\w]+)/$', views.DoctorDetailView.as_view(), name='doctor_detail'),
    url(r'^patient/(?P<username>[-\w]+)/$', views.PatientDetailView.as_view(), name='patient_detail'),
    url(r'^official/(?P<username>[-\w]+)/$', views.OfficialDetailView.as_view(), name='official_detail'),
    url(r'^hospital-staff/(?P<username>[-\w]+)/$', views.StaffDetailView.as_view(), name='staff_detail'),
    url(r'^hospital/(?P<pk>\d+)/$', views.HospitalDetailView.as_view(), name='hospital_detail'),
    url(r'^pharmacy/(?P<pk>\d+)/$', views.PharmacyDetailView.as_view(), name='pharmacy_detail'),
    url(r'^appointment/(?P<pk>\d+)/$', views.AppointmentDetailView.as_view(), name='appointment_detail'),
    url(r'^ward/(?P<pk>\d+)/$', views.WardDetailView.as_view(), name='ward_detail'),
    url(r'^drug/(?P<pk>\d+)/$', views.DrugDetailView.as_view(), name='drug_detail'),
    url(r'^illness/(?P<pk>\d+)/$', views.IllnessDetailView.as_view(), name='illness_detail'),
    url(r'^prescription/(?P<pk>\d+)/$', views.PrescriptionDetailView.as_view(), name='prescription_detail'),
    url(r'^bed/(?P<pk>\d+)/$', views.BedDetailView.as_view(), name='bed_detail'),
    url(r'^history/(?P<pk>\d+)/$', views.HistoryDetailView.as_view(), name='history_detail'),
    url(r'^report/(?P<pk>\d+)/$', views.ReportDetailView.as_view(), name='report_detail'),
    url(r'^medical-test/(?P<pk>\d+)/$', views.MedicalTestDetailView.as_view(), name='medical_detail'),
    url(r'^recommendation/(?P<pk>\d+)/$', views.RecommendationDetailView.as_view(), name='recommendation_detail'),
    url(r'^user/(?P<pk>\d+)/$', views.UserDetailView.as_view(template_name='chis_sl/user_detail.html'),
        name='user_detail'),
    url(r'^new-doctor/$', views.DoctorCreateView.as_view(), name='create_doctor'),
    url(r'^new-patient/$', views.PatientCreateView.as_view(), name='create_patient'),
    url(r'^new-official/$', views.OfficialCreateView.as_view(), name='create_official'),
    url(r'^new-hospital-staff/$', views.StaffCreateView.as_view(), name='create_staff'),
    url(r'^new-hospital/$', views.HospitalCreateView.as_view(), name='create_hospital'),
    url(r'^new-pharmacy/$', views.PharmacyCreateView.as_view(), name='create_pharmacy'),
    url(r'^new-appointment/$', views.AppointmentCreateView.as_view(), name='create_appointment'),
    url(r'^new-ward/$', views.WardCreateView.as_view(), name='create_ward'),
    url(r'^new-bed/$', views.BedCreateView.as_view(), name='create_bed'),
    url(r'^new-drug/$', views.DrugCreateView.as_view(), name='create_drug'),
    url(r'^new-illness/$', views.IllnessCreateView.as_view(), name='create_illness'),
    url(r'^new-prescription/$', views.PrescriptionCreateView.as_view(), name='create_prescription'),
    url(r'^new-history/$', views.HistoryCreateView.as_view(), name='create_history'),
    url(r'^new-report/$', views.ReportCreateView.as_view(), name='create_report'),
    url(r'^new-medical-test/$', views.MedicalTestCreateView.as_view(), name='create_medical_test'),
    url(r'^new-recommendation/$', views.RecommendationCreateView.as_view(), name='create_recommendation'),
    url(r'^edit-doctor/(?P<username>[-\w]+)/$', views.DoctorUpdateView.as_view(), name='update_doctor'),
    url(r'^edit-patient/(?P<username>[-\w]+)/$', views.PatientUpdateView.as_view(), name='update_patient'),
    url(r'^edit-patient-profile/(?P<username>[-\w]+)/$', views.PatientProfileUpdateView.as_view(),
        name='update_patient_profile'),
    url(r'^edit-official/(?P<username>[-\w]+)/$', views.OfficialUpdateView.as_view(), name='update_official'),
    url(r'^edit-hospital-staff/(?P<username>[-\w]+)/$', views.StaffUpdateView.as_view(), name='update_staff'),
    url(r'^edit-hospital-staff-profile/(?P<username>[-\w]+)/$', views.StaffProfileUpdateView.as_view(),
        name='update_staff_profile'),
    url(r'^edit-hospital/(?P<pk>\d+)/$', views.HospitalUpdateView.as_view(), name='update_hospital'),
    url(r'^edit-pharmacy/(?P<pk>\d+)/$', views.PharmacyUpdateView.as_view(), name='update_pharmacy'),
    url(r'^edit-appointment/(?P<pk>\d+)/$', views.AppointmentUpdateView.as_view(), name='update_appointment'),
    url(r'^edit-ward/(?P<pk>\d+)/$', views.WardUpdateView.as_view(), name='update_ward'),
    url(r'^edit-bed/(?P<pk>\d+)/$', views.BedUpdateView.as_view(), name='update_bed'),
    url(r'^edit-drug/(?P<pk>\d+)/$', views.DrugUpdateView.as_view(), name='update_drug'),
    url(r'^edit-illness/(?P<pk>\d+)/$', views.IllnessUpdateView.as_view(), name='update_illness'),
    url(r'^edit-prescription/(?P<pk>\d+)/$', views.PrescriptionUpdateView.as_view(), name='update_prescription'),
    url(r'^edit-history/(?P<pk>\d+)/$', views.HistoryUpdateView.as_view(), name='update_history'),
    url(r'^edit-report/(?P<pk>\d+)/$', views.ReportUpdateView.as_view(), name='update_report'),
    url(r'^edit-medical-test/(?P<pk>\d+)/$', views.MedicalTestUpdateView.as_view(), name='update_medical_test'),
    url(r'^edit-recommendation/(?P<pk>\d+)/$', views.RecommendationUpdateView.as_view(), name='update_recommendation'),
    url(r'^edit-user/(?P<pk>\d+)/$', views.UserUpdateView.as_view(template_name='chis_sl/user_form.html'),
        name='update_user'),
    url(r'^remove-doctor/(?P<username>[-\w]+)/$', views.DoctorDeleteView.as_view(), name='delete_doctor'),
    url(r'^remove-patient/(?P<username>[-\w]+)/$', views.PatientDeleteView.as_view(), name='delete_patient'),
    url(r'^remove-official/(?P<username>[-\w]+)/$', views.OfficialDeleteView.as_view(), name='delete_official'),
    url(r'^remove-hospital-staff/(?P<username>[-\w]+)/$', views.StaffDeleteView.as_view(), name='delete_staff'),
    url(r'^remove-hospital/(?P<pk>\d+)/$', views.HospitalDeleteView.as_view(), name='delete_hospital'),
    url(r'^remove-pharmacy/(?P<pk>\d+)/$', views.PharmacyDeleteView.as_view(), name='delete_pharmacy'),
    url(r'^remove-appointment/(?P<pk>\d+)/$', views.AppointmentDeleteView.as_view(), name='delete_appointment'),
    url(r'^remove-ward/(?P<pk>\d+)/$', views.WardDeleteView.as_view(), name='delete_ward'),
    url(r'^remove-bed/(?P<pk>\d+)/$', views.BedDeleteView.as_view(), name='delete_bed'),
    url(r'^remove-drug/(?P<pk>\d+)/$', views.DrugDeleteView.as_view(), name='delete_drug'),
    url(r'^remove-illness/(?P<pk>\d+)/$', views.IllnessDeleteView.as_view(), name='delete_illness'),
    url(r'^remove-prescription/(?P<pk>\d+)/$', views.PrescriptionDeleteView.as_view(), name='delete_prescription'),
    url(r'^remove-history/(?P<pk>\d+)/$', views.HistoryDeleteView.as_view(), name='delete_history'),
    url(r'^remove-report/(?P<pk>\d+)/$', views.ReportDeleteView.as_view(), name='delete_report'),
    url(r'^remove-medical-test/(?P<pk>\d+)/$', views.MedicalTestDeleteView.as_view(), name='delete_medical_test'),
    url(r'^remove-recommendation/(?P<pk>\d+)/$', views.RecommendationDeleteView.as_view(),
        name='delete_recommendation'),
    url(r'^remove-user/(?P<pk>\d+)/$', views.UserDeleteView.as_view(template_name='chis_sl/user_confirm_delete.html'),
        name='delete_user'),
    url(r'^appointment-by/(?P<username>[-\w]+)/$', views.DoctorAppointmentsList.as_view(), name='for_doctor'),
    url(r'^appointment-by/(?P<username>[-\w]+)/(?P<pk>\d+)/$', views.DoctorAppointmentUpdateView.as_view(),
        name='edit_doctor_appointment'),
    url(r'^recommendation-by/(?P<username>[-\w]+)/$', views.DoctorRecommendationsListView.as_view(),
        name='recommendation_for_doctor'),
    url(r'^recommendation-by/(?P<username>[-\w]+)/(?P<pk>\d+)/$', views.DoctorRecommendationUpdateView.as_view(),
        name='edit_doctor_recommendation'),
    url(r'^medical-test-by/(?P<username>[-\w]+)/$', views.DoctorMedicalTestsListView.as_view(),
        name='medical_test_for_doctor'),
    url(r'^medical-test-by/(?P<username>[-\w]+)/(?P<pk>\d+)/$', views.DoctorMedicalTestUpdateView.as_view(),
        name='edit_doctor_medical_test'),
    url(r'^prescription-by/(?P<username>[-\w]+)/$', views.DoctorPrescriptionsListView.as_view(),
        name='prescription_for_doctor'),
    url(r'^prescription-by/(?P<username>[-\w]+)/(?P<pk>\d+)/$', views.DoctorPrescriptionUpdateView.as_view(),
        name='edit_doctor_prescription'),
    url(r'^patient-for/(?P<username>[-\w]+)/$', views.DoctorPatientsListView.as_view(), name='patient_for_doctor'),
    url(r'^patient-for/(?P<username>[-\w]+)/(?P<pk>\d+)/$', views.DoctorPatientUpdateView.as_view(),
        name='edit_doctor_patient'),
    url(r'^patient-for/(?P<username>[-\w]+)/(?P<pk>\d+)/$', views.PatientDetailView.as_view(),
        name='patient_doctor_detail'),
    url(r'^appointment-for/(?P<username>[-\w]+)/$', views.PatientAppointmentsListView.as_view(),
        name='appointment_for_patient'),
    url(r'^appointment-for/(?P<username>[-\w]+)/(?P<pk>\d+)/$', views.AppointmentDetailView.as_view(),
        name='patient_appointment_detail'),
    url(r'^recommendation-for/(?P<username>[-\w]+)/$', views.PatientRecommendationsListView.as_view(),
        name='recommendation_for_patient'),
    url(r'^recommendation-for/(?P<username>[-\w]+)/(?P<pk>\d+)/$', views.RecommendationDetailView.as_view(),
        name='patient_recommendation_detail'),
    url(r'^medical-test-for/(?P<username>[-\w]+)/$', views.PatientMedicalTestsListView.as_view(),
        name='medical_test_for_patient'),
    url(r'^medical-test-for/(?P<username>[-\w]+)/(?P<pk>\d+)/$', views.MedicalTestDetailView.as_view(),
        name='patient_medical_test_detail'),
    url(r'^prescription-for/(?P<username>[-\w]+)/$', views.PatientPrescriptionsListView.as_view(),
        name='prescription_for_patient'),
    url(r'^prescription-for/(?P<username>[-\w]+)/(?P<pk>\d+)/$', views.PrescriptionDetailView.as_view(),
        name='patient_prescription_detail'),
    url(r'^medical-history-for/(?P<username>[-\w]+)/$', views.PatientHistoryListView.as_view(),
        name='medical_history_for_patient'),
    url(r'^medical-history-for/(?P<username>[-\w]+)/(?P<pk>\d+)/$', views.HistoryDetailView.as_view(),
        name='patient_medical_history_detail'),
    url(r'^medical-report-for/(?P<username>[-\w]+)/$', views.PatientReportListView.as_view(),
        name='medical_report_for_patient'),
    url(r'^medical-report-for/(?P<username>[-\w]+)/(?P<pk>\d+)/$', views.ReportDetailView.as_view(),
        name='patient_medical_report_detail'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^reset-password/$', password_reset, name='password_reset'),
    url(r'^reset-password/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uid64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        name='password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete, name='password_reset_complete'),
]
