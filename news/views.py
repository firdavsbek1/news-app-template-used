from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
import math
from django.db.models import Q
from django.urls import reverse_lazy
from .models import News
from django.views import generic
from .forms import ContactModelForm, NewsModelForm, ReviewForm
from .custom_permission import IsAdminOrReadOnly
from hitcount.models import HitCount
from hitcount.views import HitCountMixin,HitCountDetailView


class HomePageView(generic.ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['business_news'] = News.ready.all().filter(category__name='business')[:5]
        context['crime_news'] = News.ready.all().filter(category__name='crime')[:5]
        context['tech_news'] = News.ready.all().filter(category__name='technology')[:5]
        context['sports_news'] = News.ready.all().filter(category__name='sports')[:5]
        context['sliders'] = News.ready.all().order_by('-published_time')[:10]
        return context


def about_page(request):
    return render(request, 'about.html')


def show_category(request, category):
    news_list = News.ready.filter(category__name=category)
    return render(request, 'category.html',
                  context={"news_list": news_list,
                           "category": category,
                           "category_counter": math.ceil(len(news_list) / 2) + 1})


@login_required()
def delete_news(request, id):
    news_item = News.objects.get(id=id)
    if request.method == "POST":
        news_item.delete()
        return redirect('home-page')
    context = {
        'news': news_item,
    }
    return render(request, 'delete.html', context)


@login_required()
def edit_news(request, id):
    news_item = News.objects.get(id=id)
    if request.method == "POST":
        form = NewsModelForm(request.POST, request.FILES, instance=news_item)
        if form.is_valid():
            news = form.save()
            return redirect('news-detail', slug=news.slug)

    form = NewsModelForm(instance=news_item)
    context = {
        'news': news_item,
        'form': form
    }
    return render(request, 'edit.html', context)


def contact_page(request):
    form = ContactModelForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home-page')
    return render(request, 'contact.html')


@user_passes_test(lambda user: user.is_superuser)
def admin_page(request):
    admin_users = User.objects.filter(is_superuser=True)
    return render(request, 'admin.html', {'users': admin_users})


def not_found_page(request):
    return render(request, '404.html')


class NewsListView(generic.ListView):
    model = News
    template_name = 'news/news-list.html'
    context_object_name = 'news_list'

    def get_queryset(self):
        return super().get_queryset().filter(status=News.Choice.ready_paper)


class NewsDetailView(HitCountDetailView):
    model = News
    template_name = 'single_page.html'
    context_object_name = 'news'
    pk_url_kwargs = 'slug'
    count_hit = True

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['reviews'] = self.get_object().reviews.filter(active=True)
        context_data['reviews_count'] = context_data['reviews'].count()
        return context_data

    def post(self, request, *args, **kwargs):
        news = self.get_object()
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.user = request.user
            new_review.news = news
            new_review.save()
        return render(request, self.template_name,context={"news":news,
                                                           'reviews': news.reviews.filter(active=True),
                                                           'reviews_count':self.get_object().reviews.filter(active=True).count()
                                                           })


class NewUpdateView(IsAdminOrReadOnly, generic.UpdateView):
    model = News
    template_name = 'edit.html'
    context_object_name = 'news'
    form_class = NewsModelForm

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class NewsDeleteView(IsAdminOrReadOnly, generic.DeleteView):
    model = News
    template_name = 'delete.html'
    context_object_name = 'news'
    success_url = reverse_lazy('home-page')


class NewsCreateView(IsAdminOrReadOnly, generic.CreateView):
    model = News
    template_name = 'edit.html'
    form_class = NewsModelForm

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)


class NewsSearchView(generic.ListView):
    model = News
    template_name = 'category.html'
    context_object_name = 'news_list'

    def get_queryset(self, *args, **kwargs):
        search_query = self.request.GET.get('q')
        return News.ready.filter(
            Q(title__icontains=search_query) | Q(body__icontains=search_query) | Q(category__name=search_query))

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['category'] = "Search Page"
        context_data['category_counter'] = math.ceil(len(self.get_queryset()) / 2) + 1
        return context_data

# def news_list(request):
#     # news_list_all=News.objects.all()
#     news_list_all=News.ready.all()
#     return render(request,'news/news-list.html',{'news_list':news_list_all})
#
#


def news_detail(request,slug):
    context={}
    news_object = get_object_or_404(News,slug=slug,status=News.Choice.ready_paper)
    hit_count_object=HitCount.objects.get_for_object(news_object)
    hits=hit_count_object.hits
    context['hitcount']={'pk':hit_count_object.pk}
    hit_response=HitCountMixin.hit_count(request,hit_count_object)
    if hit_response.hit_counted:
        hits+=1
        context['hitcount']['hit_counted']=hit_response.hit_counted
        context['hitcount']['hit_message']=hit_response.hit_message
    context['hitcount']['total_hits']=hits
    context['news']=news_object
    return render(request,'single_page.html',context)


# def home_page(request):
#     news = News.ready.all().order_by("-published_time")
#     context={
#         'news_list':news,
#     }
#     return render(request, 'news_list.html', context)
