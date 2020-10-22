import pytest
from django.contrib.auth.models import User, Permission
from django.test import Client
from space_app.models import Rocket, Satellite, Producer, PlaceOnOrbit, LaunchSite, LaunchSiteRockets, Flight


@pytest.fixture
def rockets(user):
    rockets = []
    r1 = Rocket.objects.create(
        name='Saturn V',
        launch_price=23745278
    )
    r2 = Rocket.objects.create(
        name='Atlas',
        launch_price=6435345
    )
    rockets.append(r1)
    rockets.append(r2)
    return rockets


@pytest.fixture
def rocket_for_tests(user, super_user):
    rocket_for_tests = Rocket.objects.create(name='Soyuz', launch_price=3453454)
    return rocket_for_tests


@pytest.fixture
def launchsite(user, rocket_for_tests):
    site = LaunchSite.objects.create(site="Boca Chica / USA", rockets=rocket_for_tests)
    return site


@pytest.fixture
def launchsiterockets(user, launchsite, rocket_for_tests):
    site_rocket = LaunchSiteRockets.objects.create(
        site=launchsite,
        rocket=rocket_for_tests,
        comment='comment with very important informations'
    )
    return site_rocket


@pytest.fixture
def satellites(user, places_on_orbits):
    satellites = []
    s1 = Satellite.objects.create(
        name='Satellie 1',
        weight=235786,
        description='GPS satellite',
        destination_orbit="LEO"
    )
    s2 = Satellite.objects.create(
        name='Satellie 2',
        weight=456786,
        description='Weather satellite',
    )
    satellites.append(s1)
    satellites.append(s2)
    return satellites


@pytest.fixture
def satellite_for_tests(user):
    satellite_for_tests = Satellite.objects.create(
        name='Satellie ALFA',
        weight=555786,
        description='GLONAS satellite',
    )
    return satellite_for_tests


@pytest.fixture
def producer(user):
    producer = Producer.objects.create(name='NASA - JPL', country="USA")
    return producer


@pytest.fixture
def places_on_orbits(user):
    place = []
    p1 = PlaceOnOrbit.objects.create(
        orbit="LEO"
    )
    p2 = PlaceOnOrbit.objects.create(
        name="GEO",
    )
    place.append(p1)
    place.append(p2)
    return place


@pytest.fixture
def place_on_orbit_for_tests(user):
    place = PlaceOnOrbit.objects.create(orbit="LEO")
    return place


@pytest.fixture
def flight(user, rocket_for_tests, satellite_for_tests, place_on_orbit_for_tests):
    flight = Flight.objects.create(
        rocket=rocket_for_tests,
        destination=place_on_orbit_for_tests,
        satellite=satellite_for_tests,
        launchsite="Łeba-Rąbka / POLAND"
    )
    return flight


@pytest.fixture
def user():
    user = User.objects.create(
        username="Wladzio444",
        email="wlaczio@kozaczekbuziaczek.pl"
    )
    user.set_password('qwerty09876')
    user.save()
    return user


@pytest.fixture
def super_user():
    super_user = User.objects.create(
        username="TadzioAdmin",
        email="Tadeusz@wajchepszeusz.ru",
        is_superuser=True
    )
    super_user.set_password('kamikaze34')
    super_user.save()
    return super_user