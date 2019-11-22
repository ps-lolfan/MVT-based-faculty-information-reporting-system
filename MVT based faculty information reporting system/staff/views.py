# Create your views here.
import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from mysite.common_utils import CommonUtils
from staff.forms import personaldetailsForm, bachelordetailsForm, \
    masterdetailsForm, phddetailsForm, experiencedetailsForm, publicationdetailsForm, workshopdetailsForm, \
    patentsdetailsForm, grantsfetchedForm, grantsappliedForm, awardsdetailsForm, bankdetailsForm, coursedetailsForm, \
    facultydetailsForm, registerForm44
from staff.forms import DepartmentForm
from django.http.response import HttpResponseRedirect
from staff.models import Department, register44, Personal_Details, facultydetails, Bachelors_Degree, Experience_Details, \
    Publication_Details
from django.contrib import messages


# Create your views here.


#
def viwer(request):
    return HttpResponseRedirect('/staff/dashboard')


# to view the login page for Admin
def log(request):
    return render(request, 'login4.html')


# view to come back Admin dashboard
def backk(request):
    return render(request, 'dashboard.html')


# to view login page for HOD
def log2(request):
    return render(request, 'login5.html')


# to view login page for Faculty
def log3(request):
    return render(request, 'login6.html')


def log4(request):
    return render(request, 'login5.html')


# TO view details of Faculties in HOD dashboard
def view_Faculty(request):
    if request.method == 'GET':
        queryset = facultydetails.objects.filter(department='MCA').only("name", "department", "email", "mobile",
                                                                        "facultycourse", "designation")
        return render(request, 'viewFaculty.html',
                      {'staff': queryset})


# view for deleteing faculties in HOd dashboard
def delete_Faculty(request):
    return render(request, 'deleteFaculty.html')


# view faculty report in HOD dashboard
def view_Report(request):
    return render(request, 'viewReport.html')


def homes(request):
    return render(request, 'homepage.html')


# To view a home page
def hp(request):
    return render(request, 'homepage.html')


def faculty_home(request):
    return render(render, 'facultydashboard.html')


# To view HOD dashboard
def hod_dashboard(request):
    return render(request, 'dashboard2.html')


# ---------------------------------------------------------------------------------------------------

# login view(login code) for Admin dashboard
def seen(request):
    if request.method == 'GET':
        return render(request, 'login4.html')
    else:
        validate_user = authenticate(
            username=request.POST['username'],
            password=request.POST['password'])
        if validate_user:
            login(request, validate_user)
            return render(request, 'dashboard.html')
        else:
            return render(request, 'login4.html')


# --------------------------------------------------------------------------------------------

# login view (login code) for Faculty dashboard
def seener(request):
    if request.method == 'GET':
        return render(request, 'login6.html')
    else:
        validate_user = authenticate(
            username=request.POST['username'],
            password=request.POST['password'])
        if validate_user:
            login(request, validate_user)
            return render(request, 'facultydashboard.html')
        else:
            return render(request, 'login6.html')


# login view(login code) for HOD Dashboard
def seens(request):
    if request.method == 'GET':
        return render(request, 'login5.html')
    else:
        validate_user = authenticate(
            username=request.POST['username'],
            password=request.POST['password'])
        if validate_user:
            login(request, validate_user)
            return render(request, 'dashboard2.html')
        else:
            return render(request, 'login5.html')


# view to insert department in Admin dashboard
def insert_department(request):
    if request.method == 'POST':
        department_form = DepartmentForm(request.POST)
        if department_form.is_valid():
            post_department = department_form.save(commit=False)
            post_department.save()
            return HttpResponseRedirect('/staff/adddept')
    if request.method == 'GET':
        return render(request, 'adddept.html')


# view to add HODS in Admin dashboard
def insert_hod(request):
    if request.method == 'POST':
        department_form = registerForm44(request.POST)
        if department_form.is_valid():
            new_user = User.objects.create_user(
                username=request.POST['email'],
                password=request.POST['password'])

            post_department = department_form.save(commit=False)
            post_department.user = new_user

            post_department.save()
            return HttpResponseRedirect('/staff/addhod')
    if request.method == 'GET':
        return render(request, 'addhod.html')


# TO view all departments in Admin dashboard
def depttview(request):
    if request.method == 'GET':
        department = list(Department.objects.all())
        return render(request, 'view.html',
                      {'staff': department})


# TO view all HOD dept:MCA in Admin dashboard
def view_hod(request):
    if request.method == 'GET':
        queryset = register44.objects.filter(designation='HOD', department='MCA').only("name", "department")
        return render(request, 'viewhod.html',
                      {'staff': queryset})


# TO delete the department iin Admin dashboard
def dept_delete(request):
    if request.method == 'POST':
        acronym = request.POST['acronym']
        Department.objects.filter(
            acronym__iexact=acronym
        ).delete()
        return HttpResponseRedirect('/staff/deptdelete')
    else:
        return render(request,
                      'deptdelete.html')


# view to insert personl details of faculty in faclty dashboard

def insert_personal(request):
    message = ''
    priority = ''
    title = ''
    if request.method == 'POST':
        personaldetails_form = personaldetailsForm(request.POST)
        print(personaldetails_form.errors)
        if personaldetails_form.is_valid():
            if request.POST['edit_personaldetails']:
                if Personal_Details.objects.filter(
                        mobile=request.POST['mobile']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    personaldetails_records = CommonUtils().fetch_department(str(request.user))
                    return render(request, 'personal.html',
                                  {'personaldetails_records': personaldetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                personaldetails_content = {
                    'firstname' : request.POST['firstname'],
                    'middlename' : request.POST['middlename'],
                    'lastname' : request.POST['lastname'],
                    'dateofbirth' : request.POST['dateofbirth'],
                    'emailid' : request.POST['emailid'],
                    'mobile' : request.POST['mobile'],
                    'alternatemobile' : request.POST['alternatemobile'],
                    'aadharnumber' : request.POST['aadharnumber'],
                    'pancardnumber' : request.POST['pancardnumber'],
                    'bloodgroup' : request.POST['bloodgroup'],
                    'street' : request.POST['street'],
                    'pincode' : request.POST['pincode'],
                    'city': request.POST['city'],
                    'district': request.POST['district'],
                    'state': request.POST['state'],
                    'dateofjoining': request.POST['dateofjoining'],
                    'departmentname': request.POST['departmentname'],
                    'designation': request.POST['designation'],
                }
                Personal_Details.objects.filter(
                    id=request.POST['edit_personaldetails']).update(
                        **personaldetails_content)
                message = 'Data Updated !!'
                priority = 'success'
                title = 'Data updated'
            else:
                if Personal_Details.objects.filter(
                        mobile=request.POST['mobile']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    personaldetails_records = CommonUtils().fetch_department(str(request.user))
                    return render(request, 'personal.html',
                                  {'personaldetails_records': personaldetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                post_personaldetails = personaldetails_form.save(commit=False)
                post_personaldetails.user = request.user
                post_personaldetails.save()
                message = 'Data saved !!'
                priority = 'success'
                title = 'Data saved'
            personaldetails_records = CommonUtils().fetch_department(str(request.user))
            return render(request, 'personal.html',
                          {'personaldetails_records': personaldetails_records,
                           'message': message, 'title': title,
                           'priority': priority})
    if request.method == 'GET':
        personaldetails_records = CommonUtils().fetch_department(str(request.user))
        return render(request, 'personal.html',
                      {'personaldetails_records': personaldetails_records,
                       'message': message, 'title': title,
                       'priority': priority})


# view to inseert bachelor degree details of faculty in faculty dashboard
def add_bachelor(request):
    message = ''
    priority = ''
    title = ''
    if request.method == 'POST':
        bachelordetails_form = bachelordetailsForm(request.POST)
        print(bachelordetails_form.errors)
        if bachelordetails_form.is_valid():
            if request.POST['edit_bachelordetails']:
                if Bachelors_Degree.objects.filter(
                        degreename=request.POST['degreename']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    bachelordetails_records = CommonUtils().fetch_bachelor(str(request.user))
                    return render(request, 'bachelor.html',
                                  {'bachelordetails_records': bachelordetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                bachelordetails_content = {
                    'degreename': request.POST['degreename'],
                    'collegename': request.POST['collegename'],
                    'University': request.POST['University'],
                    'yearofpassing': request.POST['yearofpassing'],
                    'result': request.POST['result'],
                    'percentage': request.POST['percentage'],

                }
                Bachelors_Degree.objects.filter(
                    id=request.POST['edit_bachelordetails']).update(
                    **bachelordetails_content)
                message = 'Data Updated !!'
                priority = 'success'
                title = 'Data updated'
            else:
                if Bachelors_Degree.objects.filter(
                        degreename=request.POST['degreename']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    bachelordetails_records = CommonUtils().fetch_bachelor(str(request.user))
                    return render(request, 'bachelor.html',
                                  {'bachelordetails_records': bachelordetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                post_bachelordetails = bachelordetails_form.save(commit=False)
                post_bachelordetails.user = request.user
                post_bachelordetails.save()
                message = 'Data saved !!'
                priority = 'success'
                title = 'Data saved'
            bachelordetails_records = CommonUtils().fetch_bachelor(str(request.user))
            return render(request, 'bachelor.html',
                          {'bachelordetails_records': bachelordetails_records,
                           'message': message, 'title': title,
                           'priority': priority})
    if request.method == 'GET':
        bachelordetails_records = CommonUtils().fetch_bachelor(str(request.user))
        return render(request, 'bachelor.html',
                      {'bachelordetails_records': bachelordetails_records,
                       'message': message, 'title': title,
                       'priority': priority})


def view_personal(request):
    return render(request, 'facultyview.html')


# view to inseert master degree details of faculty in faculty dashboard
def add_master(request):
    if request.method == 'POST':
        department_form = masterdetailsForm(request.POST)
        if department_form.is_valid():
            post_department = department_form.save(commit=False)
            post_department.save()
            messages.success(request, 'INSERTED SUCCESSFULLY!!')
            return render(request, 'facultydashboard.html')
    if request.method == 'GET':
        return render(request, 'master.html')


# view to inseert phd degree details of faculty in faculty dashboard
def add_phd(request):
    if request.method == 'POST':
        department_form = phddetailsForm(request.POST)
        if department_form.is_valid():
            post_department = department_form.save(commit=False)
            post_department.save()
            messages.success(request, 'INSERTED SUCCESSFULLY!!')
            return render(request, 'phd.html')
    if request.method == 'GET':
        return render(request, 'phd.html')


# view to inseert experience details of faculty in faculty dashboard
def add_experience(request):
    message = ''
    priority = ''
    title = ''
    if request.method == 'POST':
        personaldetails_form = experiencedetailsForm(request.POST)
        print(personaldetails_form.errors)
        if personaldetails_form.is_valid():
            if request.POST['edit_personaldetails']:
                if Experience_Details.objects.filter(
                        institutename=request.POST['institutename']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    personaldetails_records = CommonUtils().fetch_experience(str(request.user))
                    return render(request, 'teachingExp.html',
                                  {'personaldetails_records': personaldetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                personaldetails_content = {
                    'institutename': request.POST['institutename'],
                    'joiningdate': request.POST['joiningdate'],
                    'designation': request.POST['designation'],
                    'hikename': request.POST['hikename'],
                    'scale': request.POST['scale'],
                    'enddate': request.POST['enddate'],
                    'address': request.POST['address'],
                    'state': request.POST['state'],

                }
                Experience_Details.objects.filter(
                    id=request.POST['edit_personaldetails']).update(
                    **personaldetails_content)
                message = 'Data Updated !!'
                priority = 'success'
                title = 'Data updated'
            else:
                if Experience_Details.objects.filter(
                        institutename=request.POST['institutename']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    personaldetails_records = CommonUtils().fetch_experience(str(request.user))
                    return render(request, 'teachingExp.html',
                                  {'personaldetails_records': personaldetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                post_personaldetails = personaldetails_form.save(commit=False)
                post_personaldetails.user = request.user
                post_personaldetails.save()
                message = 'Data saved !!'
                priority = 'success'
                title = 'Data saved'
            personaldetails_records = CommonUtils().fetch_experience(str(request.user))
            return render(request, 'teachingExp.html',
                          {'personaldetails_records': personaldetails_records,
                           'message': message, 'title': title,
                           'priority': priority})
    if request.method == 'GET':
        personaldetails_records = CommonUtils().fetch_experience(str(request.user))
        return render(request, 'teachingExp.html',
                      {'personaldetails_records': personaldetails_records,
                       'message': message, 'title': title,
                       'priority': priority})


# view to inseert publication details of faculty in faculty dashboard
def add_publication(request):
    message = ''
    priority = ''
    title = ''
    if request.method == 'POST':
        publicationdetails_form = publicationdetailsForm(request.POST)
        print(publicationdetails_form.errors)
        if publicationdetails_form.is_valid():
            if request.POST['edit_publicationdetails']:
                if Publication_Details.objects.filter(
                        titleofpublication=request.POST['titleofpublication']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    publicationdetails_records = CommonUtils().fetch_publication(str(request.user))
                    return render(request, 'publications.html',
                                  {'publicationdetails_records': publicationdetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                publicationdetails_content = {
                    'titleofpublication': request.POST['titleofpublication'],
                    'authorname': request.POST['authorname'],
                    'year': request.POST['year'],
                    'titleofpaper': request.POST['titleofpaper'],
                    'volume': request.POST['volume'],
                    'pagenumbers': request.POST['pagenumbers'],
                    'impact': request.POST['impact'],
                    'reviewer': request.POST['reviewer'],
                    'journalname': request.POST['journalname'],

                }
                Publication_Details.objects.filter(
                    id=request.POST['edit_publicationdetails']).update(
                    **publicationdetails_content)
                message = 'Data Updated !!'
                priority = 'success'
                title = 'Data updated'
            else:
                if Publication_Details.objects.filter(
                        titleofpublication=request.POST['titleofpublication']).count() > 1:
                    message = 'Data Exists!!'
                    priority = 'error'
                    title = 'Data already exists'
                    publicationdetails_records = CommonUtils().fetch_publication(str(request.user))
                    return render(request, 'publications.html',
                                  {'publicationdetails_records': publicationdetails_records,
                                   'message': message, 'title': title,
                                   'priority': priority})
                post_publicationdetails = publicationdetails_form.save(commit=False)
                post_publicationdetails.user = request.user
                post_publicationdetails.save()
                message = 'Data saved !!'
                priority = 'success'
                title = 'Data saved'
            publicationdetails_records = CommonUtils().fetch_publication(str(request.user))
            return render(request, 'publications.html',
                          {'publicationdetails_records': publicationdetails_records,
                           'message': message, 'title': title,
                           'priority': priority})
    if request.method == 'GET':
        publicationdetails_records = CommonUtils().fetch_publication(str(request.user))
        return render(request, 'publications.html',
                      {'publicationdetails_records': publicationdetails_records,
                       'message': message, 'title': title,
                       'priority': priority})


# To view the facuulty dashboard
def add_home(request):
    if request.method == 'GET':
        return render(request, 'facultydashboard.html')


# view to inseert workshop details of faculty in faculty dashboard
def add_workshop(request):
    if request.method == 'POST':
        department_form = workshopdetailsForm(request.POST)
        if department_form.is_valid():
            post_department = department_form.save(commit=False)
            post_department.save()
            # messages.success(request, 'INSERTED SUCCESSFULLY!!')
            return render(request, 'workshops.html')
    if request.method == 'GET':
        return render(request, 'workshops.html')


# view to inseert patents details of faculty in faculty dashboard
def add_patents(request):
    if request.method == 'POST':
        department_form = patentsdetailsForm(request.POST)
        if department_form.is_valid():
            post_department = department_form.save(commit=False)
            post_department.save()
            # messages.success(request, 'INSERTED SUCCESSFULLY!!')
            return render(request, 'patents.html')
    if request.method == 'GET':
        return render(request, 'patents.html')


# view to inseert grantsfetched details of faculty in faculty dashboard
def add_grantsfetched(request):
    if request.method == 'POST':
        department_form = grantsfetchedForm(request.POST)
        if department_form.is_valid():
            post_department = department_form.save(commit=False)
            post_department.save()
            # messages.success(request, 'INSERTED SUCCESSFULLY!!')
            return render(request, 'grantsfetched.html')
    if request.method == 'GET':
        return render(request, 'grantsfetched.html')


# view to inseert grants Applied details of faculty in faculty dashboard
def add_grantsapplied(request):
    if request.method == 'POST':
        department_form = grantsappliedForm(request.POST)
        if department_form.is_valid():
            post_department = department_form.save(commit=False)
            post_department.save()
            # messages.success(request, 'INSERTED SUCCESSFULLY!!')
            return render(request, 'grantsapplied.html')
    if request.method == 'GET':
        return render(request, 'grantsapplied.html')


# view to inseert Awards details of faculty in faculty dashboard
def add_awards(request):
    if request.method == 'POST':
        department_form = awardsdetailsForm(request.POST)
        if department_form.is_valid():
            post_department = department_form.save(commit=False)
            post_department.save()
            # messages.success(request, 'INSERTED SUCCESSFULLY!!')
            return render(request, 'awards.html')
    if request.method == 'GET':
        return render(request, 'awards.html')


# view to inseert Bank details of faculty in faculty dashboard
def add_bank(request):
    if request.method == 'POST':
        department_form = bankdetailsForm(request.POST)
        if department_form.is_valid():
            post_department = department_form.save(commit=False)
            post_department.save()
            messages.success(request, 'INSERTED SUCCESSFULLY!!')
            return render(request, 'addbank.html')
    if request.method == 'GET':
        return render(request, 'addbank.html')


# view to inseert course details  in HOD dashboard
def add_Course(request):
    if request.method == 'POST':
        department_form = coursedetailsForm(request.POST)
        if department_form.is_valid():
            post_department = department_form.save(commit=False)
            post_department.save()
            messages.success(request, 'INSERTED SUCCESSFULLY!!')
            return render(request, 'addCourse.html')
    if request.method == 'GET':
        return render(request, 'addCourse.html')


# view to add the faculties  in HOD dashboard
def add_Faculty(request):
    if request.method == 'POST':
        department_form = facultydetailsForm(request.POST)
        if department_form.is_valid():
            new_user = User.objects.create_user(
                username=request.POST['email'],
                password=request.POST['password'])

            post_department = department_form.save(commit=False)
            post_department.user = new_user

            post_department.save()
            return HttpResponseRedirect('/staff/addFaculty')
    if request.method == 'GET':
        return render(request, 'addFaculty.html')


def insert_personaldetails(request):
    if request.method == 'POST':
        department_form = personaldetailsForm(request.POST)
        if department_form.is_valid():
            post_department = department_form.save(commit=False)
            post_department.save()
            # messages.success(request, 'INSERTED SUCCESSFULLY!!')
            return HttpResponseRedirect('/staff/viewww')
    if request.method == 'GET':
        return render(request, 'insertpersonal.html')


