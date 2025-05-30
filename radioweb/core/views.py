from django.shortcuts import render
from django.utils.timezone import now
from .models import ProgramSchedule
from podcasts.models import PodcastEpisodePage
from .models import SiteInfoSettings

def home_view(request):
    programs = ProgramSchedule.objects.all()
    program_count = programs.count()
    podcast_count = PodcastEpisodePage.objects.live().count()


    try:
        site = SiteInfoSettings.for_request(request)
        stream_url = site.streaming_url
    except SiteInfoSettings.DoesNotExist:
        stream_url = ""
            
    # Get upcoming program (for today)
    current_time = now().time()
    today = now().strftime('%A')  # 'Monday', 'Tuesday', etc.

    upcoming_program = (
        programs
        .filter(day_of_week=today, start_time__gte=current_time)
        .order_by('start_time')
        .first()
    )

    recent_activities = [
        {"type": "program", "message": "🎙️ Afternoon Jazz started at 2:00 PM"},
        {"type": "schedule", "message": "📅 New schedule added for Tech Talk"},
        {"type": "listener", "message": "🎧 50 new listeners joined at 3:00 PM"},
    ]

    # stream_url = SiteInfoSettings.for_request(request).streaming_url

    return render(request, 'core/home_page.html', {
        "program_count": program_count,
        "podcast_count": podcast_count,
        "upcoming_program": upcoming_program,
        "recent_activities": recent_activities,
        "programs": programs.order_by('day_of_week', 'start_time'),
        "stream_url": stream_url,
    })

def program_schedule_view(request):
    schedules = ProgramSchedule.objects.all().order_by('day_of_week', 'start_time')
    return render(request, 'core/program_schedule.html', 
                  {'programs': schedules, 
                   })