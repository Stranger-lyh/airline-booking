from django.shortcuts import render
from django.shortcuts import render,HttpResponse

# Create your views here.
from app import models
def addPort(request):
    test1 = models.Airport(name="双流国际机场",place="成都")
    test1.save()
    t = models.Airport(name="首都国际机场",place="北京")
    t.save()
    t = models.Airport(name="浦东国际机场",place="上海")
    t.save()
    t = models.Airport(name="白云国际机场",place="广州")
    return HttpResponse("<p>数据添加成功！</p>")

# 添加航空公司信息
def addCompany(request):
    t = models.Company(name="中国国际航空公司")
    t.save()
    t1 = models.Company(name="中国南方航空公司")
    t1.save()
    t2 = models.Company(name="东方航空公司")
    t2.save()
    return HttpResponse("<p>数据添加成功！</p>")

# 添加型号信息
def addPlaneType(request):
    t = models.PlaneType(name="波音737",capacity=150,voyage=3000)
    t.save()
    t = models.PlaneType(name="空客A320",capacity = 80,voyage=6000)
    t.save()
    return HttpResponse("<p>数据添加成功！</p>")

# 会员等级信息
def addVipLevel(request):
    t = models.VipLevel(name="铂金卡",discount = 7)
    t.save()
    t = models.VipLevel(name="金卡",discount= 8)
    t.save()
    t = models.VipLevel(name="银卡",discount = 9)
    t.save()
    return HttpResponse("<p>数据添加成功！</p>")

def addAccount(request):
    t = models.Account(id="aaa",secret="123456")
    t.save()
    return HttpResponse("<p>数据添加成功！</p>")

def addCustomer(request):
    ac_obj = models.Account.objects.get(id="aaa")
    t = models.Customer(name="张三",acount_id=ac_obj,tel_num=155555555)
    t.save()
    return HttpResponse("<p>数据添加成功！</p>")

def addRoute(request):
    start_obj = models.Airport.objects.get(name="双流国际机场")
    end_obj = models.Airport.objects.get(name="首都国际机场")
    t = models.Route(startPort_id=start_obj,arrivePort_id=end_obj)
    t.save()
    return HttpResponse("<p>数据添加成功！</p>")

def addPlane(request):
    t_obj = models.PlaneType.objects.get(id=1)
    c_obj = models.Company.objects.get(id = 1)
    t = models.Plane(type_id=t_obj,company_id=c_obj,work_time=2)
    t.save()
    t_obj = models.PlaneType.objects.get(id=2)
    c_obj = models.Company.objects.get(id=2)
    t = models.Plane(type_id=t_obj, company_id=c_obj,work_time=4)
    t.save()
    return HttpResponse("<p>数据添加成功！</p>")

def addAdmin(request):
    t = models.Admin(id="admin",secret="admin",name="管理员")
    t.save()
    return HttpResponse("<p>数据添加成功！</p>")


def addFlight(request):
    route_obj = models.Route.objects.get(id=1)
    plane_obj = models.Plane.objects.filter(pk=1).first()

    company_obj = models.Company.objects.get(id=1)
    cnt = 150
    start_time = "2020-10-1 14:00:00"
    end_time = "2020-10-1 16:00:00"
    t = models.Flight(route_id=route_obj,plane_id=plane_obj,company_id=company_obj,start_time=start_time,
                      arrive_time = end_time,ticketNum=cnt)
    t.save()
    return HttpResponse("<p>数据添加成功！</p>")

def addTicket(request):
    flight_obj = models.Flight.objects.get(id=1)
    models.Ticket.objects.create(flight_id=flight_obj,price=800,status="未被售出")
    return HttpResponse("<p>数据添加成功！</p>")

def addVip(request):
    t_obj = models.Customer.objects.get(id=1)
    l_obj = models.VipLevel.objects.get(level_id=2)
    models.Vip.objects.create(customer_id=t_obj,level_id=l_obj)
    return HttpResponse("<p>数据添加成功！</p>")

