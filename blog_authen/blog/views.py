from django.shortcuts import render
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy
from .models import PostForm  # Import your custom PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator # new

# Create your views here.
class BlogListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'home.html'
    #queryset = Post.objects.filter(title__contains="1")  
    #context_object_name = 'all_posts_list' # new

class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'
    paginate_by = 1 # Set the number of comments per page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = self.object.post_comments.filter(is_approved=True)
        paginator = Paginator(comments, self.paginate_by)

        page = self.request.GET.get('page')
        comments = paginator.get_page(page)

        context['comments'] = comments
        return context

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    form_class = PostForm  # Use your custom PostForm
    #fields = ['title','author','body']

    def form_valid(self, form):
        # Set the author to the current user
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body']

    def test_func(self):
        obj= self.get_object()
        return obj.author == self.request.user

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy('home')

    def test_func(self):
        obj= self.get_object()
        return obj.author == self.request.user

from django.shortcuts import render, redirect
from .models import PostForm  # Importing the PostForm from models.py

# View function to create a new post
def blogCreateView(request):
    # Check if the request is a POST request (i.e., the form has been submitted)
    if request.method == 'POST':
        form = PostForm(request.POST)  # Create a form instance with the submitted data
        if form.is_valid():  # Check if the form data passes all validation rules
            form.save()  # Save the valid form data to create a new Post instance in the database
            return redirect('home')  # Redirect to the 'home' view after successful post creation
    else:
        form = PostForm()  # If the request is GET, create an empty form instance
    
    # Render the template with the form (either blank or filled with POST data)
    return render(request, 'post_new.html', {'form': form})
