from django.db import models

# Create your models here.
class Rover(models.Model):
    foursq_id = models.CharField(max_length=24)
    #probably too long
    oauth_token = models.CharField(blank=True,null=True,max_length=96)
    gender = models.SmallIntegerField(blank=True,null=True,default=None)

class Stereotype(models.Model):
    title = models.CharField(max_length=64)
    category = models.CharField(max_length=96)
    time = models.TimeField()
    timedelta = models.SmallIntegerField()
    color = models.SmallIntegerField(blank=True,null=True)
    weekend = models.BooleanField()

class Venue(models.Model):
    venue_id = models.CharField(max_length=24)
    #if venue is a source for a stereotype
    #  not necessarily exclusive
    sourced = models.ForeignKey(Stereotype)
    #e.g. 40.740088,-73.992577
    lat = models.FloatField()
    lon = models.FloatField()

class VenuePing(models.Model):
    venue_id = models.CharField(max_length=24)
    count = models.SmallIntegerField(blank=True,null=True,default=None)
    gender_ratio = models.FloatField(blank=True,null=True,default=None)


class TargetVenueCategory(models.Model):
    "all fields are optional "
    query = models.CharField(blank=True,null=True,max_length=96)
    category = models.CharField(blank=True,null=True,max_length=96)
    ll = models.CharField(blank=True,null=True,max_length=96)
    time = models.TimeField(blank=True,null=True)
    timedelta = models.SmallIntegerField(blank=True,null=True)

class Labeling(models.Model):
    rover = models.ForeignKey(Rover)
    stereotype = models.ForeignKey(Stereotype)

class Checkin(models.Model):
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    venue = models.ForeignKey(Venue)
    gender =  models.SmallIntegerField(blank=True,null=True,default=None)
    rover = models.ForeignKey(Rover)
    lat = models.FloatField()
    lon = models.FloatField()

class Rediscovered(models.Model):
    rover = models.ForeignKey(Rover)
    stereotype = models.ForeignKey(Stereotype)
    lat = models.FloatField()
    lon = models.FloatField()
    venue = models.ForeignKey(Venue)
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
          
     
