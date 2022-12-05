from django.contrib import admin
from .models import Appeal


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
