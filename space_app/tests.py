from django.test import TestCase
import pytest
from django.urls import reverse, reverse_lazy
from space_app.models import Rocket, Satellite, Flight, PlaceOnOrbit, Producer, LaunchSite


@pytest.mark.django_db
def test_status(client):
    response = client.get('/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_main(client):
    response = client.get(reverse('main_page'))
    assert response.status_code == 200

# LISTS DB

@pytest.mark.django_db
def test_rockets_list(client, rockets):
    response = client.get(reverse('rockets_list'))
    context = response.context
    assert len(context) == 2


@pytest.mark.django_db
def test_satellites_list(client):
    response = client.get(reverse('satellites_list'))
    context = response.context
    assert len(context) >= 2


@pytest.mark.django_db
def test_launchsites_list(client):
    response = client.get(reverse('launchsites_list'))
    context = response.context
    assert len(context) == 2


@pytest.mark.django_db
def test_producer_list(client):
    response = client.get(reverse('producers_list'))
    context = response.context
    assert len(context) == 2


@pytest.mark.django_db
def test_places_on_orbits_list(client):
    response = client.get(reverse('places_on_orbit_list'))
    context = response.context
    assert len(context) >= 2


@pytest.mark.django_db
def test_flights_list(client):
    response = client.get(reverse('flights_list'))
    context = response.context
    assert len(context) >= 2


# LISTS URLS

@pytest.mark.django_db
def test_rockets_list_url(client):
    response = client.get(reverse('rockets_list'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_satellites_list_url(client):
    response = client.get(reverse('satellites_list'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_launchsites_list_url(client):
    response = client.get(reverse('launchsites_list'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_producer_list_url(client):
    response = client.get(reverse('producers_list'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_places_on_orbit_list_url(client):
    response = client.get(reverse('places_on_orbit_list'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_flights_list_url(client):
    response = client.get(reverse('flights_list'))
    assert response.status_code == 200


# DETAILS

@pytest.mark.django_db
def test_rocket_details(client, rocket_for_tests):
    response = client.get(f'/rocket/{rocket_for_tests.id}/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_satellite_details(client, satellite_for_tests):
    response = client.get(f'/satellite/{satellite_for_tests.id}/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_producer_details(client, producer):
    response = client.get(f'/producer/{producer.id}/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_place_on_orbit_details(client, place_on_orbit_for_tests):
    response = client.get(f'/place_on_orbit/{place_on_orbit_for_tests.id}/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_flight_details(client, flight):
    response = client.get(f'/flight/{flight.id}/')
    assert response.status_code == 200



# ROCKET

@pytest.mark.django_db
def test_add_rocket_user(client, user):
    client.force_login(user=user)
    rocket = {
        'name': 'Falcon9',
        'launch_price': 2342342
    }
    client.post(reverse('rocket_add'), rocket)
    assert Rocket.objects.get(name='Falcon9', launch_price=2342342)


@pytest.mark.django_db
def test_add_rocket_superuser(client, super_user):
    client.force_login(user=super_user)
    rocket = {
        'name': 'Long March',
        'launch_price': 56756775
    }
    client.post(reverse('rocket_add'), rocket)
    assert Rocket.objects.get(name='Long March', launch_price=56756775)


@pytest.mark.django_db
def test_add_rocket_unlogged_user(client):
    response = client.get(reverse('rocket_add'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_update_rocket_superuser(client, rocket_for_tests, super_user):
    client.force_login(user=super_user)
    response = client.get(f'/updaterocket/{rocket_for_tests.id}/')
    assert response.status_code == 200
    rocket = {
        'name': 'Falcon9 - EDITED',
        'launch_price': 3435345
    }
    client.post(f'/updaterocket/{rocket_for_tests.id}/', rocket)
    assert Rocket.objects.get(name='Falcon9 - EDITED', launch_price=3435345)


@pytest.mark.django_db
def test_delete_rocket(client, rocket_for_tests, super_user):
    client.force_login(user=super_user)
    response = client.get(f'/delete_rocket/{rocket_for_tests.id}/')
    assert response.status_code == 200
    client.post(f'/delete_rocket/{rocket_for_tests.id}/', {'del': 'Abort'})
    assert Rocket.objects.count() == 1
    client.post(f'/delete_rocket/{rocket_for_tests.id}/', {'del': 'DELETE'})
    assert Rocket.objects.count() == 0


@pytest.mark.django_db
def test_delete_rocket_unlogged_user(client, rocket_for_tests):
    response = client.get(f'/delete_rocket/{rocket_for_tests.id}/')
    assert response.status_code == 302



# SATELLITE

@pytest.mark.django_db
def test_add_satellite_user(client, user):
    client.force_login(user=user)
    satellite = {
        'name': 'SAT TEST',
        'weight': 4234234,
        'description': 'WEATHER SATELLITE'
    }
    client.post(reverse('satellite_add'), satellite)
    assert Satellite.objects.get(name='SAT TEST', weight=4234234, description='WEATHER SATELLITE')


@pytest.mark.django_db
def test_add_satellite_unlogged_user(client):
    response = client.get(reverse('satellite_add'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_update_satellite_superuser(client, satellite_for_tests, super_user):
    client.force_login(user=super_user)
    response = client.get(f'/updatesatellite/{satellite_for_tests.id}/')
    assert response.status_code == 200
    satellite = {
        'name': 'SAT TEST- EDITED',
        'weight': 5534234,
        'description': 'WEATHER AND SPY SATELLITE'
    }
    client.post(f'/updatesatellite/{satellite_for_tests.id}/', satellite)
    assert Satellite.objects.get(name='SAT TEST- EDITED', weight=5534234, description='WEATHER AND SPY SATELLITE')


@pytest.mark.django_db
def test_delete_satellite(client, satellite_for_tests, super_user):
    client.force_login(user=super_user)
    response = client.get(f'/delete_satellite/{satellite_for_tests.id}/')
    assert response.status_code == 200
    client.post(f'/delete_satellite/{satellite_for_tests.id}/', {'del': 'Abort'})
    assert Satellite.objects.count() == 1
    client.post(f'/delete_satellite/{satellite_for_tests.id}/', {'del': 'DELETE'})
    assert Satellite.objects.count() == 0


@pytest.mark.django_db
def test_delete_rocket_unlogged_user(client, satellite_for_tests):
    response = client.get(f'/delete_satellite/{satellite_for_tests.id}/')
    assert response.status_code == 302



# FLIGHTS

@pytest.mark.django_db
def test_add_flight_user(client, user, rocket_for_tests, place_on_orbit_for_tests, satellite_for_tests):
    client.force_login(user=user)
    flight = {
        'rocket': rocket_for_tests.id,
        'destination': place_on_orbit_for_tests.id,
        'satellite': satellite_for_tests.id,
        'launchsite': 'Łeba-Rąbka / POLAND'
    }
    client.post(reverse('flight_add'), flight)
    assert Flight.objects.count() == 1
    assert Flight.objects.get(launchsite='Łeba-Rąbka / POLAND')


@pytest.mark.django_db
def test_add_flight_unlogged_user(client):
    response = client.get(reverse('flight_add'))
    assert response.status_code == 302


@pytest.mark.django_db
def test_update_flight_superuser(client, super_user, flight, rocket_for_tests, place_on_orbit_for_tests, satellite_for_tests):
    client.force_login(user=super_user)
    response = client.get(f'/updateflight/{flight.id}/')
    assert response.status_code == 200
    context = {
        'rocket': rocket_for_tests.id,
        'destination': place_on_orbit_for_tests.id,
        'satellite': satellite_for_tests.id,
        'launchsite': "Wenchang Satellite Launch Center / CHINA"
    }
    client.post(f'/updateflight/{flight.id}/', context)
    assert Flight.objects.get(launchsite="Wenchang Satellite Launch Center / CHINA")


@pytest.mark.django_db
def test_delete_flight(client, flight, super_user):
    client.force_login(user=super_user)
    response = client.get(f'/delete_flight/{flight.id}/')
    assert response.status_code == 200
    client.post(f'/delete_flight/{flight.id}/', {'del': 'Abort'})
    assert Flight.objects.count() == 1
    client.post(f'/delete_flight/{flight.id}/', {'del': 'DELETE'})
    assert Flight.objects.count() == 0


@pytest.mark.django_db
def test_delete_rocket_unlogged_user(client, flight):
    response = client.get(f'/delete_flight/{flight.id}/')
    assert response.status_code == 302


# PLACES ON ORBITS

@pytest.mark.django_db
def test_add_place_on_orbit_user(client, user):
    client.force_login(user=user)
    orbit = {
        'orbit': "MOON"
    }
    client.post(reverse('add_place_on_orbit'), orbit)
    assert PlaceOnOrbit.objects.count() == 1
    assert PlaceOnOrbit.objects.get(orbit='MOON')


# PRODUCERS

@pytest.mark.django_db
def test_add_producer_user(client, user):
    client.force_login(user=user)
    producer = {
        'name': "Uralskie zakłady rakietowe",
        'country': "RUSSIA"
    }
    client.post(reverse('add_producer'), producer)
    assert Producer.objects.count() == 1
    assert Producer.objects.get(country='RUSSIA')


@pytest.mark.django_db
def test_add_producer_unlogged_user(client):
    response = client.get(reverse('add_producer'))
    assert response.status_code == 302



# LAUNCH SITES

@pytest.mark.django_db
def test_add_launchsite_user(client, user, rocket_for_tests):
    client.force_login(user=user)
    launchsite = {
        'site': "Kennedy Space Center / USA",
        'rockets': rocket_for_tests.id
    }
    client.post(reverse('add_launchsite'), launchsite)
    assert LaunchSite.objects.count() == 1
    assert LaunchSite.objects.get(site='Kennedy Space Center / USA')


@pytest.mark.django_db
def test_add_launchsite_unlogged_user(client):
    response = client.get(reverse('add_launchsite'))
    assert response.status_code == 302
