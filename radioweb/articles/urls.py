from django.urls import path
from .views import articles_view, article_detail_view 

urlpatterns = [
    path('', articles_view, name='articles'),
    path('<int:pk>/', article_detail_view, name='article_detail'),
]
