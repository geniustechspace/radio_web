from django.urls import path
from .views import home_view, program_schedule_view

urlpatterns = [
    path('', home_view, name='home'),
    path('program-schedule/', program_schedule_view, name='program_schedule'),
]
