from django.shortcuts import render
from .models import Moive
from Spider import myThread
import time
# Create your views here.
def index(request):
    thread1 = myThread()
    thread1.start()
    context = Moive.objects.all()
    real_time = time.ctime()
    return render(request,'index.html',context={'Movie':context,'Time':real_time})