from django.urls import path
from .views import ads_list_view, ad_detail_view 

urlpatterns = [
    path('', ads_list_view, name='advertisements'),
    path('<int:pk>/', ad_detail_view, name='ad_detail'),
]
