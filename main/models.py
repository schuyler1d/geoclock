from django.db import models

GENDER = {
    'male':-1,
    'female':1,
    'none':0,
    -1:'male',
    1:'female',
    0:'none',
}

# Create your models here.
class Rover(models.Model):
    foursq_id = models.CharField(primary_key=True,max_length=24)
    #probably too long
    oauth_token = models.CharField(blank=True,null=True,max_length=96)
    gender = models.SmallIntegerField(blank=True,null=True,default=None)

class Stereotype(models.Model):
    title = models.CharField(max_length=64)
    category = models.CharField(max_length=96)
    starttime = models.TimeField()
    endtime = models.TimeField()
    color = models.SmallIntegerField(blank=True,null=True)
    weekend = models.BooleanField()

class VenueStereotype(models.Model):
    venue = models.CharField(max_length=24)
    stereotype = models.ForeignKey(Stereotype)

class VenuePing(models.Model):
    venue = models.CharField(max_length=24)
    count = models.SmallIntegerField(blank=True,null=True,default=None)
    gender_ratio = models.FloatField(blank=True,null=True,default=None)


class TargetVenueCategory(models.Model):
    "all fields are optional "
    query = models.CharField(blank=True,null=True,max_length=96)
    category = models.CharField(blank=True,null=True,max_length=96)
    ll = models.CharField(blank=True,null=True,max_length=96)
    starttime = models.TimeField(blank=True,null=True)
    endtime = models.TimeField(blank=True,null=True)

class Labeling(models.Model):
    rover = models.ForeignKey(Rover)
    stereotype = models.ForeignKey(Stereotype)

class Checkin(models.Model):
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    venue = models.CharField(max_length=24)
    gender =  models.SmallIntegerField(blank=True,null=True,default=None)
    rover = models.ForeignKey(Rover)
    lat = models.FloatField()
    lng = models.FloatField()

class Rediscovered(models.Model):
    rover = models.ForeignKey(Rover)
    stereotype = models.ForeignKey(Stereotype)
    lat = models.FloatField()
    lng = models.FloatField()
    venue = models.CharField(max_length=24)
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
          
     
