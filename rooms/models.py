from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class AbstractItem(core_models.TimeStampedModel):
    """Abstract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Amenity(AbstractItem):
    """Amenity Model Definition"""

    class Meta:
        verbose_name_plural = "Amernities"

    pass


class RoomType(AbstractItem):
    """Room Model Definition"""

    class Meta:
        verbose_name = "Room Type"
        ordering = ["created"]

    pass


class Facility(AbstractItem):
    """Facility Model Definition"""

    class Meta:
        verbose_name_plural = "Facilities"

    pass


class HouseRule(AbstractItem):
    """HouseRule Model Definition"""

    class Meta:
        verbose_name = "House Rule"

    pass


# Create your models here.
class Room(core_models.TimeStampedModel):
    """Rooms Model Definition"""

    name = models.CharField(max_length=140, default="")
    description = models.TextField(default="")
    country = CountryField(default="")
    city = models.CharField(max_length=80, default="")
    price = models.IntegerField(default=0)
    address = models.CharField(max_length=140, default="")
    guests = models.IntegerField(default=0)
    beds = models.IntegerField(default=0)
    bedrooms = models.IntegerField(default=0)
    baths = models.IntegerField(default=0)
    check_in = models.TimeField(null=True)
    check_out = models.TimeField(null=True)
    instant_book = models.BooleanField(default=False)
    """Foreign key uses connection-- connected rooms with the user"""
    host = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True)
    """on_delete = setnull -> room doesn't get deleted if we delete roomtype"""
    room_types = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)
    facilities = models.ManyToManyField("Facility", blank=True)
    house_rules = models.ManyToManyField("HouseRule", blank=True)
    amenities = models.ManyToManyField("Amenity", blank=True)

    def __str__(self):
        return self.name


class Photo(core_models.TimeStampedModel):
    """Photo model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
