from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from django.http import HttpResponse,JsonResponse
import json

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
    t.save()
    '''
    body = json.loads(request.body.decode('utf-8'))
    t = models.Airport(name=body['airport'], place=body['place'])
    t.save()
    '''
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
    t = models.Flight(route_id=route_obj,plane_id=plane_obj,price=800,start_time=start_time,
                      arrive_time = end_time,ticketNum=cnt)
    t.save()
    return HttpResponse("<p>数据添加成功！</p>")

'''''
def addTicket(request):
    flight_obj = models.Flight.objects.get(id=1)
    models.Ticket.objects.create(flight_id=flight_obj,price=800,status="未被售出")
    return HttpResponse("<p>数据添加成功！</p>")
'''''
def addVip(request):
    t_obj = models.Customer.objects.get(id=1)
    l_obj = models.VipLevel.objects.get(level_id=2)
    models.Vip.objects.create(customer_id=t_obj,level_id=l_obj)
    return HttpResponse("<p>数据添加成功！</p>")

def queryAccount(request):
    if request.method == "GET":
        ret = models.Account.objects.all()
        json_list = []
        for i in ret:
            json_dict = {}
            json_dict["id"] = i.id
            json_dict["secret"] = i.secret

            json_list.append(json_dict)
        ret1 = json.dumps(json_list)
        return HttpResponse(ret1, content_type="application/json")

def queryAdmin(request):
    if request.method == "GET":
        ret = models.Admin.objects.all()
        json_list = []
        for i in ret:
            json_dict = {}
            json_dict["id"] = i.id
            json_dict["name"] = i.name
            json_dict["secret"] = i.secret
            json_list.append(json_dict)
        ret1 = json.dumps(json_list)
        return HttpResponse(ret1, content_type="application/json")


# 航空公司
class Company:
    # 查询操作
    def queryAllCompany(request):
        if request.method == "GET":
            ret = models.Company.objects.all()
            json_list = []
            for i in ret:
                json_dict = {}
                json_dict["id"] = i.id
                json_dict["name"] = i.name

                json_list.append(json_dict)
            ret1 = json.dumps(json_list)
            return HttpResponse(ret1,content_type="application/json")
    # 添加操作
    def addCompany(request):
        if request.method == "POST":
            body = json.loads(request.body.decode('utf-8'))
            if models.Company.objects.filter(name=body['name']):
                return HttpResponse("name已存在！",status=400)
            else:
                models.Company.objects.create(name=body['name'])
                return HttpResponse("<p>数据添加成功！</p>")

    def deleteCompany(request):
        if request.method == "DELETE":
            body = json.loads(request.body.decode('utf-8'))
            models.Company.objects.filter(id = body['id']).delete()
            return HttpResponse("<p>数据删除成功！</p>")

# 机场
class Airport:
    # 查询操作
    def queryAllAirport(request):
        if request.method == "GET":
            ret = models.Airport.objects.all()
            json_list = []
            for i in ret:
                json_dict = {}
                json_dict["id"] = i.id
                json_dict["name"] = i.name
                json_dict["place"] = i.place
                json_list.append(json_dict)
            ret1 = json.dumps(json_list)
            return HttpResponse(ret1, content_type="application/json")

    def queryAirport(request):
        if request.method == "GET":
            json_dict = {}
            json_dict["name"] = models.Airport.objects.get(id = request.GET.get("id")).name
            json_dict["place"] = models.Airport.objects.get(id = request.GET.get("id")).place
            ret1 = json.dumps(json_dict)
            return HttpResponse(ret1, content_type="application/json")

    def addAirport(request):
        if request.method == "POST":
            body = json.loads(request.body.decode('utf-8'))
            if models.Airport.objects.filter(name=body['name']):
                return HttpResponse("name已存在！",status=400)
            else:
                models.Airport.objects.create(name=body['name'],place=body['place'])
                return HttpResponse("<p>数据添加成功！</p>")

    def deleteAirport(request):
        if request.method == "DELETE":
            body = json.loads(request.body.decode('utf-8'))
            models.Airport.objects.filter(id = body['id']).delete()
            return HttpResponse("<p>数据删除成功！</p>")

# 飞机型号
class PlaneType:
    def queryAllPlaneType(request):
        if request.method == "GET":
            ret = models.PlaneType.objects.all()
            json_list = []
            for i in ret:
                json_dict = {}
                json_dict["id"] = i.id
                json_dict["name"] = i.name
                json_dict["capacity"] = i.capacity
                json_dict["voyage"] = i.voyage
                json_list.append(json_dict)
            ret1 = json.dumps(json_list)
            return HttpResponse(ret1, content_type="application/json")

    def queryPlaneType(request):
        if request.method == "GET":
            json_dict = {}
            json_dict["name"] = models.PlaneType.objects.get(id = request.GET.get("id")).name
            json_dict["capacity"] = models.PlaneType.objects.get(id = request.GET.get("id")).capacity
            json_dict["voyage"] = models.PlaneType.objects.get(id = request.GET.get("id")).voyage
            ret1 = json.dumps(json_dict)
            return HttpResponse(ret1, content_type="application/json")

    def addPlaneType(request):
        if request.method == "POST":
            body = json.loads(request.body.decode('utf-8'))
            if models.PlaneType.objects.filter(name=body['name']):
                return HttpResponse("name已存在！",status=400)
            else:
                models.PlaneType.objects.create(name=body['name'], capacity=body['capacity'],voyage = body['voyage'])
                return HttpResponse("<p>数据添加成功！</p>")

    def deletePlaneType(request):
        if request.method == "DELETE":
            body = json.loads(request.body.decode('utf-8'))
            models.PlaneType.objects.filter(id=body['id']).delete()
            return HttpResponse("<p>数据删除成功！</p>")

class Route:
    def addRoute(request):
        if request.method == "POST":
            body = json.loads(request.body.decode('utf-8'))
            models.Route.objects.create(startPort_id=models.Airport.objects.get(id=body["id1"]), arrivePort_id=models.Airport.objects.get(id=body["id2"]))
            return HttpResponse("<p>数据添加成功！</p>")

    def deleteRoute(request):
        if request.method == "DELETE":
            body = json.loads(request.body.decode('utf-8'))
            models.Route.objects.filter(id=body['id']).delete()
            return HttpResponse("<p>数据删除成功！</p>")

# 航班
class Flight:
    def queryAllFlight(request):
        if request.method == "GET":
            ret = models.Flight.objects.all()
            json_list = []
            for i in ret:
                json_dict = {}
                json_dict["id"] = i.id
                json_dict["startPortName"] = i.route_id.startPort_id.name;
                json_dict["startPorPlace"] = i.route_id.startPort_id.place;
                json_dict["arrivePortName"] = i.route_id.arrivePort_id.name;
                json_dict["arrivePortPlace"] = i.route_id.arrivePort_id.place;
                json_dict["companyName"] = i.plane_id.company_id.name;
                json_dict["price"] = i.price
                json_dict["startTime"] = i.start_time.strftime("%Y-%m-%d %H:%M:%S");
                json_dict["arriveTime"] = i.arrive_time.strftime("%Y-%m-%d %H:%M:%S");
                json_dict["Typename"] = i.plane_id.type_id.name;
                json_dict["Capacity"] = i.plane_id.type_id.capacity;
                json_dict["MaxVoyage"] = i.plane_id.type_id.voyage;
                json_dict["leftTicket"] = i.ticketNum;
                json_list.append(json_dict)
            ret1 = json.dumps(json_list)
            return HttpResponse(ret1, content_type="application/json")

    def addFlight(request):
        if request.method == "POST":
            body = json.loads(request.body.decode('utf-8'))
            models.Flight.objects.create(route_id=models.Route.objects.get(id=body["route_id"]),
                                        plane_id=models.Plane.objects.get(id=body["plane_id"]),
                                         price=body["price"],
                                         start_time=body["time1"],
                                         arrive_time=body["time2"],
                                         ticketNum=body["num"])
            return HttpResponse("<p>数据添加成功！</p>")

    def deleteFlight(request):
        if request.method == "DELETE":
            body = json.loads(request.body.decode('utf-8'))
            models.Flight.objects.filter(id=body['id']).delete()
            return HttpResponse("<p>数据删除成功！</p>")
