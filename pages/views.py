from django.shortcuts import render
from django.http import HttpResponse
from partners.models import Partner
#from team.models import Team
from testaments.models import Testament
from django.contrib.auth.decorators import login_required
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
from .models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from pages.choices import age_choices, colleges_choices, education_level_choices, expirience_choices, country_choices


def index(request):
    partners = Partner.objects.order_by('-membership_date').filter(is_published=True)[:4]
    testaments = Testament.objects.order_by('-post_date').filter(is_published=True)[:3]
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]
    
   
    context = {
        'posts': posts,
        'partners': partners,
        'testaments': testaments,
        'country_choices': country_choices,
        'colleges_choices': colleges_choices,
        'education_level_choices': education_level_choices,
        'expirience_choices': expirience_choices,
        'age_choices': age_choices,
        
        
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')


def workers(request):
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]

    context = {
        'posts': posts,
        'colleges_choices': colleges_choices,
        'country_choices': country_choices,
        'education_level_choices': education_level_choices,
        'expirience_choices': expirience_choices,
        'age_choices': age_choices,
    }
    return render(request, 'pages/workers.html', context)



class PostListView(ListView):
    model = Post
    template_name = 'pages/workers.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    is_published = True
    paginate_by = 2


class UserPostListView(ListView):
    model = Post
    template_name = 'pages/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(name=user).order_by('-date_posted')



class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [
        'profession', 
        'why_you_essay', 
        'resume', 
        'date_posted', 
        'name',
        'age',
        'phone',
        'email',
        'address',
        'home',
        'expirience',
        'education_level',
        'colleges',
        'is_fulltime',
        'is_parttime',
        'is_employee'
        ]


    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = fields = [
        'profession', 
        'why_you_essay', 
        'resume', 
        'date_posted', 
        'name',
        'age',
        'phone',
        'email',
        'address',
        'home',
        'expirience',
        'education_level',
        'college',
        'is_fulltime',
        'is_parttime',
        'is_employee'
        ]

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.name:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = 'workers'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.name:
            return True
        return False

def search(request):
  queryset_list = Post.objects.order_by('-date_posted')

  #keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(resume__icontains=keywords)

  
  # home
  if 'home' in request.GET:
    home = request.GET['home']
    if home:
      queryset_list = queryset_list.filter(home__iexact=home)

  # Country
  if 'country' in request.GET:
    country = request.GET['country']
    if country:
      queryset_list = queryset_list.filter(country__iexact=country)
 
  # expirience
  if 'expirience' in request.GET:
    expirience = request.GET['expirience']
    if expirience:
      queryset_list = queryset_list.filter(expirience__lte=expirience)
  
  # education
  if 'education_level' in request.GET:
    education_level = request.GET['education_level']
    if education_level:
      queryset_list = queryset_list.filter(education_level__lte=education_level)

  # colleges
  if 'colleges' in request.GET:
    colleges = request.GET['colleges']
    if colleges:
      queryset_list = queryset_list.filter(colleges__lte=colleges)

  # age
  if 'age' in request.GET:
    age = request.GET['age']
    if age:
      queryset_list = queryset_list.filter(age__lte=age)

  context = {
        'colleges_choices': colleges_choices,
        'country_choices': country_choices,
        'education_level_choices': education_level_choices,
        'expirience_choices': expirience_choices,
        'age_choices': age_choices,
        'pages': queryset_list,
        'values': request.GET

  }

  return  render(request, 'pages/search.html', context)

