from django.contrib import admin
from .models import Computer,PlayerEquipment,SmartPhone,SmartWatch,TV,Tablet

admin.site.register(Computer)
admin.site.register(SmartPhone)
admin.site.register(SmartWatch)
admin.site.register(TV)
admin.site.register(PlayerEquipment)
admin.site.register(Tablet)