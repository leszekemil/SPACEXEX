"""SPACEXEX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from space_app import views
from space_app.views import Satellites, Rockets, AddSatellite, AddRocket, Producers, AddProducer, \
    PlacesOnOrbits, AddPlaceOnOrbit, Flights, AddFlight, LaunchSites, AddLaunchsite, RocketDetails, SatelliteDetails, \
    ProducerDetails, PlaceOnOrbitDetails, FlightDetails, LaunchSiteDetails, \
    UpdateRocketView, DeleteRocketView, UpdateSatelliteView, DeleteSatelliteView, UpdateFlightView, DeleteFlightView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', views.main_page, name='main_page'),
    path('main/', views.main_page),

    path('satellites/', Satellites.as_view(), name="satellites_list"),
    path('satellite/add/', AddSatellite.as_view(), name='satellite_add'),
    path('satellite/<int:satellite_id>/', SatelliteDetails.as_view(), name='satellite_details'),
    path('updatesatellite/<int:pk>/', UpdateSatelliteView.as_view(), name='satellite_update'),
    path('delete_satellite/<int:pk>/', DeleteSatelliteView.as_view(), name='satellite_delete'),

    path('rockets/', Rockets.as_view(), name="rockets_list"),
    path('rocket/<int:rocket_id>/', RocketDetails.as_view(), name='rocket_details'),
    path('rocket/add/', AddRocket.as_view(), name='rocket_add'),
    path('updaterocket/<int:pk>/', UpdateRocketView.as_view(), name='rocket_update'),
    path('delete_rocket/<int:pk>/', DeleteRocketView.as_view(), name='rocket_delete'),

    path('producers/', Producers.as_view(), name="producers_list"),
    path('producer/<int:producer_id>/', ProducerDetails.as_view(), name='producer_details'),
    path('producer/add/', AddProducer.as_view(), name='add_producer'),

    path('places_on_orbits/', PlacesOnOrbits.as_view(), name='places_on_orbit_list'),
    path('place_on_orbit/<int:place_on_orbit_id>/', PlaceOnOrbitDetails.as_view(), name='place_on_orbit_details'),
    path('place_on_orbit/add/', AddPlaceOnOrbit.as_view(), name='add_place_on_orbit'),

    path('flights/', Flights.as_view(), name="flights_list"),
    path('flight/<int:flight_id>/', FlightDetails.as_view(), name='flight_details'),
    path('flight/add/', AddFlight.as_view(), name='flight_add'),
    path('updateflight/<int:pk>/', UpdateFlightView.as_view(), name='flight_update'),
    path('delete_flight/<int:pk>/', DeleteFlightView.as_view(), name='flight_delete'),

    path('launchsites/', LaunchSites.as_view(), name="launchsites_list"),
    path('launchsite/<int:launchsite_id>/', LaunchSiteDetails.as_view, name='flight_details'),
    path('launchsite/add/', AddLaunchsite.as_view(), name='add_launchsite'),
]
