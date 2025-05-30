from django.db import models
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from django.core.exceptions import ValidationError


@register_snippet
class Advertisement(ClusterableModel):
    AD_TYPE_CHOICES = [
        ('banner', 'Banner Ad'),
        ('audio', 'Audio Ad'),
    ]

    title = models.CharField(max_length=255)
    ad_type = models.CharField(max_length=10, choices=AD_TYPE_CHOICES)
    target_url = models.URLField(help_text="Where the user will be redirected on click.")
    caption = RichTextField(blank=True, help_text="Optional description or call-to-action.")
    audio_file = models.FileField(
        upload_to='ads/audio/',
        null=True,
        blank=True,
        help_text="Only required for audio ads."
    )

    panels = [
        FieldPanel('title'),
        FieldPanel('ad_type'),
        FieldPanel('target_url'),
        FieldPanel('caption'),
        FieldPanel('audio_file'),
        InlinePanel('images', label="Ad Images"),
    ]

    def __str__(self):
        return self.title

    def clean(self):
        super().clean()

        # If ad_type is banner, audio_file must be empty
        if self.ad_type == 'banner' and self.audio_file:
            raise ValidationError({
                'audio_file': 'Audio file must be empty when the ad type is Banner.'
            })

        # If ad_type is audio, there must be no images
        if self.ad_type == 'audio' and self.images.exists():
            raise ValidationError({
                'images': 'Images must be empty when the ad type is Audio.'
            })



class AdvertisementImage(models.Model):
    advertisement = ParentalKey(
        'Advertisement',
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
    )
    alt_text = models.CharField(max_length=255, blank=True)

    panels = [
        FieldPanel('image'),
        FieldPanel('alt_text'),
    ]

    def __str__(self):
        return self.image.title if self.image else "Image"
