from staff.models import Personal_Details, Bachelors_Degree, Experience_Details, Publication_Details


class CommonUtils:

    def fetch_department(self, pd='all'):
        if pd.lower() == 'all':
            department_records = Personal_Details.objects.all()
        else:
            department_records = Personal_Details.objects.filter(emailid=pd)
        department_list = []
        for elements, item in enumerate(department_records):
            department_dict = {}
            department_dict["id"] = item.id
            department_dict["firstname"] = item.firstname
            department_dict["middlename"] = item.middlename
            department_dict["lastname"] = item.lastname
            department_dict["dateofbirth"] = str(item.dateofbirth)
            department_dict["emailid"] = item.emailid
            department_dict["mobile"] = item.mobile
            department_dict["alternatemobile"] = item.alternatemobile
            department_dict["aadharnumber"] = item.aadharnumber
            department_dict["pancardnumber"] = item.pancardnumber
            department_dict["bloodgroup"] = item.bloodgroup
            department_dict["street"] = item.street
            department_dict["pincode"] = item.pincode
            department_dict["city"] = item.city
            department_dict["district"] = item.district
            department_dict["state"] = item.state
            department_dict["dateofjoining"] = str(item.dateofjoining)
            department_dict["departmentname"] = item.departmentname
            department_dict["designation"] = item.designation

            department_list.append(department_dict)
        return department_list





    def fetch_bachelor(self, pd='all'):
        if pd.lower() == 'all':
            bachelor_records = Bachelors_Degree.objects.all()
        else:
            bachelor_records = Bachelors_Degree.objects.filter(degreename=pd)
        bachelor_list = []
        for elements, item in enumerate(bachelor_records):
            bacelor_dict = {}
            bacelor_dict["id"] = item.id
            bacelor_dict["degreename"] = item.degreename
            bacelor_dict["collegename"] = item.collegename
            bacelor_dict["University"] = item.University
            bacelor_dict["yearofpassing"] = str(item.yearofpassing)
            bacelor_dict["result"] = item.result
            bacelor_dict["percentage"] = item.percentage


            bachelor_list.append(bacelor_dict)
        return bachelor_list





    def fetch_experience(self, pd='all'):
        if pd.lower() == 'all':
            department_records = Experience_Details.objects.all()
        else:
            department_records = Experience_Details.objects.filter(institutename=pd)
        department_list = []
        for elements, item in enumerate(department_records):
            department_dict = {}
            department_dict["id"] = item.id
            department_dict["institutename"] = item.institutename
            department_dict["joiningdate"] = str(item.joiningdate)
            department_dict["designation"] = item.designation
            department_dict["hikename"] = item.hikename
            department_dict["scale"] = item.scale
            department_dict["enddate"] = str(item.enddate)
            department_dict["address"] = item.address
            department_dict["state"] = item.state


            department_list.append(department_dict)
        return department_list





    def fetch_publication(self, pd='all'):
        if pd.lower() == 'all':
            department_records = Publication_Details.objects.all()
        else:
            department_records = Publication_Details.objects.filter(titleofpublication=pd)
        department_list = []
        for elements, item in enumerate(department_records):
            department_dict = {}
            department_dict["id"] = item.id
            department_dict["titleofpublication"] = item.titleofpublication
            department_dict["authorname"] = item.authorname
            department_dict["year"] = str(item.year)
            department_dict["titleofpaper"] = item.titleofpaper
            department_dict["volume"] = item.volume
            department_dict["pagenumbers"] = item.pagenumbers
            department_dict["impact"] = item.impact
            department_dict["reviewer"] = item.reviewer
            department_dict["journalname"] = item.journalname


            department_list.append(department_dict)
        return department_list





