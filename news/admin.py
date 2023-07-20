from django.contrib import admin
from .models import News,Category,Contact,Review


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','slug','published_time','category']
    list_filter = ['published_time','status','created_time']
    prepopulated_fields = {"slug":('title',)}
    date_hierarchy = 'published_time'
    search_fields = ['title','body']
    ordering = ['status','published_time']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user','news','created_time','active']
    list_filter = ['created_time','active','user']
    search_fields = ['body',]
    actions = ['disable_reviews','enable_reviews']

    def disable_reviews(self,request,queryset):
        queryset.update(active=False)

    def enable_reviews(self,request,queryset):
        queryset.update(active=True)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']


admin.site.register(Category,CategoryAdmin)
admin.site.register(Contact)
admin.site.register(Review,ReviewAdmin)