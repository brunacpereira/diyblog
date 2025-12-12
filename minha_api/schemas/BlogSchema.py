# from minha_api.schemas.BlogSchema import BloggerSchema
from datetime import datetime
from blog.models import Blog
from ninja import Schema, ModelSchema, FilterSchema, Field

class BlogIn(ModelSchema):
    class Meta:
        model = Blog 
        fields = "__all__"

class BlogOut(Schema):
    title: str  
    description: str 
