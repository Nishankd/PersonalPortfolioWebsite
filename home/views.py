# views.py
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Project
from .forms import *


class HomeView(View):
    template_name = 'index.html'

    def get(self, request):
        projects = Project.objects.all()
        form = ContactForm()
        return render(request, self.template_name, {'projects': projects, 'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the home page after successful form submission
            return redirect('homepage')

        projects = Project.objects.all()
        return render(request, self.template_name, {'projects': projects, 'form': form})
