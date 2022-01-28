from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Product, Tag
from django.db.models import Q


def searchProducts(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    tags = Tag.objects.filter(name__icontains=search_query)
    products = Product.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(tags__in=tags)
    )
    return products, search_query


def paginateProducts(request, products, results):
    page = request.GET.get('page')
    paginator = Paginator(products, results)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        products = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        products = paginator.page(page)
    return products
