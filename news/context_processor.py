from .models import News,Category
import math

def processor(reqeust):
    context={
        'category_list':Category.objects.all(),
        'latest_news':News.ready.all().order_by('-published_time')[:10],
        'popular_posts':News.ready.all().order_by('published_time')[:10],
        'all_news':News.objects.all(),
        'news_counter':math.ceil(len(News.objects.all())/2)
    }
    return context
