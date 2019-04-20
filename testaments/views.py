from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Pot


def home(request):
    context = {
        'pots': Pot.objects.all()
    }
    return render(request, 'testament/home.html', context)


class PotListView(ListView):
    model = Pot
    template_name = 'testament/pot_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'pots'
    ordering = ['-post_date']
    paginate_by = 5


class UserPotListView(ListView):
    model = Pot
    template_name = 'testament/user_pots.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Pot.objects.filter(author=user).order_by('-post_date')


class PotDetailView(DetailView):
    model = Pot


class PotCreateView(LoginRequiredMixin, CreateView):
    model = Pot
    fields = ['title', 'info', 'author', 'photo']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PotUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pot
    fields = ['title', 'info', 'author', 'photo']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        pot = self.get_object()
        if self.request.user == pot.author:
            return True
        return False


class PotDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pot
    success_url = '/'

    def test_func(self):
        pot = self.get_object()
        if self.request.user == pot.author:
            return True
        return False



 
