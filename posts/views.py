from django.shortcuts import get_object_or_404, render
from taggit.models import Tag

from .forms import PostForm
# from django.template.defaultfilters import slugify
from .models import Post


def home_view(request):
    posts = Post.objects.order_by('-created_date')

    # Mostrar as tags mais comuns
    common_tags = Post.tags.most_common()[:5]
    form = PostForm(request.POST)
    if form.is_valid():
        newpost = form.save(commit=False)
        # newpost.slug = slugify(newpost.title)
        newpost.save()
        # IMPORTANTE
        form.save_m2m()

    context = {
        'posts':posts,
        'common_tags':common_tags,
        'form':form,
    }
    return render(request, 'home.html', context)


def detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'detail.html', {'post':post})

def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug )
    # Filtrar postagens por nome da tag
    posts = Post.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'posts':posts,
    }
    return render(request, 'home.html', context)
