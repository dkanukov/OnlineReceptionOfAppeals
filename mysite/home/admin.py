from django.contrib import admin
from .models import Appeal, Feedback
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)


class FeedbackAdmin(ModelAdmin):
    """Администрирование отзывов в Wagtail"""
    model = Feedback
    menu_label = "Отзывы"
    menu_icon = "mail"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('author', 'content', 'rating', 'is_published')


modeladmin_register(FeedbackAdmin)


class AppealAdmin(admin.ModelAdmin):
    list_display = (
        'type',
        'name',
        'last_name',
        'phone_number',
        'option'
    )

    search_fields = ('type', 'option')


admin.site.register(Appeal, AppealAdmin)
