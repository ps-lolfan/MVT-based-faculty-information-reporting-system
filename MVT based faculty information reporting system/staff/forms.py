from django import forms
from staff.models import  Personal_Details, Bachelors_Degree, Masters_degree, Phd_Degree, Experience_Details, \
    Publication_Details, Workshop_Details, Patents_Details, Grants_Fetched, Grants_Applied, Awards_Details, Bank_Details, \
    Course_Details, facultydetails, register44

from staff.models import Department

class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ('name', 'acronym','code','estd','location')


class registerForm44(forms.ModelForm):

    class Meta:
        model = register44
        fields = ('name','email','department','mobile','designation')















class personaldetailsForm(forms.ModelForm):
    class Meta:
        model = Personal_Details
        fields = ('firstname','middlename','lastname','dateofbirth','emailid','mobile','alternatemobile','aadharnumber','pancardnumber','bloodgroup','street','pincode','city','district','state','dateofjoining','departmentname','designation')

class bachelordetailsForm(forms.ModelForm):
    class Meta:
        model =  Bachelors_Degree
        fields = ('degreename','collegename','University','yearofpassing','result','percentage')

class masterdetailsForm(forms.ModelForm):
    class Meta:
        model =  Masters_degree
        fields = ('degreename','collegename','University','yearofpassing','result','percentage')

class phddetailsForm(forms.ModelForm):
    class Meta:
        model = Phd_Degree
        fields = ('degreename','collegename','specification','University','yearofpassing','result','percentage')


class experiencedetailsForm(forms.ModelForm):
    class Meta:
        model = Experience_Details
        fields = ('institutename','joiningdate','designation','hikename','scale','enddate','address','state')

class publicationdetailsForm(forms.ModelForm):
    class Meta:
        model = Publication_Details
        fields = ('titleofpublication','authorname','year','titleofpaper','volume','pagenumbers','impact','reviewer','journalname')


class workshopdetailsForm(forms.ModelForm):
    class Meta:
        model = Workshop_Details
        fields = ('presentationlevel','type','sourceoffunding','paper','name','description','country','state','startdate','date','hostorganization','eventname','area','resourceperson','place','numberofparticipants','briefdescription','amountfaculty','modeofpayment','amountuniversity')


class patentsdetailsForm(forms.ModelForm):
    class Meta:
        model = Patents_Details
        fields = ('title','name','holder','datesubmitprovisional','datesubmitcomplete','datepublication','remarks')


class grantsfetchedForm(forms.ModelForm):
    class Meta:
        model = Grants_Fetched
        fields = ('projectname','grantissuedby','grantedamount','grantdate','coauthors','address','description')


class grantsappliedForm(forms.ModelForm):
    class Meta:
        model = Grants_Applied
        fields = ('date', 'projectname', 'agency', 'grantamount', 'address', 'description')


class awardsdetailsForm(forms.ModelForm):
    class Meta:
        model = Awards_Details
        fields = ('awardname','awardinstitution','date','description')

class bankdetailsForm(forms.ModelForm):
    class Meta:
        model = Bank_Details
        fields = ('bankname','accountnumber','branchname','ifsccode','city','state')


class coursedetailsForm(forms.ModelForm):
    class Meta:
        model = Course_Details
        fields = ('name','code','credit','created','department','semester','coursedescription')


class facultydetailsForm(forms.ModelForm):
    class Meta:
        model = facultydetails
        fields =('name','email','department','mobile','joining','facultycourse','designation')