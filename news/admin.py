from django.contrib import admin
from .models import News,Category,Contact


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','slug','published_time','category']
    list_filter = ['published_time','status','created_time']
    prepopulated_fields = {"slug":('title',)}
    date_hierarchy = 'published_time'
    search_fields = ['title','body']
    ordering = ['status','published_time']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Contact)
