from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, UpdateView
from user.forms import UserForm
from user.models import User, City


class UserRegistration(CreateView):
    template_name = 'registration.html'
    model = User
    form_class = UserForm
    success_url = "login/"

    def get_queryset(self):
        state_id = self.request.GET.get('state')
        cities = City.objects.filter(state_id=state_id).order_by('name')
        import pdb;
        pdb.set_trace()
        return redirect(self.request, 'registration.html', {'cities': cities})

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user.save()
        return HttpResponseRedirect(self.success_url)


class UserUpdateView(UpdateView):
    model = User
    fields = ['email', 'address', 'phone_no']
    template_name = 'user/main.html'

    def get_success_url(self):
        return reverse('book_list')
        # return reverse('detailmanager', kwargs={"pk": self.request.user.category_id.id})


class UserLogin(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = 'book_list'

    # def get_success_url(self):
    #     return redirect('book_list')

    def get_success_url(self):
        return reverse('book_list')


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("login")
