from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+ 1
    context = {
        'num_visits': num_visits
    }
    return render(request, 'session_app/index.html', context)

def ping(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)