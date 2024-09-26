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


