from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Reg
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,"home.html")
class Regview(View):
    def post(self,request):
        fn=request.POST["t1"]
        ln=request.POST["t2"]
        uname=request.POST["t3"]
        psw=request.POST["t4"]
        cpsw=request.POST["t5"]
        email=request.POST["t6"]
        mobno=request.POST["t7"]
        r1=Reg(FirstName=fn,LastName=ln,UserName=uname,Password=psw,ConfirmPassword=cpsw,EmailId=email,MobileNo=mobno)
        r1.save()
        return HttpResponse("Registration is successful")