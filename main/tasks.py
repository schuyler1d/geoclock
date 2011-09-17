from models import Venue,Stereotype,VenuePing
import datetime

def find_venues(category):
    'query trending venues in category'
    #store in Venue
    pass

def hour_task_findstereotyped():
    #for all stereotypes that fit this hour,
    # query all venues for its category
    # and create 
    #  1. venueping
    #  2. labeling for each user
    #  3. checkin for each user
    now = datetime.datetime.now()
    is_weekend = (now.weekday() > 4) #5,6=sat,sun
    sters = Stereotype.objects.filter(weekend=is_weekend,
                                      starttime__gte=datetime.time(now.hour),
                                      endtime__lte=datetime.time(now.hour),
                                      ).values('id')
    vens = {}
    for v in VenueStereotype.objects.filter(stereotype__in=sters):
        vens.setdefault(v.venue,[]).append(v.stereotype_id)
    #can optimize with multi query
    for v,st in vens.items():
        venue_data = foursq.venues(v).get('response',{}).get('venue',None)
        herenow = venue_data['hereNow']
        genders = {'male':0,'female':0,'none':0}
        for rover in herenow['groups']['others']['items']:
            genders[rover['user']['gender']] += 1
            Checkin.objects.create(time,
                                   date,
                                   venue=v,
                                   gender=GENDER[rover['user']['gender']],
                                   lat=venue_data['location']['lat'],
                                   lng=venue_data['location']['lng'],
                                   )
                                   

        VenuePing.objects.create(venue=v,count=herenow['count'])
        


def hour_task_findtrendingvenues():
    #for each source category
    #  query all trending venues and create
    #  1. venue if not already existing
    # .create_or_update(VenueStereotype)
    pass
