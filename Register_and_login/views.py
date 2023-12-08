from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'Register_and_login/index.html',{})