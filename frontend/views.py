import requests
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect
from django.shortcuts import render

from accounts.models import UserProfile
from .forms import UserCreationForm, ProfileForm
from django.urls import reverse_lazy, reverse
from django.views import generic

def index(request):
    data = requests.get('http://' + str(get_current_site(request)) + '/api/districts/').json()
    context = {'districts': data}
    return render(request, 'index.html', context)


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('frontend:login')
    template_name = 'registration/signup.html'

class ProfileView(generic.CreateView):
    form_class = ProfileForm
    success_url = reverse_lazy('login')
    template_name = 'registration/profile.html'

    def get(self, request):
        profile = UserProfile.objects.filter(user=self.request.user)[0]
        form = self.form_class(instance=profile)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            UserProfile.objects.filter(user=request.user).delete()
            new_profile = form.save(commit=False)
            new_profile.user = request.user
            new_profile.save()
            return HttpResponseRedirect(reverse('frontend:profile'))
        context = {'form': form}
        return render(request, self.template_name, context)


