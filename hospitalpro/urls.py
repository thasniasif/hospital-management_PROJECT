"""hospitalpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hospitalapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.home, name='home'),
                  path('home', views.home, name='home'),
                  path('contact', views.contact, name='contact'),
                  path('about', views.about, name='about'),
                  path('admin_home', views.admin_home, name='admin_home'),
                  path('admin_patient', views.admin_patient, name='admin_patient'),
path('doctor_home', views.doctor_home, name='doctor_home'),
path('doctor_signup', views.doctor_signup, name='doctor_signup'),
path('doctor_signup_admin', views.doctor_signup_admin, name='doctor_signup_admin'),
                  path('admin_signup', views.admin_signup, name='admin_signup'),
                  path('admin_login', views.admin_login, name='admin_login'),

path('doctor_login', views.doctor_login, name='doctor_login'),
path('doctor_dash', views.doctor_dash, name='doctor_dash'),
path('doctor_approve', views.doctor_approve, name='doctor_approve'),
path('doctor_record', views.doctor_record, name='doctor_record'),
path('doctor_special', views.doctor_special, name='doctor_special'),
path('doctor_dashboard', views.doctor_dashboard, name='doctor_dashboard'),
path('doctor_patient', views.doctor_patient, name='doctor_patient'),
path('doctor_appointment', views.doctor_appointment, name='doctor_appointment'),
# path('discharge2<int:pk>', views.discharge2, name='discharge2'),
                  path('admin_dash', views.admin_dash, name='admin_dash'),
                  path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
                  path('admin_doctor', views.admin_doctor, name='admin_doctor'),
                    path('approve<int:id>',views.approve,name='approve'),
                path('admin_book_appointment',views.admin_book_appointment,name='admin_book_appointment'),
path('app_approve<int:id>',views.app_approve,name='app_approve'),
path('app_reject<int:id>',views.app_reject,name='app_reject'),
path('y_d_p', views.y_d_p, name='y_d_p'),
path('admit<int:id>',views.admit,name='admit'),
path('OP<int:id>',views.OP,name='OP'),
path('discharge_patient_op',views.discharge_patient_op,name='discharge_patient_op'),
path('doc_discharge_OP<int:id>',views.doc_discharge_OP,name='doc_discharge_OP'),
path('your_op_patient_record',views.your_op_patient_record,name='your_op_patient_record'),
    path('admin_view_appoint', views.admin_view_appoint,name='admin_view_appoint'),
                    path('reject<int:id>',views.reject,name='reject'),
                    path('admin_appoint',views.admin_appoint,name='admin_appoint'),
                    path('admin_approve_appoint', views.admin_approve_appoint,name='admin_approve_appoint'),
path('doc_discharge<int:id>',views.doc_discharge,name='doc_discharge'),
path('logout',views.logout,name='logout'),
path('doctor_v_y_a', views.doctor_v_y_a, name='doctor_v_y_a'),
path('delete_appoint', views.delete_appoint, name='delete_appoint'),
path('appoint_delete<int:id>', views.appoint_delete,name='appoint_delete'),
path('doc_logout', views.doc_logout, name='doc_logout'),
path('IP<int:id>',views.IP,name='IP'),
path('admit_patient2',views.admit_patient2,name='admit_patient2'),
path('patient_home', views.patient_home, name='patient_home'),
path('patient_signup', views.patient_signup, name='patient_signup'),
path('patient_login', views.patient_login, name='patient_login'),
path('patient_dash', views.patient_dash, name='patient_dash'),
path('patient_dashboard', views.patient_dashboard, name='patient_dashboard'),
path('patient_approve', views.patient_approve, name='patient_approve'),
path('approve_pat<int:id>',views.approve_pat,name='approve_pat'),
path('patient_record', views.patient_record, name='patient_record'),
path('discharge_patient', views.discharge_patient, name='discharge_patient'),
path('patient_signup_admin', views.patient_signup_admin, name='patient_signup_admin'),
path('discharge<int:id>',views.discharge,name='discharge'),
path('your_patient_record',views.your_patient_record,name='your_patient_record'),
path('patient_appointments', views.patient_appointments, name='patient_appointments'),
path('book_appoint', views.book_appoint, name='book_appoint'),
path('view_your_appoint', views.view_your_appoint, name='view_your_appoint'),
path('pat_logout', views.pat_logout, name='pat_logout'),
path('patient_discharge', views.patient_discharge, name='patient_discharge'),
path('validate_username',views.validate_username,name='validate_username'),
path('validate_password',views.validate_password,name='validate_password'),
path('bill_pdf<int:id>',views.bill_pdf,name='bill_pdf'),
path('bill_pdf_pat',views.bill_pdf_pat,name='bill_pdf_pat'),
path('reject_pat<int:id>',views.reject_pat,name='reject_pat'),
path('validate_password_pat',views.validate_password_pat,name='validate_password_pat'),
path('validate_username_pat',views.validate_username_pat,name='validate_username_pat'),
path('login_a_vala',views.login_a_vala,name='login_a_vala'),
path('login_val',views.login_val,name='login_val'),
path('login_valp',views.login_valp,name='login_valp'),
path('validate_a_uname',views.validate_a_uname,name='validate_a_uname'),
path('validate_a_password',views.validate_a_password,name='validate_a_password'),
                  # path('bill<int:pat_id>', views.bill, name='bill'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
