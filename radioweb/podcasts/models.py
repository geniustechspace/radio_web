from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from django.core.validators import FileExtensionValidator

class PodcastEpisodePage(Page):
    audio_file = models.FileField(
        upload_to='podcasts/',
        validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav', 'ogg'])],
        blank=True,
        null=True
    )
    summary = RichTextField()
    publish_date = models.DateField()

    content_panels = Page.content_panels + [
        FieldPanel('audio_file'),
        FieldPanel('summary'),
        FieldPanel('publish_date'),
    ]
