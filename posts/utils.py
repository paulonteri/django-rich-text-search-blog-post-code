from django.contrib.postgres.search import SearchVector
from django.db.models import Q

from posts.models import Post


def posts_basic_search(query: str):
    return Post.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    )


def posts_richtext_search_search(query: str):
    return Post.objects.filter(description__search=query)


def posts_richtext_search_search_vector(query: str):
    Post.objects.annotate(search=SearchVector("title", "description")).filter(
        search=query
    )
