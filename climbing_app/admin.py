from django.contrib import admin
from . import models 
admin.site.register(models.ClimbingLocation)
admin.site.register(models.ClimbingGym)
admin.site.register(models.LocationArea)
admin.site.register(models.SportRoute)
admin.site.register(models.SportRouteImage)
admin.site.register(models.Boulder)
admin.site.register(models.BoulderImage)
admin.site.register(models.BoulderRoute)
