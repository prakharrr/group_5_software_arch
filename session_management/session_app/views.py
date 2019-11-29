from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'session_app/index.html', context)

def ping(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)