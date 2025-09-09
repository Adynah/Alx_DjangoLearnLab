from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import CommentForm
from django.urls import reverse_lazy

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

def add_comment(request, post_id):
    """
    Handle creating a new comment for a specific post.
    Only accessible to authenticated users.
    """
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.id)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form, 'post': post})

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