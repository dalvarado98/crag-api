import graphene
from graphene_django.types import DjangoObjectType
from . import models

class ClimbingLocationType(DjangoObjectType):
    class Meta:
        model = models.ClimbingLocation

class ClimbingGymType(DjangoObjectType):
    class Meta:
        model = models.ClimbingGym
        
class LocationAreaType(DjangoObjectType):
    class Meta:
        model = models.LocationArea

class SportRouteType(DjangoObjectType):
    class Meta:
        model = models.SportRoute

class SportRouteImageType(DjangoObjectType):
    class Meta:
        model = models.SportRouteImage

# TODO missing endpoint
class Boulder(DjangoObjectType):
    class Meta: 
        model = models.Boulder

# TODO missing endpoint
class BoulderImage(DjangoObjectType): 
    class Meta:
        model = models.BoulderImage

# TODO missing endpoint
class BoulderRoute(DjangoObjectType):
    class Meta:
        model = models.BoulderRoute

class Query(graphene.AbstractType):
    all_climbing_locations = graphene.List(ClimbingLocationType)
    all_climbing_gyms = graphene.List(ClimbingGymType)
    all_location_areas = graphene.List(LocationAreaType)
    all_sport_routes = graphene.List(SportRouteType)

    def resolve_all_climbing_locations(self, info):
        return models.ClimbingLocation.objects.all() 

    def resolve_all_climbing_gyms(self, info):
        return models.ClimbingGym.objects.all()

    def resolve_all_location_areas(self, info):
        return models.LocationArea.objects.all()
    
    def resolve_all_sport_routes(self, info):
        return models.SportRoute.objects.all()