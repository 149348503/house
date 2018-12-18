from django.shortcuts import render

# Create your views here.
def index_login(request):
    return render(request,'login.html')


def index_main(request):
    return render(request,'main.html')


def index_top(request):
    return render(request,'top.html')


def index_left(request):
    return render(request,'left.html')


def index_center(request):
    return render(request,'center.html')