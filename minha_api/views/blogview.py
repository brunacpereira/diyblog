from ninja import NinjaAPI, Router, Query, File, Form
from blog.models import Blog
from minha_api.schemas.BlogSchema import BlogIn, BlogOut

blog_router = Router()

@blog_router.post("/", response={201:BlogOut})
def criar_blog(request, payload: BlogIn):
    """
    Cria um novo artigo no blog a partir dos dados fornecidos nos parâmetros de entrada
    """
    blog = Blog.objects.create(
        title=payload.title,
        blogger=payload.blogger,
        description=payload.description
    )

    return blog