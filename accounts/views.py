from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib.auth.models import Permission

from accounts.forms import PermissionForm


class MyLoginView(LoginView):
    extra_context = {'button_name': 'STWÓRZ KONTO'}


class CreateUser(View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, 'listFormView.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Utworzono nowego konto. Masz teraz dostep do pełnych zasobów serwisu.")
        return render(request, 'listFormView.html', {'form': form})


class SingUpView(CreateView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'registration/login.html'

    def form_valid(self, form):
        response = super(SingUpView, self).form_valid(form)
        user = self.object
        user.user_permissions.add(Permission.objects.get(codename='add_launchsite'))
        user.user_permissions.add(Permission.objects.get(codename='add_producer'))
        login(self.request, self.object)
        return response


class ChangePermissionView(UpdateView):
    form_class = PermissionForm
    success_url = '/'
    model = User
    template_name = 'listFormView.html'


class UserListView(ListView):
    model = User
    template_name = 'listUserView.html'

    def get_queryset(self):
        return User.objects.filter(is_superuser=False)
