from django.shortcuts import render
from blog.models import Blog, Blogger, Comment
from django.views import generic
from django.contrib.auth.models import User

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_blogs = Blog.objects.all().count()
    num_bloggers = Blogger.objects.all().count()
    num_users = User.objects.all().count()


    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits


    context = {
        'num_blogs': num_blogs,
        'num_bloggers': num_bloggers,
        'num_users' : num_users,
        'num_visits' : num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5

    def get_queryset(self):
        return Blog.objects.order_by('-date_of_post')

class BlogDetailView(generic.DetailView):
    model = Blog

class BloggerListView(generic.ListView):
    model = Blogger
    paginate_by = 10

class BloggerDetailView(generic.DetailView):
    model = Blogger

class CommentListView(generic.ListView):
    model = Comment
    paginate_by = 10
    
class CommentDetailView(generic.DetailView):
    model = Comment

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from blog.forms import NewCommentForm

@login_required
def new_comment_blog(request, pk):
    new_comment = Comment()
    blog = get_object_or_404(Blog, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = NewCommentForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            
            description = form.cleaned_data['description']
            new_comment.description = description
            new_comment.blog = blog
            new_comment.date = datetime.date.today()
            new_comment.user = request.user
            new_comment.save()
            
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('blog-detail', args=[str(blog.id)]))
                                 

    # If this is a GET (or any other method) create the default form.
    else:
        form = NewCommentForm(initial={'description': ''})

    context = {
        'form': form,
        'new_comment': new_comment,
        'blog' : blog
    }

    return render(request, 'blog/comment_form.html', context)

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog.models import Blog

class BlogCreate(CreateView):
    model = Blog
    fields = ['title', 'blogger','description']

class BlogUpdate(UpdateView):
    model = Blog
    fields = ['title', 'description']

class BlogDelete(DeleteView):
    model = Blog
    success_url = reverse_lazy('blogs')


class BloggerCreate(CreateView):
    model = Blogger
    fields = ['first_name', 'last_name','bio']

class BloggerUpdate(UpdateView):
    model = Blogger
    fields = ['last_name', 'bio']

class BloggerDelete(DeleteView):
    model = Blogger
    success_url = reverse_lazy('bloggers')