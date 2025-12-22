from django.contrib import admin

from . import models

admin.site.register(models.EnginePart)
admin.site.register(models.EnginePartInstance)
