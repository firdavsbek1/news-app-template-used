from django.urls import path
from .views import (show_category, contact_page, about_page, not_found_page, NewsListView,
                    NewsDetailView,HomePageView)

urlpatterns = [
    path('news/',NewsListView.as_view(),name='news-list'),
    path('news/<slug:slug>/',NewsDetailView.as_view(),name='news-detail'),
    path('',HomePageView.as_view(),name='home-page'),
    path('about/',about_page,name='about-page'),
    path('contact/',contact_page,name='contact-page'),
    path('not-found/',not_found_page,name='not-found'),
    path('<str:category>/',show_category,name='category-news'),

]