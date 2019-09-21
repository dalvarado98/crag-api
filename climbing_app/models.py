from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

class Province:
    HEREDIA = 'HE'
    ALAJUELA = 'AL'
    SAN_JOSE = 'SJ'
    CARTAGO = 'CA'
    GUANACASTE = 'GU'
    LIMON = 'LI'
    PROVINCE_CHOICES = [
        (HEREDIA, 'Heredia'),
        (ALAJUELA, 'Alajuela'),
        (SAN_JOSE, 'San Jose'),
        (CARTAGO, 'Cartago'),
        (GUANACASTE, 'Guanacaste'),
        (LIMON, 'Limon'),
    ]

class VGrade: 
    V_GRADE_VALUE = ['V'+str(a) for a in range(17)]
    V_GRADE_OPTIONS = list(zip(V_GRADE_VALUE, V_GRADE_VALUE))

class FontGrade: 
    FONT_GRADE_VALUE = [str(a) + b + c for a in range(4, 10) for b in ['A', 'B', 'C'] for c in ['', '+']]
    FONT_GRADE_OPTIONS = list(zip(FONT_GRADE_VALUE, FONT_GRADE_VALUE))

class YDSGrade:
    YDS_GRADE_VALUE = ['5.' + str(a) for a in range(4,10)] + ['5.' + str(a) + b for a in range(10, 16) for b in ['a', 'b', 'c', 'd']]
    YDS_GRADE_OPTIONS = list(zip(YDS_GRADE_VALUE, YDS_GRADE_VALUE))

class ClimbingLocation(models.Model, Province):
    climbing_location_id = models.AutoField(primary_key=True)
    coordinates = models.CharField(max_length=250, unique=True, default='0,0')
    province = models.CharField(max_length=100, choices=Province.PROVINCE_CHOICES, default=Province.SAN_JOSE)
    name = models.CharField(max_length=250, unique=True)
    description_markdown = models.TextField()
    description_HTML = models.TextField()
    address = models.CharField(max_length=500)

class ClimbingGym(models.Model, Province):
    climbing_gym_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    province = models.CharField(max_length=100, choices=Province.PROVINCE_CHOICES, default=Province.SAN_JOSE)
    address = models.CharField(max_length=500)
    coordinates = models.CharField(max_length=250, unique=True, default='0,0')

class LocationArea(models.Model):
    location_area_id = models.AutoField(primary_key=True)
    climbing_location = models.ForeignKey(ClimbingLocation, related_name='areas', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description_markdown = models.TextField()
    description_HTML = models.TextField()

class SportRoute(models.Model, YDSGrade, FontGrade):
    sport_route_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    location_area = models.ForeignKey(LocationArea, related_name='sport_routes', on_delete=models.CASCADE)
    yds_grade = models.CharField(max_length=10, choices=YDSGrade.YDS_GRADE_OPTIONS)
    font_grade = models.CharField(max_length=10, choices=FontGrade.FONT_GRADE_OPTIONS)
    is_project = models.BooleanField()
    distance = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    quick_draw_qty = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)]) 

class SportRouteImage(models.Model):
    sport_route_image_id = models.AutoField(primary_key=True)
    route = models.ForeignKey(SportRoute, related_name='route_images', on_delete=models.CASCADE)
    imageUrl = models.URLField()

class Boulder(models.Model):
    boulder_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location_area = models.ForeignKey(LocationArea, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)

class BoulderImage(models.Model): 
    route_image_id = models.AutoField(primary_key=True)
    boulder = models.ForeignKey(Boulder, related_name='boulder_images', on_delete=models.CASCADE)
    image_url = models.URLField()

class BoulderRoute(models.Model, VGrade):
    boulder_route_id = models.AutoField(primary_key=True)
    v_grade = models.CharField(max_length=10, choices=VGrade.V_GRADE_OPTIONS)
    is_project = models.BooleanField() 
    is_high_ball = models.BooleanField()
    is_sit_start = models.BooleanField()
    boulder = models.ForeignKey(Boulder, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)



