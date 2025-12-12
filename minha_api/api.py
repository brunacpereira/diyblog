from ninja import NinjaAPI, Schema
from .views.blogview import blog_router

api = NinjaAPI(urls_namespace="minha_api") # Instancia a API

api.add_router("blogs/", blog_router, tags=["Blogs"])


