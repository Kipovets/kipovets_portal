from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Author
from .filters import PostFilter
from .forms import PostForm


class PostView(ListView):
    model = Post
    ordering = '-time_create'
    template_name = 'news/postlist.html'
    context_object_name = 'postlist'
    paginate_by = 10


class PostDetail(DetailView):
    model = Post
    template_name = 'news/post.html'
    context_object_name = 'post'


class PostSearch(ListView):
    model = Post
    form = PostFilter
    template_name = 'news/search.html'
    context_object_name = 'search'

    def get_queryset(self):
        queryset = super(PostSearch, self).get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.queryset

    def get_context_data(self, **kwargs):
        context = super(PostSearch, self).get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news/create.html'
    permission_required = 'news.add_post'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = Author.objects.get(user_id=1)   #Author.objects.get(user_id=self.request.user.id)
        path = self.request.path
        if path == '/news/create/':
            post.type_post = 'NW'
            return super().form_valid(form)
        elif path == '/articles/create/':
            post.type_post ='AR'
            return super().form_valid(form)


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news/create.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'news/delete.html'
    success_url = reverse_lazy('postlist')



