from django.db import models

class AdmissionForm(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50)
    english_dob = models.DateField()
    nepali_dob = models.DateField()
    gender = models.CharField(max_length=10,choices=(
        ('Male','Male'),
        ('Female','Female'),
    ))
    address = models.TextField()
    admission_for_grade = models.CharField(max_length=50)
    last_school = models.CharField(max_length=255,null=True,blank=True)
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)
    father_mobile = models.CharField(max_length=15)
    father_office = models.CharField(max_length=250,null=True,blank=True)
    father_office_phone = models.CharField(max_length=15,null=True,blank=True)
    father_email = models.EmailField(null=True,blank=True)
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100,null=True,blank=True)
    mother_mobile = models.CharField(max_length=15,null=True,blank=True)
    mother_office = models.CharField(max_length=250,null=True,blank=True)
    mother_office_phone = models.CharField(max_length=15,null=True,blank=True)
    mother_email = models.EmailField(null=True,blank=True)
    local_name = models.CharField(max_length=100,null=True,blank=True)
    local_relation = models.CharField(max_length=50,null=True,blank=True)
    local_mobile = models.CharField(max_length=15,null=True,blank=True)
    local_phone = models.CharField(max_length=15,null=True,blank=True)
    local_email = models.EmailField(null=True,blank=True)
    local_occupation = models.CharField(max_length=255,null=True,blank=True)
    bus_required = models.CharField(max_length=5,choices=(
        ('Yes','Yes'),
        ('No','No')
    ))
    bus_pickup = models.CharField(max_length=250,null=True,blank=True)
    disease_details = models.TextField(null=True,blank=True)
    medication_details = models.TextField(null=True,blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} , {self.admission_for_grade}'