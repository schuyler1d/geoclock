from settings_shared import *

TEMPLATE_DIRS = (
    "/var/www/geoclock/geoclock/templates",
)

MEDIA_ROOT = '/var/www/geoclock/uploads/'
# put any static media here to override app served static media
STATICMEDIA_MOUNTS = (
    ('/sitemedia', '/var/www/geoclock/geoclock/sitemedia'),	
)


DEBUG = False
TEMPLATE_DEBUG = DEBUG

try:
    from local_settings import *
except ImportError:
    pass
