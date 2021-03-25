from django.contrib import admin
from . import models
from django.utils.html import mark_safe

# Register your models here.


@admin.register(models.RoomType, models.Facility, models.HouseRule, models.Amenity)
class ItemAdmin(admin.ModelAdmin):
    """ItemAdmin Definition"""

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo Admin Definition """

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="100px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "thumbnail"


# inline admin class-> allows this inline admin to be inside another class.
class PhotoInline(admin.TabularInline):
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """RoomAdmin Definition"""

    inlines = (PhotoInline,)
    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "city", "country", "address", "price")},
        ),
        (
            "Times",
            {"fields": ("check_in", "check_out")},
        ),
        (
            "Spaces",
            {
                "fields": (
                    "guests",
                    "beds",
                    "bedrooms",
                )
            },
        ),
        (
            "More about the Spaces",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        (
            "Last Details",
            {"fields": ("host",)},
        ),
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
        "total_rating",
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

    raw_id_fields = ("host",)

    search_fields = ("^host__username",)
    # Many to Many relations
    filter_horizontal = ("house_rules", "amenities", "facilities")

    def count_amenities(self, obj):
        # print(obj.amenities.all())
        return obj.amenities.count()

    "the list display column name"
    count_amenities.short_description = "number of amenities"
