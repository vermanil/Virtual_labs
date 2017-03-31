from django.shortcuts import render
from django.http import HttpResponse
from .models import problemSolving_course, List_of_labs, Task
import smtplib

# Create your views here.
sender_email = "enter Email id"
sender_passwd = "password of that"
reciever_email = "reciever email id"

def index(request):
    print("welcome to Virtuals Labs")
    return render(request, 'vlabs/course.html',{})

def computerScience(request):
    # print("hello")
    return render(request,'vlabs/ComputerScience.html',{})

def problemSolving(request):
    # print("helloq")
    # return HttpResponse("welcome")
    struct = problemSolving_course.objects.all()
    return render(request, "vlabs/problemSolving.html",{'struct': struct, "action": "Intro"})

def totalLabs(request):
    labs = List_of_labs.objects.all()
    return render(request, "vlabs/problemSolving.html",{'struct': labs, "action": "lab"})

def targetaudience(request):
    struct = problemSolving_course.objects.all()
    return render(request, "vlabs/problemSolving.html", {'struct': struct, "action": "Audience"})

def topic(request):
    struct = problemSolving_course.objects.all()
    return render(request, "vlabs/problemSolving.html", {'struct': struct, "action": "Topic"})

def feedback(request):
    if request.method == 'POST':
        print(request.POST.keys())
        Name = request.POST.get('name')
        # sender = request.POST.get('email')
        message = request.POST.get('des')
        msg = "Sent by " + Name + " " + message
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_passwd)
        server.sendmail(sender_email, reciever_email, msg)
        server.quit()
    else:
        return render(request, "vlabs/feedback.html", {"action" : "Feedback"})

def lab(request, name):
    # print(name)
    lab = List_of_labs.objects.get(list_of_labs=name)
    # print(lab.Introduction)
    return render(request, "vlabs/LAB.html",{"lab":lab, "labNo": name,"action":"Introduction"})

def task(request,name):
    # print(request.path)
    print(name)
    # lab = Task.objects.all()
    m = int(name[len(name)-1])
    lab = Task.objects.filter(labNo=m)
    # print(lab.list_of_labs)
    # return HttpResponse("hello")
    return render(request, "vlabs/LAB.html", {"lab": lab, "labNo": name, "action":"task"})

def objective(request,name):
    # print(request.path)
    print(name)
    lab = List_of_labs.objects.get(list_of_labs=name)
    # return HttpResponse("hello")
    return render(request, "vlabs/LAB.html", {"lab": lab, "labNo": name, "action":"objective"})
