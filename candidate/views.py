from django.http import JsonResponse

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
        degree_yr = request.POST.get('degree')

        if any([tenth, tenth_yr]):
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
