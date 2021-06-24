from django.shortcuts import render

# Create your views here.
from myapp.models import project,project1,IMG
from myapp.models import project2,project3,project4
from django.http import HttpResponse

def title(request):
    projectlist = project.objects.all()
    return render(request,'myapp/project.html',{'name':projectlist})

def index(request):
    return HttpResponse(r'ddx的广告投放分析网页')

def uploadimg(request):
    if request.method == 'POST':
        new_img = IMG(
            img=request.FILES.get('img')
            )
                     
        new_img.save()
    return render(request,'myapp/uploadimg.html')

def showimg(request):
    imgs = IMG.objects.all()
    content = {
        'imgs' : imgs,
        }
    return render(request,'myapp/showimg.html',content)


    
def Project1(request):
    project1list = project1.objects.all()
    return render(request,'myapp/project1.html',{'project1':project1list})

def Project2(request):
    project2list = project2.objects.all()
    return render(request,"myapp/project2.html",{"project2":project2list})

def Project3(request):
    project3list = project3.objects.all()
    return render(request,"myapp/project3.html",{"project3":project3list})

def Project4(request):
    project4list = project4.objects.all()
    return render(request,"myapp/project4.html",{"project4":project4list})
