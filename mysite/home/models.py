from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.models import Page, Orderable
from modelcluster.fields import ParentalKey
from wagtail.fields import StreamField


class News(Orderable):

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


class Programs(Orderable):
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


class Feedback(Orderable):

    author = models.CharField(max_length=50, verbose_name='Имя автора')
    content = models.TextField(verbose_name='Текст отзыва')
    rating = models.IntegerField(verbose_name='Количество звезд', default=5)
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

    page = ParentalKey(
        'home.HomePage',
        on_delete=models.CASCADE,
        related_name='reviews',
        default=3
    )

    panels = [
        FieldPanel('author'),
        FieldPanel('content'),
        FieldPanel('rating'),
        FieldPanel('is_published')
    ]

    def __str__(self):
        return f"Отзыв номер {self.id}"


    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


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


class Report(Orderable):
    file = models.FileField(upload_to='reports/', verbose_name='отчёт')
    create_date = models.DateField(auto_now_add=True, blank=True, null=True)

    page = ParentalKey(
        'home.HomePage',
        on_delete=models.CASCADE,
        related_name='reports'
    )
    panels = [
        FieldPanel('file')
    ]


class Document(models.Model):
    file = models.FileField(upload_to='documents/', verbose_name='документ')
    create_date = models.DateField(auto_now_add=True, blank=True, null=True)

    page = ParentalKey(
        'home.HomePage',
        on_delete=models.CASCADE,
        related_name='documents'
    )
    panels = [
        FieldPanel('file')
    ]


class HomePage(Page):

    email = models.EmailField(default="dfvrn@admin.ru", null=True, blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([InlinePanel('news', label='новость')],
                        heading='Новости'),
        MultiFieldPanel([InlinePanel('programs', label='программу')],
                        heading='Программы'),
        #MultiFieldPanel([InlinePanel('reviews', label='отзыв')],
        #                heading='Отзывы'),
        MultiFieldPanel([InlinePanel('about', label='информацию', max_num=1)], heading='Информация'),
        MultiFieldPanel([InlinePanel('reports', label='отчёт')], heading='Отчеты'),
        MultiFieldPanel([InlinePanel('documents', label='документ')],
                        heading='Документы')
    ]


class Appeal(models.Model):

    TYPE_CHOICES = (
        (1, 'Помощь'),
        (2, 'Консультация'),
        (3, 'Волонтерство')
    )

    OPTION_CHOICES = (
        (1, 'SOS размещение'),
        (2, 'Гуманитарная помощь'),
        (3, 'Необходим адресный сбор'),
        (4, 'Koнсультация психолога'),
        (5, 'Консультация юриста'),
        (6, 'Хочу в группу поддержки'),
        (7, 'Хочу быть волонтером фонда')
    )

    STATUS_CHOICES = (
        ('new', 'Новый'),
        ('work', 'В работе'),
        ('done', 'Выполнен'),
        ('archive', 'В архиве')
    )

    type = models.IntegerField(
        verbose_name='Тип обращения',
        choices=TYPE_CHOICES
    )
    name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(
        max_length=20, verbose_name='Фамилия',
        blank=True, null=True
    )
    phone_number = models.CharField(
        max_length=20, verbose_name='Телефон',
        blank=True, null=True
    )
    option = models.IntegerField(
        verbose_name='Тип требуемой помощи',
        choices=OPTION_CHOICES
    )
    status = models.CharField(
        max_length=50, verbose_name="Статус",
        choices=STATUS_CHOICES, default='new',
        null=False, blank=False
    )
    create_date = models.DateField(auto_now_add=True, verbose_name="Дата обращения")
    notes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'
        constraints = (
            models.CheckConstraint(
                check=models.Q(type__gte=1) & models.Q(type__lte=3),
                name='appeal_type_constraint'
            ),
            models.CheckConstraint(
                check=models.Q(option__gte=1) & models.Q(option__lte=7),
                name='appeal_option_constraint'
            ),
            models.CheckConstraint(
                check=models.Q(status='new') | models.Q(status='work') |
                models.Q(status='done') | models.Q(status='archive'),
                name='appeal_status_constraint'
            )
        )



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
