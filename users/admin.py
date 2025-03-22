from django.contrib import admin
from .models import Moshinalar

@admin.register(Moshinalar)
class MoshinalarAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'price')
    list_filter = ('price','description')