from django.http import JsonResponse
from .models import Candidate
# Create your views here.
def save_personal_in_session(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        dob = request.POST.get('dob')
        cur_loc = request.POST.get('cur_loc')
        job_loc = request.POST.get('job_loc')

        if any([fname, lname, email, mobile, dob, cur_loc, job_loc]):
            request.session['fname'] = fname
            request.session['lname'] = lname
            request.session['email'] = email
            request.session['mobile'] = mobile
            request.session['dob'] = dob
            request.session['cur_loc'] = cur_loc
            request.session['job_loc'] = job_loc
            return JsonResponse({'Status': 'Personal Data Updated In Session'})
        else:
            return JsonResponse({'error': 'Fill the form below submitting!!'}, status=422)
    return JsonResponse({'error': 'Wrong Request'}, status=405)

def save_edu_in_session(request):
    if request.method == 'POST':
        tenth = request.POST.get('tenth')
        tenth_yr = request.POST.get('tenth_yr')
        twelfth = request.POST.get('twelfth')
        twelfth_yr = request.POST.get('twelfth_yr')
        degree = request.POST.get('degree')
        degree_score = request.POST.get('degree_score')
        degree_yr = request.POST.get('degree_yr')

        if any([tenth, tenth_yr, twelfth, twelfth_yr, degree, degree_score, degree_yr]):
            request.session['tenth'] = tenth
            request.session['tenth_yr'] = tenth_yr
            request.session['twelfth'] = twelfth
            request.session['twelfth_yr'] = twelfth_yr
            request.session['degree'] = degree
            request.session['degree_score'] = degree_score
            request.session['degree_yr'] = degree_yr
            return JsonResponse({'Status': 'Educational Data Updated In Session'})
        else:
            return JsonResponse({'error': 'Fill the form below submitting!!'}, status=422)
    return JsonResponse({'error': 'Wrong Request'}, status=405)

def db_insert(request):
    params = []
    if request.method == 'POST':
        cur_designation = request.POST.get('cur_designation')
        exp_designation = request.POST.get('exp_designation')
        cur_salary = request.POST.get('cur_salary')
        exp_salary = request.POST.get('exp_salary')
        notice_days = request.POST.get('notice_days')
        params.extend([cur_designation,exp_designation])
        params.extend([cur_salary, exp_salary, notice_days])

        firstname = request.session['fname']
        lastname = request.session['lname']
        email = request.session['email']
        mobile = request.session['mobile']
        dob = request.session['dob']
        cur_loc = request.session['cur_loc']
        job_loc = request.session['job_loc']
        params.extend([firstname,lastname,email,mobile,dob,cur_loc,job_loc])
        
        tenth = request.session['tenth']
        tenth_yr = request.session['tenth_yr']
        twelfth = request.session['twelfth']
        twelfth_yr = request.session['twelfth_yr']
        degree = request.session['degree']
        degree_score = request.session['degree_score']
        degree_yr = request.session['degree_yr']
        params.extend([tenth, tenth_yr, twelfth, twelfth_yr,degree])
        params.extend([degree_score, degree_yr])
        print(params, 77777)

        if all(params):
            Candidate.objects.create(
                firstname=firstname, lastname=lastname,
                mobile=mobile, email=email, dob=dob,
                cur_loc=cur_loc, job_loc=job_loc,
                tenth=tenth, tenth_yr=tenth_yr,
                twelfth=twelfth, twelfth_yr=twelfth_yr,
                degree=degree, degree_score=degree_score,
                degree_yr=degree_yr, 
                cur_designation=cur_designation,
                exp_designation=exp_designation,
                cur_salary=cur_salary, exp_salary=exp_salary,
                notice_days=notice_days
            )
            return JsonResponse({'Status': 'Profile updated, You will get updates on Job openings'})
        else:
            return JsonResponse({'error': 'Fill the form below submitting!!'}, status=422)
    return JsonResponse({'error': 'Wrong Request'}, status=405)