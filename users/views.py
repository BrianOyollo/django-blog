from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import Profile


# Create your views here.

class UserProfileView(TemplateView):
    model = Profile
    template_name = 'users/profile.html'
    fields = '__all__'
    context_object_name='all_profiles'
