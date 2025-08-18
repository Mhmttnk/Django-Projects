from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES=[
    ('beklemede','Beklemede'),
    ('işleme alındı','İşleme Alındı'),
    ('hata giderildi', 'Hata Giderildi')
]

class ServiceItem(models.Model):
    brand = models.CharField(max_length = 15)
    model = models.CharField(max_length = 20)
    issue = models.TextField(max_length = 100)
    
    class Meta:
        abstract = True

class Computer(ServiceItem):
    PC_TYPE_CHOICES=[
        ('masaüstü','Masaüstü'),
        ('laptop','Laptop'),
    ]
    pc_type = models.CharField(max_length = 8, choices = PC_TYPE_CHOICES)
    user=models.ForeignKey(User, on_delete=models.CASCADE) #  Her kayıt ilgili kullanıcıya ait
    status = models.CharField(max_length = 15, choices = STATUS_CHOICES, default = 'beklemede')

class PlayerEquipment(ServiceItem, models.Model):
    equipment_type = models.CharField(max_length = 20)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    status = models.CharField(max_length = 15, choices = STATUS_CHOICES, default = 'beklemede')

class SmartPhone(ServiceItem):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    status = models.CharField(max_length = 15, choices = STATUS_CHOICES, default = 'beklemede')
 
class SmartWatch(ServiceItem):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    status = models.CharField(max_length = 15, choices = STATUS_CHOICES, default = 'beklemede')

class TV(ServiceItem):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    status = models.CharField(max_length = 15, choices = STATUS_CHOICES, default = 'beklemede')

class Tablet(ServiceItem):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    status = models.CharField(max_length = 15, choices = STATUS_CHOICES, default = 'beklemede')
