from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from .models import Post, Comment
from .forms import CommentForm
from django.urls import reverse_lazy
from django.db.models import Q

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)   # log user in after registering
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})

@login_required
def profile_view(request):
    return render(request, "registration/profile.html")

def home_view(request):
    return render(request, "home.html")

# List all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # blog/templates/blog/post_list.html
    context_object_name = 'posts'
    ordering = ['-published_date']
    paginate_by = 5

# Detail of a single post
class PostDetailView(DetailView):
     """
    Display a single blog post along with all its related comments.
    Authenticated users can add a new comment directly from this view.
    """
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add comment form to the context
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comments.all()  # all comments for this post
        return context


# Create a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update a post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Delete a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/posts/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class CommentCreateView(LoginRequiredMixin, CreateView):
    """
    Class-based view to allow an authenticated user to create a comment
    for a specific blog post.
    
    Attributes:
    - model: Comment model to create
    - form_class: CommentForm (validates content)
    - template_name: HTML template for creating a comment
    """
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        """
        Automatically associate the comment with:
        - the logged-in user as the author
        - the related post based on post_id in the URL
        """
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=self.kwargs.get('pk'))
        form.instance.author = self.request.user
        form.instance.post = post
        return super().form_valid(form)

    def get_success_url(self):
        """
        After successfully creating a comment, redirect to the
        post detail page so the user can see their comment.
        """
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Allow the comment author to edit their comment.
    Permissions enforced via UserPassesTestMixin.
    """
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def test_func(self):
        # Only allow the author to update the comment
        comment = self.get_object()
        return self.request.user == comment.author

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Allow the comment author to delete their comment.
    Permissions enforced via UserPassesTestMixin.
    """
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        # Only allow the author to delete the comment
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        # Redirect to the post detail page after deletion
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})
    
class PostSearchView(ListView):
    """
    View to handle searching blog posts by title, content, or tags.
    """
    model = Post
    template_name = 'blog/post_search.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """
        Filter posts based on the search query from GET parameter 'q'.
        """
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__name__icontains=query)
            ).distinct()
        return Post.objects.none()  # Return empty queryset if no search term

class TagPostListView(ListView):
    """
    Display all posts that have a specific tag.
    """
    model = Post
    template_name = 'blog/post_list_by_tag.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """
        Filter posts based on the tag name from the URL.
        """
        tag_name = self.kwargs.get('tag_name')
        return Post.objects.filter(tags__name__iexact=tag_name)