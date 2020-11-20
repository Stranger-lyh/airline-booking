from django.shortcuts import render
from django.shortcuts import render,HttpResponse

# Create your views here.
from app import models
def add(request):
    test1 = models.Airport(name="双流机场",place="成都")
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")