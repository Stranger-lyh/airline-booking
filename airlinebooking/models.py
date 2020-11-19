from django.db import models

# 顾客信息
class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    acount_id = models.IntegerField()
    name = models.CharField()
    tel_num = models.IntegerField()

# 账号信息
class Account(models.Model):
    id = models.IntegerField(primary_key=True)
    secret = models.CharField()

# 会员信息
class Vip(models.Model):
    id = models.IntegerField(primary_key=True)
    customer_id = models.IntegerField()
    level_id = models.CharField()

# 会员等级信息
class VipLevel(models.Model):
    level_id = models.IntegerField(primary_key=True)
    name = models.CharField()
    discount = models.IntegerField()

# 管理员信息
class Admin(models.Model):
    id = models.IntegerField(primary_key=True)
    secret = models.CharField()
    name = models.CharField()

# 机票信息
class Ticket(models.Model):
    id = models.IntegerField(primary_key=True)
    flight_id = models.IntegerField()
    price = models.FloatField()
    status = models.CharField()

# 账单信息
class Bill(models.Model):
    id = models.IntegerField(primary_key=True)
    customer_id = models.IntegerField()
    ticket_id = models.IntegerField()
    price = models.FloatField()

# 航班信息
class Flight:
    id = models.IntegerField(primary_key=True)
    route_id = models.IntegerField()
    plane_id = models.IntegerField()
    company_id = models.IntegerField()
    start_time = models.DateTimeField()
    arrive_time = models.DateTimeField()

# 飞机信息
class Plane:
    id = models.IntegerField(primary_key=True)
    type_id = models.IntegerField()
    work_time = models.IntegerField()

# 型号信息
class PlaneType:
    id = models.IntegerField(primary_key=True)
    capacity = models.IntegerField()
    voyage = models.IntegerField()

# 机场信息
class Airport:
    id = models.IntegerField(primary_key=True)
    name = models.CharField()
    place = models.CharField()

# 航线信息
class Route:
    id = models.IntegerField(primary_key=True)
    startPort_id = models.IntegerField()
    arrivePort_id = models.IntegerField()

# 航空公司信息
class Company:
    id = models.IntegerField(primary_key=True)
    name = models.CharField()

# 托运信息:
class Consign:
    id = models.IntegerField(primary_key=True)
    customer_id = models.IntegerField()
    fligth_id = models.IntegerField()
    weight = models.FloatField()