from django.contrib import admin

from .models import Interview

@admin.register(Interview)
class Interview(admin.ModelAdmin):
    pass
