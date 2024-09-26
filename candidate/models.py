from django.db import models

# Create your models here.
class Candidate(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=60, primary_key=True)
    mobile = models.CharField(max_length=50)
    dob = models.DateField()
    cur_loc = models.CharField(max_length=50)
    job_loc = models.CharField(max_length=50)
    tenth = models.CharField(max_length=3)
    tenth_yr = models.DateField()
    twelfth = models.CharField(max_length=3)
    twelfth_yr = models.DateField()
    degree = models.CharField(max_length=15)
    degree_score = models.CharField(max_length=3)
    degree_yr = models.DateField()
    cur_designation = models.CharField(max_length=50)
    exp_designation = models.CharField(max_length=50)
    cur_salary = models.CharField(max_length=15)
    exp_salary = models.CharField(max_length=15)
    notice_days = models.IntegerField()