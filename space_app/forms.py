from django import forms
from space_app.models import Satellite, Rocket, Producer, PlaceOnOrbit, Flight, LaunchSite
from django.core.exceptions import ValidationError


class SatelliteForm(forms.ModelForm):
    class Meta:
        model = Satellite
        fields = "__all__"


class RocketForm(forms.ModelForm):
    class Meta:
        model = Rocket
        fields = "__all__"


class ProducerForm(forms.ModelForm):
    class Meta:
        model = Producer
        fields = "__all__"


class PlaceOnOrbitForm(forms.ModelForm):
    class Meta:
        model = PlaceOnOrbit
        fields = "__all__"


class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = "__all__"


class LaunchSiteForm(forms.ModelForm):
    class Meta:
        model = LaunchSite
        fields = "__all__"