from django.urls import path
from .views import podcasts_view 

urlpatterns = [
    path('', podcasts_view, name='podcasts'), 
]
