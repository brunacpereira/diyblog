from django.conf.urls import include
from django.urls import path
from blog import views
from django.views.generic import RedirectView
# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [  
    path('', views.index, name='index'),  
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('bloggers/', views.BloggerListView.as_view(), name='bloggers'),
    path('blogger/<int:pk>', views.BloggerDetailView.as_view(), name='blogger-detail'),
    path('blog/<int:pk>/new-comment/', views.new_comment_blog, name='new-comment-blog'),
    path('blog/create/', views.BlogCreate.as_view(), name='blog_create'),
    path('blog/<int:pk>/update/', views.BlogUpdate.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete/', views.BlogDelete.as_view(), name='blog_delete'),
    path('blogger/create/', views.BloggerCreate.as_view(), name='blogger_create'),
    path('blogger/<int:pk>/update/', views.BloggerUpdate.as_view(), name='blogger_update'),
    path('blogger/<int:pk>/delete/', views.BloggerDelete.as_view(), name='blogger_delete'),
]

