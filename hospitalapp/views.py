from django.shortcuts import render, redirect
from .models import admin, doctor,patient,appointment,discharge_tb
import random
from django.http import JsonResponse
from django.contrib import messages

from django.contrib.messages.api import success
import time
# from django.utils.timezone import mktime
from datetime import date
from django.db.models import Q

# Create your views here.

def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def admin_home(request):
    return render(request, 'admin_home.html')


def admin_signup(request):
    if (request.method == 'POST'):
        f_name = request.POST.get("fname")
        l_name = request.POST.get("lname")
        u_name = request.POST.get("uname")
        password = request.POST.get("password")
        rec = admin(first_name=f_name, last_name=l_name, user_name=u_name, password=password)
        # if rec.is_valid():
        rec.save()
        return render(request, 'admin_signup.html')

    return render(request, 'admin_signup.html')


# def admin_login(request):
def admin_login(request):
    if (request.method == 'POST'):
        u_name = request.POST.get("uname")
        password = request.POST.get("password")
        rec = admin.objects.filter(user_name=u_name, password=password)
        if rec:
            request.session["user"] = u_name
            return redirect('admin_dash')

    return render(request, 'admin_login.html')


def admin_dash(request):
    if 'user' in request.session:
        current_user = request.session["user"]
        s = admin.objects.filter(user_name=current_user)
        context = {
            'current_user': current_user,
            's': s

        }
        return render(request, 'admin_dash.html', context)
    else:
        return render(request, 'admin_dash.html')


def admin_dashboard(request):
    if 'user' in request.session:
        current_user = request.session["user"]
        s = admin.objects.filter(user_name=current_user)
        d=doctor.objects.filter(status='Permanent')
        doc_c=d.count()
        s2=doctor.objects.order_by('-join_date')[:3]
        p1 = patient.objects.order_by('-join_date')[:3]
        p=patient.objects.filter(status='Admit')
        pat_c=p.count()
        p2 = patient.objects.filter(status='On Hold')
        admit_c=p2.count()
        a=appointment.objects.filter(status='Approved')
        app_c=a.count()
        a2 = appointment.objects.filter(status='Processing')
        process_c=a2.count()
        s3=doctor.objects.filter(status='On Hold')
        count=s3.count()
        s4=doctor.objects.all()
        c=s4.count()
        # for i in s2:
        #     print(i.user_name)
        context = {
            'dash': 1,
            'current_user': current_user,
            's': s,
            's2' : s2,
            'app_count' : count,
            'doc_c' : doc_c,
            'process_c' :   process_c,
            'app_c' : app_c,
            'pat_c' : pat_c,
            'admit_c' : admit_c,
            'c' : c,
            'p1' : p1

        }
        return render(request, 'admin_dash.html', context)
    else:
        return render(request, 'admin_dash.html')


def admin_doctor(request):
    if 'user' in request.session:
        current_user = request.session["user"]
        s = admin.objects.filter(user_name=current_user)

        context = {
            'doc': 1,
            'current_user': current_user,
            's': s,


        }
        return render(request, 'admin_dash.html', context)
    else:
        return render(request, 'admin_dash.html')
def admin_patient(request):
    if 'user' in request.session:
        current_user = request.session["user"]
        s = admin.objects.filter(user_name=current_user)

        context = {
            'pat_v': 1,
            'current_user': current_user,
            's': s,


        }
        return render(request, 'admin_dash.html', context)
    else:
        return render(request, 'admin_dash.html')

    # return render(request,'admin_dash.html')


def doctor_home(request):
    return render(request, 'doctor_home.html')



def doctor_approve(request):
    if 'user' in request.session:
        current_user = request.session["user"]
        s = admin.objects.filter(user_name=current_user)
        s2 = doctor.objects.filter(status='On Hold')
        context = {
            'approve_doctor': 1,
            'current_user': current_user,
            's' : s,
            's2': s2,

        }
        return render(request, 'admin_dash.html', context)
    else:
        return render(request, 'admin_dash.html')

def approve(request,id):
    if 'user' in request.session:
        current_user = request.session["user"]
        s = admin.objects.filter(user_name=current_user)
        s2 = doctor.objects.get(id=id)
        s2.status = 'Permanent'



        s2.save()
        context = {

            'current_user': current_user,
            's' : s,
            's2': s2,


        }
        return redirect('doctor_approve')
        # return render(request, 'admin_dash.html', context)
    else:
        return redirect('doctor_approve')

def reject(request,id):
    if 'user' in request.session:
        current_user = request.session["user"]
        s = admin.objects.filter(user_name=current_user)
        s2 = doctor.objects.get(id=id)
        s2.delete()
        context = {

            'current_user': current_user,
            's': s,


        }
        return redirect('doctor_approve')
        # return render(request, 'admin_dash.html', context)
    else:
        return redirect('doctor_approve')

    # s=doctor.objects.filter(id=id)

    # return render(request,'admin_dash.html')
def doctor_record(request):
    if 'user' in request.session:
        current_user = request.session["user"]
        s = admin.objects.filter(user_name=current_user)
        s2 = doctor.objects.filter(status='Permanent')
        for i in s2:
            print(i.first_name)
        context = {
            'doctor_record' : 1,
            'current_user': current_user,
            's': s,
            's2': s2,

        }
        return render(request, 'admin_dash.html', context)
    else:
        return render(request, 'admin_dash.html')
def discharge_patient(request):
    if 'user' in request.session:
        current_user = request.session["user"]
        s = admin.objects.filter(user_name=current_user)
        s2=[]
        a=appointment.objects.filter(status='Discharged')
        for i in a:
            s2=patient.objects.filter(user_name=i.patient_user_name)

        context = {
            'discharge_patient' : 1,
            'current_user': current_user,
            's': s,
            's2': s2,
            'a' : a,
        }
        return render(request, 'admin_dash.html', context)
    else:
        return render(request, 'admin_dash.html')


def patient_record(request):
    if 'user' in request.session:
        current_user = request.session["user"]
        s = admin.objects.filter(user_name=current_user)
        s2 = patient.objects.filter(status='Admit')
        # for i in s2:
        #     print(i.first_name)
        context = {
            'patient_record': 1,
            'current_user': current_user,
            's': s,
            's2': s2,

        }
        return render(request, 'admin_dash.html', context)
    else:
        return render(request, 'admin_dash.html')


def doctor_special(request):
    if 'user' in request.session:
        current_user = request.session["user"]
        s = admin.objects.filter(user_name=current_user)
        s2 = doctor.objects.filter(status='Permanent',specialisation='cardiology')
        sgyn=doctor.objects.filter(status='Permanent',specialisation='gynacology')
        sgen = doctor.objects.filter(status='Permanent', specialisation='general medicine')
        sp = doctor.objects.filter(status='Permanent', specialisation='pediatrics')
        sn = doctor.objects.filter(status='Permanent', specialisation='newrology')
        for i in s2:
            print(i.first_name)
        context = {
            'doctor_special' : 1,
            'current_user': current_user,
            's': s,
            's2': s2,
            'sgyn' : sgyn,
            'sgen' : sgen,
            'sp': sp,
            'sn' : sn

        }
        return render(request, 'admin_dash.html', context)
    else:
        return render(request, 'admin_dash.html')
def doctor_signup_admin(request):
    print("hello")
    if (request.method == 'POST'):
        f_name = request.POST.get("fname")
        l_name = request.POST.get("lname")
        u_name = request.POST.get("uname")
        password = request.POST.get("password")
        u_address = request.POST.get("address")
        u_special = request.POST.get("special")
        u_profile=request.FILES.get("file")

        u_mobile = request.POST.get("mobile")
        if 'user' in request.session:
            print("hi")
            current_user = request.session["user"]
            rec = doctor(first_name=f_name, last_name=l_name, user_name=u_name, password=password, address=u_address,specialisation=u_special, mobile=u_mobile, profile=u_profile,status='Permanent')

            rec.save()
            return redirect(doctor_record)
    else:
        return render(request, 'doctor_signup.html')

def patient_approve(request):
    if 'user' in request.session:
        current_user = request.session["user"]
        s = admin.objects.filter(user_name=current_user)
        s2 = patient.objects.filter(status='On Hold')
        context = {
            'approve_patient': 1,
            'current_user': current_user,
            's' : s,
            's2': s2,

        }
        return render(request, 'admin_dash.html', context)
    else:
        return render(request, 'admin_dash.html')
def approve_pat(request,id):
    if 'user' in request.session:
        current_user = request.session["user"]
        s = admin.objects.filter(user_name=current_user)
        s2 = patient.objects.get(id=id)
        d=doctor.objects.filter(user_name=s2.doc_dep)
        d_name=''
        for i in d:
            d_name=i.first_name+''+i.last_name
        name=s2.first_name+''+s2.last_name
        s2.status = 'Registered'
        s2.save()
        ap = appointment(doctor_user_name=s2.doc_dep, patient_user_name=s2.user_name, patient_name=name, description=s2.symptom,
                         doctor_name=d_name, status='Booked',app_date=s2.join_date)

        ap.save()
        context = {

            'current_user': current_user,
            's' : s,
            's2': s2,


        }
        return redirect('patient_approve')
        # return render(request, 'admin_dash.html', context)
    else:
        return redirect('patient_approve')

def patient_signup_admin(request):
    s = doctor.objects.all()
    context = {
        's': s
    }
    if (request.method == 'POST'):
        f_name = request.POST.get("fname")
        l_name = request.POST.get("lname")
        u_name = request.POST.get("uname")
        password = request.POST.get("password")
        u_address = request.POST.get("address")
        u_symptom = request.POST.get("symptom")
        u_profile=request.FILES.get("file")

        u_mobile = request.POST.get("mobile")
        u_doc=request.POST.get("doc")
        u_op = random.randint(10001, 99999)
        c = patient.objects.filter(op_num=u_op)

        while (c.count() > 0):
            u_op = random.randint(1000000001, 9999999999)
            c = patient.objects.filter(op_num=u_op)
            if (c.count() == 0):
                break

        if (c.count() == 0):

            rec = patient(doc_dep=u_doc,op_num=u_op,first_name=f_name, last_name=l_name, user_name=u_name, password=password, address=u_address, symptom=u_symptom, mobile=u_mobile,profile=u_profile,status='Admit')

            rec.save()
        # return render(request, 'patient_signup.html')
        return redirect(patient_record)

    return render(request,'patient_signup.html', context)
def discharge(request,id):

    if 'user' in request.session:
        current_user = request.session["user"]
        s = admin.objects.filter(user_name=current_user)

        if (request.method == 'POST'):
            print("request")
            r2 = appointment.objects.get(id=id)

            pat=patient.objects.filter(user_name=r2.patient_user_name)
            d_name = r2.doctor_user_name
            r3 = doctor.objects.get(user_name=d_name)
            u_name = r2.patient_user_name
            u_id=0
            for i in pat:
                u_id=i.id


            r4 = discharge_tb.objects.get(p_id_id=u_id,room_charge=0)


            c = 0

            r = request.POST.get('room_c')
            d = request.POST.get('doc_f')
            m = request.POST.get('med_c')
            o = request.POST.get('oth_c')
            r4.room_charge = r
            r4.doc_fee = d
            r4.medicine_cost = m
            r4.other_charge = o
            r4.total_charge =int(r)+int(d)+int(m)+int(o)
            r4.save()

            print(r)
            param = {
                'pat_id': id,
                'r': r,
                'd': d,
                'm': m,
                'o': o,
                'pat' :pat,
                'billl': 1,
                'current_user': current_user,
                's': s,
                'r2': r2,
                'r4': r4,
                'r3': r3,
                'c': c,
            }
            return render(request, 'admin_dash.html', param)
        else:
            a = appointment.objects.get(id=id)
            s2=[]

            s2=patient.objects.filter(user_name=a.patient_user_name)
            d_name = a.doctor_user_name
            doct = doctor.objects.get(user_name=d_name)
            u_name = a.patient_user_name
            u_id=0
            for i in s2:
                u_id = i.id
            rec = discharge_tb(patient_user_name=u_name, p_id_id=u_id, doctor_user_name=d_name)

            rec.save()
            disc = discharge_tb.objects.filter(p_id_id=u_id,room_charge=0)

            a.status = 'Discharged_by_admin'
            a.save()
            c = 0

            context = {
                'pat_id' : id,
                'discharge_v' : 1,
                'current_user': current_user,
                's': s,
                'a' :a,
                's2' : s2,
                'disc' :disc,
                'doct' : doct,
                'c' :c,
            }

            return render(request, 'admin_dash.html', context)


    else:
        return render(request, 'admin_dash.html')

def bill(request,pat_id):
    if 'user' in request.session:
        current_user = request.session["user"]
        s = admin.objects.filter(user_name=current_user)
        s2 = patient.objects.get(id=pat_id)
        d_name=s2.doc_dep
        doct=doctor.objects.get(user_name=d_name)

        disc=discharge_tb.objects.get(p_id_id=pat_id)



        c=0
        if (request.method == 'POST'):

            r = request.POST.get('room_c')
            d = request.POST.get('doc_f')
            m = request.POST.get('med_c')
            o = request.POST.get('oth_c')
            param = {
                'pat_id': id,
                'r' :r,
                'd' : d,
                'm' : m,
                'o' : o,
                'billl': 1,
                'current_user': current_user,
                's': s,
                's2': s2,
                'disc': disc,
                'doct': doct,
                'c': c,
            }
            return render(request, 'admin_dash.html', param)

        return render(request, 'admin_dash.html')
    else:
        return render(request, 'admin_dash.html')


# def discharge2(request,pk):
#     if 'user' in request.session:
#         current_user = request.session["user"]
#         s = admin.objects.filter(user_name=current_user)
#
#         s3=patient.objects.get(id=pk)
#
#
#
#
#         context = {
#
#             'current_user': current_user,
#             's': s,
#             'bill' : 1,
#
#         }
#
#         # return redirect('discharge_patient')
#         return render(request, 'admin_dash.html', context)
#     else:
#         return render(request, 'admin_dash.html')
def admin_appoint(request):
    if 'user' in request.session:
        current_user = request.session["user"]
        s = admin.objects.filter(user_name=current_user)


        context = {
            'admin_appoint' : 1,
            'current_user': current_user,
            's': s,


        }
        # return redirect('discharge_patient')
        return render(request, 'admin_dash.html', context)
    else:
        return render(request, 'admin_dash.html')

def admin_approve_appoint(request):
    if 'user' in request.session:
        current_user = request.session["user"]
        s = admin.objects.filter(user_name=current_user)
        a=appointment.objects.filter(status='Processing')

        context = {
            'admin_approve_appoint' : 1,
            'current_user': current_user,
            's': s,
            'a': a,

        }
        # return redirect('discharge_patient')
        return render(request, 'admin_dash.html', context)
    else:
        return render(request, 'admin_dash.html')

def app_approve(request,id):
    if 'user' in request.session:
        current_user = request.session["user"]
        s = admin.objects.filter(user_name=current_user)
        s2 = appointment.objects.get(id=id)
        s2.status = 'Booked'

        s2.save()
        d=doctor.objects.filter(user_name=s2.doctor_user_name)

        #
        #
        # s2.save()

        context = {

            'current_user': current_user,
            's' : s,
            's2': s2,


        }
        return redirect('admin_approve_appoint')
        # return render(request, 'admin_dash.html', context)
    else:
        return redirect('doctor_approve')
def app_reject(request,id):
    if 'user' in request.session:
        current_user = request.session["user"]
        s = admin.objects.filter(user_name=current_user)
        s2 = appointment.objects.get(id=id)
        s2.delete()
        context = {

            'current_user': current_user,
            's': s,

        }
        return redirect('admin_approve_appoint')
        # return render(request, 'admin_dash.html', context)
    else:
        return redirect('admin_approve_appoint')

def admin_book_appointment(request):
    if 'user' in request.session:
        current_user = request.session["user"]
        s = admin.objects.filter(user_name=current_user)
        a = appointment.objects.filter(status='Processing')
        d = doctor.objects.filter(status='Permanent')
        p=patient.objects.all()
        context = {
            'book_appoint': 1,
            'current_user': current_user,
            's': s,
            'a': a,
            'd' : d,
            'p' : p,
        }
        if (request.method == 'POST'):
            doc_name = ''
            pat_name=''
            desc = request.POST.get('description')
            user_doc = request.POST.get('special')
            print(user_doc)
            user_pat = request.POST.get('p_special')
            d1 = doctor.objects.filter(user_name=user_doc)
            p1 = patient.objects.filter(user_name=user_pat)
            for i in d1:
                doc_name=i.first_name+''+i.last_name
            for i in p1:
                pat_name=i.first_name+''+i.last_name
            rec = appointment(description=desc, doctor_name=doc_name,patient_name=pat_name,doctor_user_name=user_doc,patient_user_name=user_pat,status='Approved')
            rec.save()
            # return render(request, 'admin_dash.html', context)
            return redirect('admin_view_appoint')
        # return redirect('discharge_patient')
        return render(request, 'admin_dash.html', context)
    else:
        return render(request, 'admin_dash.html')

def admin_view_appoint(request):
    if 'user' in request.session:
        current_user = request.session["user"]
        s = admin.objects.filter(user_name=current_user)
        a = appointment.objects.filter(status='Booked')
        d = doctor.objects.filter(status='Permanent')

        context = {
            'admin_view_appoint': 1,
            'current_user': current_user,
            's': s,
            'a': a,
            'd' : d,

        }



        return render(request, 'admin_dash.html', context)
    else:
        return render(request, 'admin_dash.html')
def admit(request,id):
    if 'user' in request.session:
        current_user = request.session["user"]
        s = admin.objects.filter(user_name=current_user)
        s2 = appointment.objects.get(id=id)
        s2.status='Admit'
        s2.save()
        context = {

            'current_user': current_user,
            's': s,

        }
        return redirect('admin_approve_appoint')
        # return render(request, 'admin_dash.html', context)
    else:
        return redirect('admin_approve_appoint')
def admit_patient2(request):
    if 'user' in request.session:
        current_user = request.session["user"]
        s = admin.objects.filter(user_name=current_user)
        a = appointment.objects.filter(status='Processing(Admit)')
        p=[]
        for i in a:
            p=patient.objects.filter(user_name=i.patient_user_name)
        d = doctor.objects.filter(status='Permanent')

        context = {
            'admit_patient2': 1,
            'current_user': current_user,
            's': s,
            'a': a,
            'd' : d,
            'p' : p,
        }



        return render(request, 'admin_dash.html', context)
    else:
        return render(request, 'admin_dash.html')

def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('home')
    return redirect('home')






# -----------------------------------------------------------------------------------------------------------------



# DOCTOR DASHBOARD!!!!!!!!!!



# -----------------------------------------------------------------------------------------------------------


def doctor_signup(request):
    if (request.method == 'POST'):
        f_name = request.POST.get("fname")
        l_name = request.POST.get("lname")
        password = request.POST.get("password")
        u_address = request.POST.get("address")
        u_special = request.POST.get("special")
        u_profile = request.FILES.get("file")

        u_mobile = request.POST.get("mobile")
        u_name = request.POST.get("username")





        rec = doctor(first_name=f_name, last_name=l_name, user_name=u_name, password=password, address=u_address,
                         specialisation=u_special, mobile=u_mobile, profile=u_profile, status='On Hold')
        rec.save()

        return redirect(doctor_login)

    return render(request, 'doctor_signup.html')
def validate_username(request):
    u_name = request.GET.get("username")
    data={
        'is_taken' : doctor.objects.filter(user_name=u_name).exists()
    }
    if data['is_taken']:
        data['error_message']='user is taken'
    return JsonResponse(data)
def validate_password(request):
    u_name = request.GET.get("password")
    data={
        'is_taken' : doctor.objects.filter(password=u_name).exists()
    }
    if data['is_taken']:
        data['error_message']='password is taken'
    return JsonResponse(data)




def doctor_login(request):
    if (request.method == 'POST'):
        u_name = request.POST.get("uname")
        password = request.POST.get("password")

        rec = doctor.objects.filter(user_name=u_name, password=password)
        if rec:
            print("hi")
            request.session["doc_user"] = u_name

            return redirect('doctor_dash')
    return render(request,'doctor_login.html')

def doctor_dash(request):
    if 'doc_user' in request.session:
        current_user = request.session["doc_user"]
        s = doctor.objects.filter(user_name=current_user)
        w=0
        nw=0
        for i in s:
            if i.status=='On Hold':
                w=1
            else:
                nw=1



        context = {
            'current_user': current_user,
            's': s,
            'w' : w,
            'nw' : nw

        }
        return render(request, 'doctor_dash.html', context)
    else:
        return render(request, 'doctor_dash.html')
def doctor_dashboard(request):
    if 'doc_user' in request.session:
        current_user = request.session["doc_user"]
        s = doctor.objects.filter(user_name=current_user)
        s2=doctor.objects.order_by('-join_date')[:3]
        s3=doctor.objects.filter(status='On Hold')
        a=appointment.objects.filter(status='Booked',doctor_user_name=current_user)
        p1=patient.objects.filter(doc_dep=current_user,status='Registered')
        pat_c=p1.count()
        appoint_c=a.count()
        p=[]
        for i in a:
            p=patient.objects.filter(user_name=i.patient_user_name)
        count=s3.count()
        s4=doctor.objects.all()
        c=s4.count()

        context = {
            'dash': 1,
            'current_user': current_user,
            's': s,
            's2' : s2,
            'count' : count,
            'appoint_c' : appoint_c,
            'pat_c' : pat_c,
            'c' : c,
            'nw' : 1,
            'a' : a,
            'p' : p,
          }
        return render(request, 'doctor_dash.html', context)
    else:
        return render(request, 'doctor_dash.html')
def doctor_patient(request):
    if 'doc_user' in request.session:
        current_user = request.session["doc_user"]
        s = doctor.objects.filter(user_name=current_user)
        context = {
            'pat': 1,
            'current_user': current_user,
            's': s,
            'nw' : 1

        }
        return render(request, 'doctor_dash.html', context)
    else:
        return render(request, 'doctor_dash.html')
def doctor_appointment(request):
    if 'doc_user' in request.session:
        current_user = request.session["doc_user"]
        s = doctor.objects.filter(user_name=current_user)
        context = {
            'app': 1,
            'current_user': current_user,
            's': s,
            'nw' : 1

        }
        return render(request, 'doctor_dash.html', context)
    else:
        return render(request, 'doctor_dash.html')
def your_op_patient_record(request):
    global p1
    p1=[]
    if 'doc_user' in request.session:
        current_user = request.session["doc_user"]
        s = doctor.objects.filter(user_name=current_user)
        a = appointment.objects.filter(doctor_user_name=current_user, status='OP')
        for i in a:
            p1 = patient.objects.filter(doc_dep=i.doctor_user_name, status='Registered',user_name=i.patient_user_name)

        context = {
            'y_o_p_r': 1,
            'current_user': current_user,
            's': s,
            'nw': 1,
            'p1': p1,
            'a': a,

        }
        return render(request, 'doctor_dash.html', context)
    else:
        return render(request, 'doctor_dash.html')
def your_patient_record(request):
    global p1
    p1=[]
    if 'doc_user' in request.session:
        current_user = request.session["doc_user"]
        s = doctor.objects.filter(user_name=current_user)
        a=appointment.objects.filter(doctor_user_name=current_user,status='Admit')
        for i in a:

            p1 = patient.objects.filter(doc_dep=current_user,status='Registered',user_name=i.patient_user_name)


        context = {
            'y_p_r': 1,
            'current_user': current_user,
            's': s,
            'nw' : 1,
            'p1': p1,
            'a':a,

            }
        return render(request, 'doctor_dash.html', context)
    else:
        return render(request, 'doctor_dash.html')
def doctor_v_y_a(request):
    if 'doc_user' in request.session:
        current_user = request.session["doc_user"]
        s = doctor.objects.filter(user_name=current_user)
        a = appointment.objects.filter(status='Booked', doctor_user_name=current_user)
        p = []
        for i in a:
            p = patient.objects.filter(user_name=i.patient_user_name)
        context = {
            'v_y_a': 1,
            'current_user': current_user,
            's': s,
            'nw' : 1,
            'a' : a,
            'p' : p,

        }
        return render(request, 'doctor_dash.html', context)
    else:
        return render(request, 'doctor_dash.html')
def delete_appoint(request):
    if 'doc_user' in request.session:
        current_user = request.session["doc_user"]
        s = doctor.objects.filter(user_name=current_user)
        a = appointment.objects.filter(status='Booked', doctor_user_name=current_user)
        p = []
        for i in a:
            p = patient.objects.filter(user_name=i.patient_user_name)
        context = {
            'delete_a': 1,
            'current_user': current_user,
            's': s,
            'nw' : 1,
            'a' : a,
            'p' : p,

        }
        return render(request, 'doctor_dash.html', context)
    else:
        return render(request, 'doctor_dash.html')
def appoint_delete(request,id):

    if 'doc_user' in request.session:
        current_user = request.session["doc_user"]
        s = doctor.objects.filter(user_name=current_user)

        s2 = appointment.objects.get(id=id)
        s2.status='OP'
        s2.save()

        context = {
            'delete_a': 1,
            'current_user': current_user,
            's': s,
            'nw' : 1,


        }
        return redirect('delete_appoint')
    else:
        return render(request, 'doctor_dash.html')


def y_d_p(request):
    pat_rec=[]
    if 'doc_user' in request.session:
        current_user = request.session["doc_user"]
        s = doctor.objects.filter(user_name=current_user)
        dis=discharge_tb.objects.filter(doctor_user_name=current_user)
        for i in dis:
            pat_rec=patient.objects.filter(id=i.p_id_id)

        context = {
            'y_d_p': 1,
            'current_user': current_user,
            's': s,
            'nw' : 1,
            'dis' : dis,
            'pat_rec' : pat_rec,

        }

        return render(request, 'doctor_dash.html',context)
    else:
        return render(request, 'doctor_dash.html')
def IP(request,id):
    if 'doc_user' in request.session:
        current_user = request.session["doc_user"]
        s = doctor.objects.filter(user_name=current_user)

        s2 = appointment.objects.get(id=id)
        s2.status='Processing(Admit)'
        s2.save()

        context = {
            'delete_a': 1,
            'current_user': current_user,
            's': s,
            'nw' : 1,


        }
        return redirect('delete_appoint')
    else:
        return render(request, 'doctor_dash.html')
def doc_discharge(request,id):
    if 'doc_user' in request.session:
        current_user = request.session["doc_user"]
        s = doctor.objects.filter(user_name=current_user)

        s2 = appointment.objects.get(id=id)
        s2.status='Discharged'
        s2.save()


        context = {
            'doc_discharge': 1,
            'current_user': current_user,
            's': s,
            'nw' : 1,


        }
        return redirect('delete_appoint')
    else:
        return render(request, 'doctor_dash.html')

def doc_logout(request):
    try:
        del request.session['doc_user']
    except:
        return redirect('home')
    return redirect('home')



# ----------------------------------------------------------------------------------------------------------------

#  PATIENT DASHBOARD!!!!!!!!!!

# -----------------------------------------------------------------------------------------------------------------


def patient_home(request):
    return render(request, 'patient_home.html')
def patient_signup(request):
    s=doctor.objects.all()
    context={
        's' : s
    }
    for i in s:
        print(i.first_name)
    if (request.method == 'POST'):
        f_name = request.POST.get("fname")
        l_name = request.POST.get("lname")
        u_name = request.POST.get("uname")
        password = request.POST.get("password")
        u_address = request.POST.get("address")
        u_symptom = request.POST.get("symptom")
        u_profile=request.FILES.get("file")

        u_mobile = request.POST.get("mobile")
        u_doc=request.POST.get("doc")
        u_op = random.randint(10001, 99999)
        c = patient.objects.filter(op_num=u_op)
        name=f_name+' '+l_name
        d = doctor.objects.filter(user_name=u_doc)
        d_name=''
        for i in d :
            d_name=i.first_name+' '+i.last_name
        while (c.count() > 0):
            u_op = random.randint(1000000001, 9999999999)
            c = patient.objects.filter(op_num=u_op)
            if (c.count() == 0):
                break

        if (c.count() == 0):

            rec = patient(doc_dep=u_doc,op_num=u_op,first_name=f_name, last_name=l_name, user_name=u_name, password=password, address=u_address, symptom=u_symptom, mobile=u_mobile,profile=u_profile)
            rec.save()

        # return render(request, 'patient_signup.html')
        return redirect(patient_login)

    return render(request,'patient_signup.html', context)
def patient_login(request):
    # a=1
    if (request.method == 'POST'):
        a=0
        u_name = request.POST.get("uname")
        password = request.POST.get("password")
        rec = patient.objects.filter(user_name=u_name, password=password,)
        if rec:
            request.session["pat_user"] = u_name
            return redirect('patient_dash')

    # context = {
    #     'a': a
    # }
    return render(request,'patient_login.html')
def patient_dash(request):
    if 'pat_user' in request.session:
        current_user = request.session["pat_user"]
        s = patient.objects.filter(user_name=current_user)
        nw=0
        w=0
        for i in s:
            if i.status=='On Hold':
                w=1
            else:
                nw=1


        context = {
            'current_user': current_user,
            's': s,
            'w' : w,
            'nw' : nw

        }
        return render(request, 'patient_dash.html', context)
    else:
        return render(request, 'patient_dash.html')
def patient_dashboard(request):
    if 'pat_user' in request.session:
        current_user = request.session["pat_user"]
        s = patient.objects.filter(user_name=current_user)
        a=appointment.objects.filter(patient_user_name=current_user).order_by('-join_date')[:1]
        nw=0
        w=0
        for i in s:
            if i.status=='On Hold':
                w=1
            else:
                nw=1
        for i in a:
            d=doctor.objects.filter(user_name=i.doctor_user_name)

        context = {
            'current_user': current_user,
            'a':a,

            's': s,
            'd' : d,
            'w' : w,
            'nw' : nw,
            'dash' : 1,


        }
        return render(request, 'patient_dash.html', context)
    else:
        return render(request, 'patient_dash.html')

def patient_appointments(request):
    if 'pat_user' in request.session:
        current_user = request.session["pat_user"]
        s = patient.objects.filter(user_name=current_user)

        nw = 0
        w = 0
        d=[]
        for i in s:
            if i.status == 'On Hold':
                w = 1
            else:
                nw = 1
        for i in s:
            d = doctor.objects.filter(user_name=i.doc_dep)

        context = {
            'current_user': current_user,
            's': s,
            'd': d,
            'w': w,
            'nw': nw,
            'appoint': 1,

        }
        return render(request, 'patient_dash.html', context)
    else:
        return render(request, 'patient_dash.html')
def book_appoint(request):
    if 'pat_user' in request.session:
        current_user = request.session["pat_user"]
        s = patient.objects.filter(user_name=current_user)
        pat_name=''
        nw = 0
        w = 0
        for i in s:
            pat_name=i.first_name+''+i.last_name
            if i.status == 'On Hold':
                w = 1
            else:
                nw = 1

        d = doctor.objects.filter(status='Permanent')

        context = {
            'current_user': current_user,
            's': s,
            'd': d,
            'w': w,
            'nw': nw,
            'book_appoint': 1,

        }
        if (request.method == 'POST'):
            doc_name = ''
            desc = request.POST.get('description')
            user_doc = request.POST.get('special')
            ap_date=request.POST.get('book_date')
            d1 = doctor.objects.filter(user_name=user_doc)
            print(ap_date)
            for i in d1:
                doc_name=i.first_name+''+i.last_name

            rec = appointment(description=desc, doctor_name=doc_name,patient_name=pat_name,doctor_user_name=user_doc,patient_user_name=current_user,app_date=ap_date)
            rec.save()
            return redirect('view_your_appoint')
        return render(request, 'patient_dash.html', context)
    else:
        return render(request, 'patient_dash.html')


def view_your_appoint(request):
    if 'pat_user' in request.session:
        current_user = request.session["pat_user"]
        s = patient.objects.filter(user_name=current_user)

        nw=0
        w=0
        for i in s:
            if i.status=='On Hold':
                w=1
            else:
                nw=1
        name=''

        a=appointment.objects.filter(patient_user_name=current_user)
        # for i in a:
        #     d=doctor.objects.filter(user_name=i.doctor_name)
        #     for i in d:
        #         name=i.first_name



        context = {
            'current_user': current_user,
            's': s,
            'a' : a,
            'w' : w,
            'nw' : nw,
            'v_y_a' : 1,

            'name' : name,

        }
        return render(request, 'patient_dash.html', context)
    else:
        return render(request, 'patient_dash.html')
def patient_discharge(request):
    if 'pat_user' in request.session:
        current_user = request.session["pat_user"]
        s = patient.objects.filter(user_name=current_user)
        d_name=''
        disc=[]
        # start_date='0'
        for i in s:
            d_name = i.doc_dep
            disc = discharge_tb.objects.get(p_id_id=i.id)
            # start_date=time.mktime(i.join_date)
        # end_date=time.mktime(disc.release_date)
        # diff = (end_date - start_date)/86400
        # print(diff)
        doct = doctor.objects.get(user_name=d_name)


        c = 0
        d=0
        nd=0
        for i in s:
            if i.status=='Discharged':
                d=1
            else:
                nd=1
        nw = 0
        w = 0

        for i in s:
            if i.status == 'On Hold':
                w = 1

            else:
                nw = 1

        context = {
            'dis_w' : 1,
            'current_user': current_user,
            's': s,
            'w': w,
            'nw': nw,
            'd' : d,
            'nd' : nd,
            's2': s,
            'disc': disc,
            'doct': doct,
            'c': c,
        }
        return render(request, 'patient_dash.html', context)
    else:
        return render(request, 'patient_dash.html')
def pat_logout(request):
    try:
        del request.session['pat_user']
    except:
        return redirect('home')
    return redirect('home')


# ------------------------------------------------------------------------------------------------------------
