The first time you check out the project:

create a file called local_settings.py with the following two lines:
  FOURSQUARE_CLIENT_ID='243234ABC2DVB98ER34E3F3GHIJKLKJAKSDFMNO123658945'
  FOURSQUARE_CLIENT_SECRET='XYISKKJSDBC2DVBKFJSDFJSKJFABCDEFGHIJKLMNO123658945'

then run these commands:
 %  ./bootstrap.py
 %  createdb geoclock
 %  ./manage.py syncdb
 %  ./manage.py runserver <IP Address>:<PORT> 

