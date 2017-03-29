from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    print("welcome to Virtuals Labs")
    return render(request, 'vlabs/course.html',{})

def computerScience(request):
    # print("hello")
    return render(request,'vlabs/ComputerScience.html',{})

def problemSolving(request):
    # print("helloq")
    # return HttpResponse("welcome")
    return render(request, "vlabs/problemSolving.html",{})