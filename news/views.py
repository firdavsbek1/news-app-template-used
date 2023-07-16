from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse, reverse_lazy

from .models import News,Category
from django.views import generic
from .forms import ContactModelForm,NewsModelForm
from slugify import slugify


# def news_list(request):
#     # news_list_all=News.objects.all()
#     news_list_all=News.ready.all()
#     return render(request,'news/news-list.html',{'news_list':news_list_all})
#
#
# def news_detail(request,pk):
#     news_object = get_object_or_404(News,id=pk,status=News.Choice.ready_paper)
#     return render(request,'news/news-detail.html',{'news':news_object})


# def home_page(request):
#     news = News.ready.all().order_by("-published_time")
#     context={
#         'news_list':news,
#     }
#     return render(request, 'news_list.html', context)


class HomePageView(generic.ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        context['business_news']=News.ready.all().filter(category__name='business')[:5]
        context['crime_news']=News.ready.all().filter(category__name='crime')[:5]
        context['tech_news']=News.ready.all().filter(category__name='technology')[:5]
        context['sports_news']=News.ready.all().filter(category__name='sports')[:5]
        context['sliders']=News.ready.all().order_by('-published_time')[:4]
        return context


def show_category(request,category):
    news_list = News.ready.filter(category__name=category)
    return render(request, 'category.html', context={"news_list":news_list,"category":category})


def about_page(request):
    return render(request,'about.html')


def delete_news(request,id):
    news_item=News.objects.get(id=id)
    if request.method == "POST":
        news_item.delete()
        return redirect('home-page')
    context = {
        'news':news_item,
    }
    return render(request,'delete.html',context)


def edit_news(request,id):
    news_item=News.objects.get(id=id)
    if request.method=="POST":
        form=NewsModelForm(request.POST,request.FILES,instance=news_item)
        if form.is_valid():
            news=form.save()
            return redirect('news-detail',slug=news.slug)

    form=NewsModelForm(instance=news_item)
    context ={
        'news':news_item,
        'form':form
    }
    return render(request,'edit.html',context)


def contact_page(request):
    form=ContactModelForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home-page')
    return render(request,'contact.html')


def not_found_page(request):
    return render(request,'404.html')


class NewsListView(generic.ListView):
    model = News
    template_name = 'news/news-list.html'
    context_object_name = 'news_list'

    def get_queryset(self):
        return super().get_queryset().filter(status=News.Choice.ready_paper)


class NewsDetailView(generic.DetailView):
    model = News
    template_name = 'single_page.html'
    context_object_name = 'news'
    pk_url_kwargs = 'slug'

    # def get_queryset(self):
    #     return super().get_queryset().filter(self.model.slug=)


class NewUpdateView(generic.UpdateView):
    model = News
    template_name = 'edit.html'
    context_object_name = 'news'
    form_class = NewsModelForm


class NewsDeleteView(generic.DeleteView):
    model = News
    template_name = 'delete.html'
    context_object_name = 'news'
    success_url = reverse_lazy('home-page')


class NewsCreateView(generic.CreateView):
    model = News
    template_name = 'edit.html'
    form_class = NewsModelForm
