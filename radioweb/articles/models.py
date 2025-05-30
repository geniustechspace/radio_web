from django.db import models
from django.contrib.auth import get_user_model
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.blocks import (
    RichTextBlock,
    StructBlock,
    URLBlock,
    CharBlock
)
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel
from wagtail import blocks

User = get_user_model()


# Optional: custom link block
class LinkBlock(StructBlock):
    text = CharBlock(required=True, help_text="Link text")
    url = URLBlock(required=True, help_text="Destination URL")

    class Meta:
        icon = "link"
        label = "Link"
        template = "blocks/link_block.html"

# ARTICLE PAGE
class ArticlePage(Page):
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='articles'
    )
    date_published = models.DateField("Date Published")
    body = StreamField(
        [
            ("paragraph", RichTextBlock(features=["bold", "italic", "link", "ol", "ul", "hr"])),
            ("image", ImageChooserBlock()),
            ("link", LinkBlock()),
        ],
        use_json_field=True,
        blank=True
    )
    is_sponsored = models.BooleanField(default=False)


    content_panels = Page.content_panels + [
        FieldPanel("author"),
        FieldPanel("date_published"),
        FieldPanel("body"),
        FieldPanel("is_sponsored"),
    ]

    class Meta:
        verbose_name = "Article Page"
