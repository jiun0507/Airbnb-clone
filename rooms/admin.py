from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Facility, models.HouseRule, models.Amenity)
class ItemAdmin(admin.ModelAdmin):
    """ItemAdmin Definition"""

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """"""

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """RoomAdmin Definition"""

    pass
