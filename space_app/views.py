from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from django.views.generic import UpdateView, DeleteView

from space_app.forms import RocketForm, SatelliteForm, ProducerForm, PlaceOnOrbitForm, FlightForm, LaunchSiteForm
from space_app.models import Flight, Satellite, Rocket, Producer, PlaceOnOrbit, LaunchSite


# Create your views here.


def main_page(request):
    context = {
        'flights_amount': Flight.flight_amount(),
        'rocket_amount': Rocket.rocket_amount(),
        'satellite_amount': Satellite.satellite_amount()
    }
    return render(request, "main.html", context)


class Satellites(View):
    def get(self, request):
        satellites_lst = Satellite.objects.all().order_by('name')
        return render(request, 'satellites.html', {'satellites': satellites_lst})


class Rockets(View):
    def get(self, request):
        rockets_lst = Rocket.objects.all().order_by('name')
        return render(request, 'rockets.html', {'rockets': rockets_lst})


class Producers(View):
    def get(self, request):
        producers_list = Producer.objects.all()
        return render(request, 'producers.html', {'producers': producers_list})


class PlacesOnOrbits(View):
    def get(self, request):
        places_on_orbits_list = PlaceOnOrbit.objects.all()
        return render(request, 'places_on_orbits.html', {'places_on_orbits': places_on_orbits_list})


class Flights(View):
    def get(self, request):
        flights_list = Flight.objects.all()
        return render(request, 'flights.html', {'flights': flights_list})


class LaunchSites(View):
    def get(self, request):
        launchsites_list = LaunchSite.objects.all()
        return render(request, 'launchsites.html', {'launchsites': launchsites_list})


# DETAILS VIEWS

class SatelliteDetails(View):
    def get(self, request, satellite_id):
        satellite = Satellite.objects.get(id=satellite_id)
        context = {
            'satellite': satellite,
        }
        return render(request, 'satellite_details.html', context)


class RocketDetails(View):
    def get(self, request, rocket_id):
        rocket = Rocket.objects.get(id=rocket_id)
        context = {
            'rocket': rocket,
        }
        return render(request, 'rocket_details.html', context)


class ProducerDetails(View):
    def get(self, request, producer_id):
        producer = Producer.objects.get(id=producer_id)
        context = {
            'producer': producer,
        }
        return render(request, 'producer_details.html', context)


class PlaceOnOrbitDetails(View):
    def get(self, request, place_on_orbit_id):
        place_on_orbit = PlaceOnOrbit.objects.get(id=place_on_orbit_id)
        context = {
            'place_on_orbit': place_on_orbit,
        }
        return render(request, 'place_on_orbit_details.html', context)


class FlightDetails(View):
    def get(self, request, flight_id):
        flight = Flight.objects.get(id=flight_id)
        context = {
            'flight': flight,
        }
        return render(request, 'flight_details.html', context)


class LaunchSiteDetails(View):
    def get(self, request, launchsite_id):
        launchsite = LaunchSite.objects.get(id=launchsite_id)
        context = {
            'launchsite': launchsite,
        }
        return render(request, 'launchsite_details.html', context)


# ADD VIEWS

class AddRocket(LoginRequiredMixin, View):
    def get(self, request):
        form = RocketForm()
        return render(request, 'rocket_add.html', {'form': form})

    def post(self, request):
        form = RocketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rockets_list')
        else:
            return render(request, 'rocket_add.html', {'form': form})


class AddProducer(LoginRequiredMixin, View):
    def get(self, request):
        form = ProducerForm()
        return render(request, 'producer_add.html', {'form': form})

    def post(self, request):
        form = ProducerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producers_list')
        else:
            return render(request, 'producer_add.html', {'form': form})


class AddSatellite(LoginRequiredMixin, View):
    def get(self, request):
        form = SatelliteForm()
        return render(request, 'satellite_add.html', {'form': form})

    def post(self, request):
        form = SatelliteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('satellites_list')
        else:
            return render(request, 'satellite_add.html', {'form': form})


class AddPlaceOnOrbit(LoginRequiredMixin, View):
    def get(self, request):
        form = PlaceOnOrbitForm()
        return render(request, 'place_on_orbit_add.html', {'form': form})

    def post(self, request):
        form = PlaceOnOrbitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('places_on_orbit_list')
        else:
            return render(request, 'place_on_orbit_add.html', {'form': form})


class AddFlight(LoginRequiredMixin, View):
    def get(self, request):
        form = FlightForm()
        return render(request, 'flight_add.html', {'form': form})

    def post(self, request):
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flights_list')
        else:
            return render(request, 'flight_add.html', {'form': form})


class AddLaunchsite(LoginRequiredMixin, View):
    def get(self, request):
        form = LaunchSiteForm()
        return render(request, 'launchsite_add.html', {'form': form})

    def post(self, request):
        form = LaunchSiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('launchsites_list')
        else:
            return render(request, 'launchsite_add.html', {'form': form})


# UPDATE & DELETE

class UpdateRocketView(PermissionRequiredMixin, UpdateView):
    permission_required = ['space_app.update_rocket']
    model = Rocket
    form_class = RocketForm
    template_name = 'listFormView.html'
    success_url = '/rockets/'


class DeleteRocketView(PermissionRequiredMixin, DeleteView):
    permission_required = ['space_app.delete_rocket']
    model = Rocket
    template_name = "del_view.html"
    success_url = '/rockets/'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex.update({'button_name': 'DELETE'})
        return contex

    def post(self, request, *args, **kwargs):
        if request.POST['del'] == 'Abort':
            self.object = self.get_object()
            success_url = self.get_success_url()
            return redirect(success_url)
        return self.delete(request, *args, **kwargs)


class UpdateSatelliteView(PermissionRequiredMixin, UpdateView):
    permission_required = ['space_app.update_satellite']
    model = Satellite
    form_class = SatelliteForm
    template_name = 'listFormView.html'
    success_url = '/satellites/'


class DeleteSatelliteView(PermissionRequiredMixin, DeleteView):
    permission_required = ['space_app.delete_satellite']
    model = Satellite
    template_name = "del_view.html"
    success_url = '/satellites/'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex.update({'button_name': 'DELETE'})
        return contex

    def post(self, request, *args, **kwargs):
        if request.POST['del'] == 'Abort':
            self.object = self.get_object()
            success_url = self.get_success_url()
            return redirect(success_url)
        return self.delete(request, *args, **kwargs)


class UpdateFlightView(PermissionRequiredMixin, UpdateView):
    permission_required = ['space_app.update_flight']
    model = Flight
    form_class = FlightForm
    template_name = 'listFormView.html'
    success_url = '/flights/'


class DeleteFlightView(PermissionRequiredMixin, DeleteView):
    permission_required = ['space_app.delete_flight']
    model = Flight
    template_name = "del_view.html"
    success_url = '/flights/'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex.update({'button_name': 'DELETE'})
        return contex

    def post(self, request, *args, **kwargs):
        if request.POST['del'] == 'Abort':
            self.object = self.get_object()
            success_url = self.get_success_url()
            return redirect(success_url)
        return self.delete(request, *args, **kwargs)
