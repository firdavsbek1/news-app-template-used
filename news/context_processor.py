from .models import News,Category,Review
import math


def processor(reqeust):
    context={
        'category_list':Category.objects.all(),
        'latest_news':News.ready.all().order_by('-published_time')[:10],
        'popular_posts':News.ready.all().order_by('published_time')[:10],
        'all_news':News.objects.all(),
        'news_counter':math.ceil(len(News.objects.all())/2),
        'reviews_all':Review.objects.all().order_by('-created_time')[:20]
    }
    return context
