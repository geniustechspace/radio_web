from django.shortcuts import render
from .models import PodcastEpisodePage

def podcasts_view(request):
    podcasts = PodcastEpisodePage.objects.live().order_by('-publish_date')
    return render(request, 'podcasts/podcasts_page.html', {"podcasts": podcasts})
