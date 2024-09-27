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

def save_exp_in_session(request):
    if request.method == 'POST':
        cur_designation = request.POST.get('cur_designation')
        exp_designation = request.POST.get('exp_designation')
        cur_salary = request.POST.get('cur_salary')
        exp_salary = request.POST.get('exp_salary')
        notice_days = request.POST.get('notice_days')
        data = [cur_designation, exp_designation, cur_salary]
        data.extend([exp_salary, notice_days])
        print(data, 789)
        if any(data):
            request.session['cur_designation'] = cur_designation
            request.session['exp_designation'] = exp_designation
            request.session['cur_salary'] = cur_salary
            request.session['exp_salary'] = exp_salary
            request.session['notice_days'] = notice_days
            return JsonResponse({'Status': 'Experience Data Updated In Session'})
        else:
            return JsonResponse({'error': 'Fill the form below submitting!!'}, status=422)
    return JsonResponse({'error': 'Wrong Request'}, status=405)

def get_session_data(request):
    data = ""
    data += f"firstname: <b>{request.session['fname']}</b><br>"
    data += f"lastname: <b>{request.session['lname']}</b><br>"
    data += f"email: <b>{request.session['email']}</b><br>"
    data += f"mobile: <b>{request.session['mobile']}</b><br>"
    data += f"dob: <b>{request.session['dob']}</b><br>"
    data += f"cur_loc: <b>{request.session['cur_loc']}</b><br>"
    data += f"job_loc: <b>{request.session['job_loc']}</b><br>"

    data += f"tenth: <b>{request.session['tenth']}</b><br>"
    data += f"tenth_yr: <b>{request.session['tenth_yr']}</b><br>"
    data += f"twelfth: <b>{request.session['twelfth']}</b><br>"
    data += f"twelfth_yr: <b>{request.session['twelfth_yr']}</b><br>"
    data += f"degree: <b>{request.session['degree']}</b><br>"
    data += f"degree_score: <b>{request.session['degree_score']}</b><br>"
    data += f"degree_yr: <b>{request.session['degree_yr']}</b><br>"

    data += f"cur_designation: <b>{request.session['cur_designation']}</b><br>"
    data += f"exp_designation: <b>{request.session['exp_designation']}</b><br>"
    data += f"cur_salary: <b>{request.session['cur_salary']}</b><br>"
    data += f"exp_salary: <b>{request.session['exp_salary']}</b><br>"
    data += f"notice_days: <b>{request.session['notice_days']}</b><br>"

    return JsonResponse({'data': data})
    


def db_insert(request):
    params = []
    if request.method == 'GET':
        cur_designation = request.session['cur_designation']
        exp_designation = request.session['exp_designation']
        cur_salary = request.session['cur_salary']
        exp_salary = request.session['exp_salary']
        notice_days = request.session['notice_days']
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

def delete_session(request):
    request.session.delete()
    return JsonResponse({'Status': 'Session Cleared'})