from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.models import Page
from modelcluster.fields import ParentalKey
from wagtail.fields import StreamField


class News(models.Model):

    caption = models.CharField(max_length=250, verbose_name="Описание новости")

    text_before_photo = models.TextField(verbose_name="Текст над картинкой", blank=True, null=True)

    image = models.ForeignKey('wagtailimages.Image',
                              on_delete=models.CASCADE,
                              related_name='+',
                              verbose_name='Картинка новости')

    text_after_photo = models.TextField(verbose_name="Текст под картинкой", blank=True, null=True)

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

    caption = models.TextField(null=True, verbose_name="Подпись")

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
    rating = models.IntegerField(verbose_name='Количество звезд', default=5)
    page = ParentalKey(
        'home.HomePage',
        on_delete=models.CASCADE,
        related_name='reviews',
        default=3
    )

    panels = [
        FieldPanel('author'),
        FieldPanel('content')
    ]


class AboutInfo(models.Model):

    information = models.TextField(verbose_name='информация о фонде')
    phone_number = models.CharField(max_length=20,
                                    unique=True,
                                    blank=False,
                                    verbose_name='номер телефона')

    second_phone_number = models.CharField(max_length=20,
                                           unique=True,
                                           blank=True,
                                           null=True,
                                           verbose_name='дополнительный номер телефона')

    email = models.EmailField(max_length=255, verbose_name='адрес электронной почты')
    address = models.TextField(verbose_name='полный адрес')
    page = ParentalKey(
        'home.HomePage',
        on_delete=models.CASCADE,
        related_name='about'
    )

    panels = [
        FieldPanel('information'),
        FieldPanel('phone_number'),
        FieldPanel('second_phone_number'),
        FieldPanel('email'),
        FieldPanel('address')
    ]


class Report(models.Model):
    file = models.FileField(verbose_name='отчёт')
    create_date = models.DateField(auto_now_add=True, blank=True, null=True)

    page = ParentalKey(
        'home.HomePage',
        on_delete=models.CASCADE,
        related_name='reports'
    )
    panels = [
        FieldPanel('file')
    ]


class HomePage(Page):

    content_panels = Page.content_panels + [
        MultiFieldPanel([InlinePanel('news', label='новость')],
                        heading='Новости'),
        MultiFieldPanel([InlinePanel('programs', label='программу')],
                        heading='Программы'),
        MultiFieldPanel([InlinePanel('reviews', label='отзыв')],
                        heading='Отзывы'),
        MultiFieldPanel([InlinePanel('about', label='информацию', max_num=1)], heading='Информация'),
        MultiFieldPanel([InlinePanel('reports', label='отчёт')], heading='Отчеты')
    ]


class Appeal(models.Model):

    type = models.IntegerField()
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    option = models.IntegerField()


#class Partner(models.Model):
#
#    name = models.CharField(max_length=50, blank=False, verbose_name='Имя')
#    last_name = models.CharField(max_length=50, blank=False, verbose_name='Фамилия')
#    phone_number = models.CharField(max_length=20,
#                                    unique=True,
#                                    blank=False,
#                                    verbose_name='Номер телефона')
#    email = models.EmailField(blank=True, null=True, verbose_name='Email')
#    message = models.TextField(blank=True, null=True, verbose_name='Сообщение')
#    is_agree = models.BooleanField(default=False, verbose_name='Согласие с обработкой персональных данных')
