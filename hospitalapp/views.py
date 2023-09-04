from django.shortcuts import render, redirect
from .models import admin, doctor,patient
import random


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
        s2=doctor.objects.order_by('-join_date')[:3]
        p1 = patient.objects.order_by('-join_date')[:3]
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
            'count' : count,
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
            'pat': 1,
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
        s2 = patient.objects.filter(status='Admit')
        for i in s2:
            print(i.first_name)
        context = {
            'discharge_patient' : 1,
            'current_user': current_user,
            's': s,
            's2': s2,

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
            return redirect(doctor_login)
    else:
        return render(request, 'doctor_signup.html')

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
        u_name = request.POST.get("uname")
        password = request.POST.get("password")
        u_address = request.POST.get("address")
        u_special = request.POST.get("special")
        u_profile=request.FILES.get("file")

        u_mobile = request.POST.get("mobile")
        # if 'user' in request.session:
        #     current_user = request.session["user"]
        #     rec = doctor(first_name=f_name, last_name=l_name, user_name=u_name, password=password, address=u_address,
        #                  specialisation=u_special, mobile=u_mobile, profile=u_profile,status='Permanent')
        # else:
        rec = doctor(first_name=f_name, last_name=l_name, user_name=u_name, password=password, address=u_address, specialisation=u_special, mobile=u_mobile,profile=u_profile,status='On Hold')
        # if rec.is_valid():
        rec.save()
        return redirect(doctor_login)

    return render(request, 'doctor_signup.html')


def doctor_login(request):
    if (request.method == 'POST'):
        u_name = request.POST.get("uname")
        password = request.POST.get("password")
        rec = doctor.objects.filter(user_name=u_name, password=password)
        if rec:
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
        count=s3.count()
        s4=doctor.objects.all()
        c=s4.count()
        for i in s2:
            print(i.user_name)
        context = {
            'dash': 1,
            'current_user': current_user,
            's': s,
            's2' : s2,
            'count' : count,
            'c' : c,
            'nw' : 1

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
def your_patient_record(request):
    global p1
    if 'doc_user' in request.session:
        current_user = request.session["doc_user"]
        s = doctor.objects.filter(user_name=current_user)

        for i in s:
            print(i.user_name)
            p1 = patient.objects.filter(doc_dep=i.user_name)


        context = {
            'y_p_r': 1,
            'current_user': current_user,
            's': s,
            'nw' : 1,
            'p1': p1

            }
        return render(request, 'doctor_dash.html', context)
    else:
        return render(request, 'doctor_dash.html')
# ----------------------------------------------------------------------------------------------------------------
# Patient
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
        rec = patient.objects.filter(user_name=u_name, password=password)
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
            'nw' : nw,
            'dash' : 1

        }
        return render(request, 'patient_dash.html', context)
    else:
        return render(request, 'patient_dash.html')

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
        s2.status = 'Admit'
        s2.save()
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
        return redirect(patient_login)

    return render(request,'patient_signup.html', context)
def discharge(request,id):
    if 'user' in request.session:
        current_user = request.session["user"]
        s = admin.objects.filter(user_name=current_user)
        s2 = patient.objects.get(id=id)

        context = {
            'discharge' : 1,
            'current_user': current_user,
            's': s,


        }
        # return redirect('discharge_patient')
        return render(request, 'admin_dash.html', context)
    else:
        return render(request, 'admin_dash.html')

