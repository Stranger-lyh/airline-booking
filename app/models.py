from django.db import models
# 账号信息
class Account(models.Model):
    id = models.CharField(max_length=64,primary_key=True)
    secret = models.CharField(max_length=64)

# 顾客信息
class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    acount_id = models.ForeignKey("Account",on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    tel_num = models.IntegerField()

# 会员等级信息
class VipLevel(models.Model):
    level_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    discount = models.IntegerField()

# 会员信息
class Vip(models.Model):
    id = models.IntegerField(primary_key=True)
    customer_id = models.ForeignKey("Customer",on_delete=models.CASCADE)
    level_id = models.ForeignKey("VipLevel",on_delete=models.CASCADE)

# 管理员信息
class Admin(models.Model):
    id = models.CharField(max_length=64,primary_key=True)
    secret = models.CharField(max_length=64)
    name = models.CharField(max_length=64)

# 机场信息
class Airport(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    place = models.CharField(max_length=64)

# 航线信息
class Route(models.Model):
    id = models.IntegerField(primary_key=True)
    startPort_id = models.ForeignKey("Airport",on_delete=models.CASCADE,related_name="startPort_id")
    arrivePort_id = models.ForeignKey("Airport",on_delete=models.CASCADE,related_name="arrivePort_id")

# 型号信息
class PlaneType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    capacity = models.IntegerField()
    voyage = models.IntegerField()

# 航空公司信息
class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)

# 飞机信息
class Plane(models.Model):
    id = models.IntegerField(primary_key=True)
    type_id = models.ForeignKey("PlaneType",on_delete=models.CASCADE)
    company_id = models.ForeignKey("Company",on_delete=models.CASCADE)
    work_time = models.IntegerField()


# 航班信息
class Flight(models.Model):
    id = models.IntegerField(primary_key=True)
    route_id = models.ForeignKey("Route",on_delete=models.CASCADE)
    plane_id = models.ForeignKey("Plane",on_delete=models.CASCADE)
    price = models.IntegerField()
    start_time = models.DateTimeField()
    arrive_time = models.DateTimeField()
    ticketNum = models.IntegerField()
""""
# 机票信息
class Ticket(models.Model):
    id = models.IntegerField(primary_key=True)
    flight_id = models.ForeignKey("Flight",on_delete=models.CASCADE)
    price = models.FloatField()
    status = models.CharField(max_length=64)
"""
# 托运信息:
class Consign(models.Model):
    id = models.IntegerField(primary_key=True)
    customer_id = models.ForeignKey("Customer",on_delete=models.CASCADE)
    fligth_id = models.ForeignKey("Flight",on_delete=models.CASCADE)
    weight = models.FloatField()

# 账单信息
class Bill(models.Model):
    id = models.IntegerField(primary_key=True)
    customer_id = models.ForeignKey("Customer",on_delete=models.CASCADE)
    #flight_id = models.ForeignKey("Flight",on_delete=models.CASCADE)
    consign_id = models.ForeignKey("Consign",on_delete=models.CASCADE)
    price = models.FloatField()
