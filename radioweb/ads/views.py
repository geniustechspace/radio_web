from django.shortcuts import render, get_object_or_404
from .models import Advertisement


def ads_list_view(request):
    """
    View to display a list of all advertisements.
    """
    ads = Advertisement.objects.prefetch_related('images').order_by('-id')
    return render(request, 'ads/ads_list.html', {'ads': ads})


def ad_detail_view(request, pk):
    """
    View to display details of a single advertisement.
    """
    ad = get_object_or_404(Advertisement.objects.prefetch_related('images'), pk=pk)
    return render(request, 'ads/ad_detail.html', {'ad': ad})
