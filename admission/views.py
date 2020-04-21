from django.shortcuts import render,HttpResponse
from .models import *

def admissionform(request):
    if request.POST:
        first_name = request.POST.get('first_name',False)
        middle_name = request.POST.get('middle_name',False)
        last_name = request.POST.get('last_name',False)
        english_dob = request.POST.get('english_dob',False)
        nepali_dob = request.POST.get('nepali_dob',False)
        gender = request.POST.get('gender',False)
        address = request.POST.get('address',False)
        admission_for_grade = request.POST.get('admission_for_grade',False)
        last_school = request.POST.get('last_school',False)
        father_name = request.POST.get('father_name', False)
        father_occupation = request.POST.get('father_occupation', False)
        father_mobile = request.POST.get('father_mobile', False)
        father_office = request.POST.get('father_office', False)
        father_office_phone = request.POST.get('father_office_phone', False)
        father_email = request.POST.get('father_email', False)
        mother_name = request.POST.get('mother_name', False)
        mother_occupation = request.POST.get('mother_occupation', False)
        mother_mobile = request.POST.get('mother_mobile', False)
        mother_office = request.POST.get('mother_office', False)
        mother_office_phone = request.POST.get('mother_office_phone', False)
        mother_email = request.POST.get('mother_email', False)
        local_name = request.POST.get('local_name',False)
        local_relation = request.POST.get('local_relation',False)
        local_phone = request.POST.get('local_phone',False)
        local_email = request.POST.get('local_email',False)
        local_mobile = request.POST.get('local_mobile',False)
        local_occupation = request.POST.get('local_occupation',False)
        bus_required = request.POST.get('bus_required',False)
        bus_pickup = request.POST.get('bus_pickup',False)
        disease_details = request.POST.get('disease_details',False)
        medication_details = request.POST.get('medication_details',False)
        admission_form = AdmissionForm.objects.create(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            english_dob=english_dob,
            nepali_dob=nepali_dob,
            gender=gender,
            address=address,
            admission_for_grade=admission_for_grade,
            last_school=last_school,
            father_name=father_name,
            father_office=father_office,
            father_email=father_email,
            father_mobile=father_mobile,
            father_occupation=father_occupation,
            father_office_phone=father_office_phone,
            mother_email=mother_email,
            mother_mobile=mother_mobile,
            mother_occupation=mother_occupation,
            mother_office=mother_office,
            mother_office_phone=mother_office_phone,
            mother_name=mother_name,
            local_email= local_email,
            local_name=local_name,
            local_relation=local_relation,
            local_mobile=local_mobile,
            local_occupation=local_occupation,
            local_phone=local_phone,
            bus_required=bus_required,
            bus_pickup=bus_pickup,
            disease_details=disease_details,
            medication_details=medication_details,
        )
        admission_form.save()
        return render(request,'admission/successfull.html',{})
    return render(request,"admission/index.html",{})

