from django.shortcuts import render, redirect
from .models import display
from .forms import display_form
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

class display_list_view(ListView):
    model = display
    context_object_name = 'list'
    template_name = 'new_app/display_list.html'
    ordering = ['-date_posted']
class display_detail_view(DetailView):
    model = display

class display_create_view(LoginRequiredMixin,CreateView):
    model = display
    fields = ['title','video']
    context_object_name = 'form'

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super().form_valid(form)

class display_update_view(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = display
    fields = ['title', 'video']
    context_object_name = 'form'
    def form_valid(self, form):
        form.instance.host = self.request.user
        return super().form_valid(form)

    def test_func(self):
        display = self.get_object()
        if self.request.user == display.host:
            return True
        return False

class display_delete_view(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = display
    success_url = '/'

    def test_func(self):
        display = self.get_object()
        if self.request.user == display.host:
           return True
        return False


