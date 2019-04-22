from django.shortcuts import render

from blog.models import BlogPost

from .models import SearchQuery

def search_view(request):
    query = request.GET.get('q', None)
    user = None
    if request.user.is_authenticated:
        user = request.user
    context =  {"query": query}
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        post_list = Post.objects.search(query=query)
        context['post_list'] = post_list
    return render(request, 'searches/view.html',context)