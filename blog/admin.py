from django.contrib import admin
from blog.models import Blog, Blogger, Comment


admin.site.register(Blog)
admin.site.register(Blogger)
admin.site.register(Comment)
