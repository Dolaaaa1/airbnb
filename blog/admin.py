from django.contrib import admin
from .models import Post ,Category
from tof.admin import TofAdmin, TranslationTabularInline

# Register your models here.

class CategoryAdmin(TofAdmin):
    list_display = ['id','name']
    inlines = (TranslationTabularInline, )


admin.site.register(Post)
admin.site.register(Category,CategoryAdmin)
