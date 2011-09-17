import models
from django.contrib import admin

def register_all(model_import, module, exclude=[]):
    for m in dir(model_import):
        mod = getattr(model_import,m)
        if hasattr(mod,'DoesNotExist') \
                and mod.__module__==module \
                and not mod in exclude:
            admin.site.register(mod)

register_all(models,'main.models')
