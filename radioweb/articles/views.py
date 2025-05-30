from django.shortcuts import render, get_object_or_404
from .models import ArticlePage

def articles_view(request):
    articles = ArticlePage.objects.live().order_by('-date_published')
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail_view(request, pk):
    page = get_object_or_404(ArticlePage.objects.live(), id=pk)
    return render(request, 'articles/article_detail.html', {'page': page})