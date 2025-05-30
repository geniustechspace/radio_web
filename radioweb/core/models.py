from django.contrib.auth.models import AbstractUser
from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.fields import RichTextField

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('journalist', 'Journalist'),
        ('advertiser', 'Advertiser'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='journalist')

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
    
    def get_role_display(self):
        return dict(self.ROLE_CHOICES).get(self.role, 'Unknown')
    


@register_snippet
class ProgramSchedule(models.Model):
    title = models.CharField(max_length=100)
    presenter = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    day_of_week = models.CharField(max_length=20)  # e.g., Monday, Tuesday

    def __str__(self):
        return f"{self.title} ({self.day_of_week} {self.start_time}-{self.end_time})"



@register_setting
class SiteInfoSettings(BaseSiteSetting):
    streaming_url = models.URLField(help_text="Main streaming URL")
    contact_email = models.EmailField()
    about = RichTextField(blank=True)
