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

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out")},),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms",)},),
        (
            "More about the Spaces",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        ("Last Details", {"fields": ("host",)},),
    )

    ordering = ("name", "price", "bedrooms")

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "room_types",
        "count_amenities",
    )

    list_filter = (
        "host__superhost",
        "host__gender",
        "city",
        "instant_book",
        "facilities",
        "room_types",
        "amenities",
        "country",
    )
    search_fields = ("^host__username",)
    # Many to Many relations
    filter_horizontal = ("house_rules", "amenities", "facilities")

    def count_amenities(self, obj):
        # print(obj.amenities.all())
        return obj.amenities.count()

    count_amenities.short_description = "hello sexy!"
