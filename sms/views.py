from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from . import naive_bayes
import datetime

from .models import Data

def index(request):
    return render(request, 'sms/index.html')

def analyze(request):
    text = request.POST['sms-text']
    if text:
        
        pred, status = naive_bayes.pred(text)
        data = {'pred': pred, 'text': text, 'status': status}

        save_db = Data(text=text, prediction=pred, created_at=datetime.datetime.now())
        save_db.save()

        return render(request, 'sms/index.html', {'data': data})

    return HttpResponseRedirect(reverse('index'))
