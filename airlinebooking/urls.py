"""airlinebooking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('queryAllCompany/', views.Company.queryAllCompany),#查询航空公司
    path('queryAccount/', views.Account.queryAccount),#查询账户
    path('queryAdmin/', views.Account.queryAdmin),
    path('queryAllFlight/', views.Flight.queryAllFlight), #查询航班
    path('addCompany/', views.Company.addCompany), #添加航空公司
    path('deleteCompany/', views.Company.deleteCompany), #删除航空公司
    path('queryAllAirport/', views.Airport.queryAllAirport), #查询所有机场
    path('queryAirport/', views.Airport.queryAirport), #查询机场
    path('addAirport/', views.Airport.addAirport), #添加机场
    path('deleteAirport/', views.Airport.deleteAirport), #删除机场
    path('queryAllPlaneType/', views.PlaneType.queryAllPlaneType), #查询所有飞机型号
    path('queryPlaneType/', views.PlaneType.queryPlaneType), #查询指定飞机型号
    path('addPlaneType/', views.PlaneType.addPlaneType), #添加飞机型号
    path('deletePlaneType/', views.PlaneType.deletePlaneType), #删除飞机型号
    path('addRoute/', views.Route.addRoute), #添加新航线
    path('deleteRoute/', views.Route.deleteRoute), #删除航线
    path('addFlight/', views.Flight.addFlight), #添加航班
    path('deleteFlight/', views.Flight.deleteFlight), #删除航班
    path('addAccount/', views.Account.addAccount), #添加账户
    path('queryAllRoute/', views.Route.queryAllRoute), #查询所有航线
    path('queryAllPlane/',views.Plane.queryAllPlane), #查询所有飞机
    path('addPlane/',views.Plane.addPlane), #添加飞机
    path('deletePlane/',views.Plane.deletePlane), #删除飞机
    path('addBill/',views.Bill.addBill), #添加账单
    path('queryAllBill/',views.Bill.queryBill), #查询账单
    path('estimateBill/',views.Bill.estimateBill), #统计
]
"""""
# 初始添加数据
    path('addPort/',views.addPort),
    path('addCompany',views.addCompany),
    path('addPlaneType',views.addPlaneType),
    path('addVipLevel',views.addVipLevel),
    path('addAccount',views.addAccount),
    path('addCustomer',views.addCustomer),
    path('addRoute',views.addRoute),
    path('addPlane/',views.addPlane),
    path('addAdmin/',views.addAdmin),
    path('addFlight/',views.addFlight),
    path('addTicket/',views.addTicket),
    path('addVip/',views.addVip),
"""""
