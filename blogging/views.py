from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class PostListView(ListView):
    queryset = Post.objects.exclude(published_date__isnull=True).order_by('-published_date')
    template_name = 'blogging/list.html'

# def list_view(request):
#     published = Post.objects.exclude(published_date__exact=None)
#     posts = published.order_by('-published_date')
#     # template = loader.get_template('blogging/list.html')
#     # context = {'posts': posts}
#     # body = template.render(context)
#     # return HttpResponse(body, content_type='text/html')
#     context = {'posts': posts}
#     return render(request, 'blogging/list.html', context)

class PostDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'

# def detail_view(request, post_id):
#     published = Post.objects.exclude(published_date__exact=None)
#     try:
#         post = published.get(pk=post_id)
#     except Post.DoesNotExist:
#         raise Http404
#     context = {'post': post}
#     return render(request, 'blogging/detail.html', context)
