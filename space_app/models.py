import os
import uuid
from django.conf import settings
from django.db import models

ORBITS = (
    ("LEO", "LEO"),
    ("MEO", "MEO"),
    ("GEO", "GEO"),
    ("MEO", "MEO"),
    ("MOON", "MOON"),
)

LAUNCH_SITES = (
    ("Kennedy Space Center / USA", "Kennedy Space Center / USA"),
    ("Boca Chica / USA", "Boca Chica / USA"),
    ("Baikonur Cosmodrome / RUSSIA", "Baikonur CosmodromE / RUSSIA"),
    ("Vostochny Cosmodrome / RUSSIA", "Vostochny Cosmodrome / RUSSIA"),
    ("Wenchang Satellite Launch Center / CHINA", "Wenchang Satellite Launch Center / CHINA"),
    ("Łeba-Rąbka / POLAND", "Łeba-Rąbka / POLAND")
)


class Rocket(models.Model):
    name = models.CharField(max_length=25)
    producer = models.ForeignKey('Producer', on_delete=models.CASCADE, null=True, blank=True)
    launch_price = models.IntegerField(default=78)

    @staticmethod
    def rocket_amount():
        return Rocket.objects.all().count()

    def __str__(self):
        return f'{self.id} - {self.name} / {self.producer} / {self.launch_price}'

    def get_detail_url(self):
        return f'/rocket/{self.id}'

    def get_edit_url(self):
        return f'/updaterocket/{self.id}'

    def del_url(self):
        return f"/delete_rocket/{self.id}/"


class Producer(models.Model):
    name = models.CharField(max_length=128, unique=True)
    country = models.CharField(max_length=10, default="USA")

    def __str__(self):
        return f"{self.name} / {self.country}"

    def get_detail_url(self):
        return f'/producer_detail/{self.id}'


class Satellite(models.Model):
    name = models.CharField(max_length=64)
    weight = models.IntegerField(default=23000)
    description = models.CharField(max_length=300)
    destination_orbit = models.ForeignKey('PlaceOnOrbit', null=True, blank=True, on_delete=models.CASCADE, related_name="satellie_orbit")

    @staticmethod
    def satellite_amount():
        return Satellite.objects.all().count()

    def __str__(self):
        return f'{self.name}'

    def get_detail_url(self):
        return f'/satellite/{self.id}'

    def get_edit_url(self):
        return f'/updatesatellite/{self.id}'

    def del_url(self):
        return f"/delete_satellite/{self.id}/"


class PlaceOnOrbit(models.Model):
    orbit = models.CharField(max_length=10, null=True, choices=ORBITS)
    purpose = models.CharField(max_length=360, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.orbit} / {self.purpose}'

    @staticmethod
    def orbits_amount():
        return PlaceOnOrbit.objects.all().count()

    def get_detail_url(self):
        return f'/place_on_orbit/{self.id}'



class Flight(models.Model):
    flight_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, blank=True)
    departure_date = models.DateField(blank=True, null=True)
    rocket = models.OneToOneField('Rocket', on_delete=models.CASCADE)
    destination = models.ForeignKey('PlaceOnOrbit', on_delete=models.CASCADE)
    satellite = models.ForeignKey('Satellite', on_delete=models.CASCADE)
    launchsite = models.CharField(max_length=40, choices=LAUNCH_SITES)

    @staticmethod
    def flight_amount():
        return Flight.objects.all().count()

    def __str__(self):
        return f'{self.flight_id} : {self.satellite}'

    def get_detail_url(self):
        return f'/flight/{self.id}'

    def get_edit_url(self):
        return f'/updateflight/{self.id}'

    def del_url(self):
        return f"/delete_flight/{self.id}/"


class LaunchSite(models.Model):
    site = models.CharField(max_length=40, choices=LAUNCH_SITES)
    rockets = models.ManyToManyField('Rocket', through='LaunchSiteRockets')

    def __str__(self):
        return f'{self.site} / {self.rockets}'


class LaunchSiteRockets(models.Model):
    site = models.ForeignKey('LaunchSite', on_delete=models.CASCADE)
    rocket = models.ForeignKey('Rocket', on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return self.site





