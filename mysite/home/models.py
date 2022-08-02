from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.models import Page
from modelcluster.fields import ParentalKey
from wagtail import blocks
from wagtail.fields import StreamField


class News(models.Model):

    caption = models.CharField(max_length=250, verbose_name="Описание новости")

    text_before_photo = models.TextField(verbose_name="Текст над картинкой")

    image = models.ForeignKey('wagtailimages.Image',
                              on_delete=models.CASCADE,
                              related_name='+',
                              verbose_name='Картинка новости')

    text_after_photo = models.TextField(verbose_name="Текст под картинкой")

    additional_images = StreamField([('photo', ImageChooserBlock())],
                                    verbose_name="Фотоотчет",
                                    blank=True,
                                    null=True)

    create_date = models.DateField(auto_now_add=True, blank=True, null=True)

    page = ParentalKey(
        'home.HomePage',
        on_delete=models.CASCADE,
        related_name='news'
    )
    panels = [
        FieldPanel('caption'),
        FieldPanel('text_before_photo'),
        ImageChooserPanel('image'),
        FieldPanel('text_after_photo'),
        FieldPanel('additional_images')
    ]


class Programs(models.Model):
    title = models.CharField(max_length=100, null=True, verbose_name='Название программы')

    caption = models.CharField(max_length=250, null=True, verbose_name="Подпись")

    description = models.TextField(null=True, verbose_name="Описание программы")

    create_date = models.DateField(auto_now_add=True, blank=True, null=True)

    image = models.ForeignKey('wagtailimages.Image',
                              on_delete=models.CASCADE,
                              related_name='+',
                              verbose_name='Картинка программы')

    page = ParentalKey(
        'home.HomePage',
        on_delete=models.CASCADE,
        related_name='programs'
    )
    panels = [
        ImageChooserPanel('image'),
        FieldPanel('title'),
        FieldPanel('caption'),
        FieldPanel('description')
    ]


class Feedback(models.Model):

    author = models.CharField(max_length=50, verbose_name='Имя автора')
    content = models.TextField(verbose_name='Текст отзыва')
    page = ParentalKey(
        'home.HomePage',
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    panels = [
        FieldPanel('author'),
        FieldPanel('content')
    ]


class HomePage(Page):

    content_panels = Page.content_panels + [
        MultiFieldPanel([InlinePanel('news', label='новость')],
                        heading='Новости'),
        MultiFieldPanel([InlinePanel('programs', label='программу')],
                        heading='Программы'),
        MultiFieldPanel([InlinePanel('reviews', label='отзыв')],
                        heading='Отзывы'),
    ]
