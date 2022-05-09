from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):

    subtitle = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Подзаголовок'
    )

    content_panels = Page.content_panels + [
        FieldPanel("subtitle")
    ]
