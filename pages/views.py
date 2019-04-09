from django.shortcuts import render
from django.http import HttpResponse
from partners.models import Partner
#from team.models import Team
from testaments.models import Testament
from django.contrib.auth.decorators import login_required
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from pages.choices import age_choices, college_choices, education_level_choices, expirience_choices, county_choices, profession_choices
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
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator



def index(request):
    partners = Partner.objects.order_by('-membership_date').filter(is_published=True)[:4]
    testaments = Testament.objects.order_by('-post_date').filter(is_published=True)[:3]
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)

    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)
    
   
    context = {
        'posts': paged_posts,
        'partners': partners,
        'testaments': testaments,
        'profession_choices': profession_choices,
        'county_choices': county_choices,
        'college_choices': college_choices,
        'education_level_choices': education_level_choices,
        'expirience_choices': expirience_choices,
        'age_choices': age_choices,
    }
    return render(request, 'pages/index.html', context)





class PostListView(ListView):
    model = Post
    template_name = 'pages/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    is_published = True
    paginate_by = 10


class UserPostListView(ListView):
    model = Post
    template_name = 'pages/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(name=user).order_by('-date_posted')
 


class PostDetailView(DetailView):
    model = Post
    
  


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post

    fields = [
        'profession',
        'name',
        'age',
        'expirience', 
        'email',
        'address',
        'home',
        'county',
        'education_level',
        'college',
        'why_you_essay', 
        'resume', 
        'expirience',
        'date_posted', 
        'is_fulltime',
        'is_parttime',
        'is_employee'
      
        
        ]


    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post

    fields = [
        'profession',
        'name',
        'age',
        'expirience', 
        'email',
        'address',
        'home',
        'county',
        'education_level',
        'college',
        'why_you_essay', 
        'resume', 
        'expirience',
        'date_posted', 
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
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.name:
            return True
        return False
 
# about page
def about(request):
    return render(request, 'pages/about.html')


# workers page
def workers(request):
    posts = Post.objects.order_by('-date_posted').filter(is_published=True)[:3]

    context = {
        'posts': posts,
    }
    return render(request, 'pages/workers.html', context)




#hash search

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

 # profession
  if 'profession' in request.GET:
    profession = request.GET['profession']
    if profession:
      queryset_list = queryset_list.filter(profession__iexact=profession)

  # County
  if 'county' in request.GET:
    county = request.GET['county']
    if county:
      queryset_list = queryset_list.filter(county__iexact=county)
 
  # expirience
  if 'expirience' in request.GET:
    expirience = request.GET['expirience']
    if expirience:
      queryset_list = queryset_list.filter(expirience__lte=expirience)
  
  # education
  if 'education_level' in request.GET:
    education_level = request.GET['education_level']
    if education_level:
      queryset_list = queryset_list.filter(education_level__iexact=education_level)

  # college
  if 'college' in request.GET:
    college = request.GET['college']
    if college:
      queryset_list = queryset_list.filter(college__iexact=college)

  # age
  if 'age' in request.GET:
    age = request.GET['age']
    if age:
      queryset_list = queryset_list.filter(age__lte=age)

  context = {
        'profession_choices': profession_choices,
        'college_choices': college_choices,
        'county_choices': county_choices,
        'education_level_choices': education_level_choices,
        'expirience_choices': expirience_choices,
        'age_choices': age_choices,
        'posts': queryset_list,
        'values': request.GET

  }
  return  render(request, 'pages/search.html', context)

 


   