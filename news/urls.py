from django.urls import path
from .views import (show_category, contact_page, about_page, not_found_page, NewsListView,
                    NewsDetailView,HomePageView,edit_news,delete_news,NewUpdateView,NewsDeleteView,NewsCreateView)

urlpatterns = [
    path("news/create/",NewsCreateView.as_view(),name='create-news'),
    path('news/<slug:slug>/',NewsDetailView.as_view(),name='news-detail'),
    path('',HomePageView.as_view(),name='home-page'),
    path('about/',about_page,name='about-page'),
    path('contact/',contact_page,name='contact-page'),
    path('not-found/',not_found_page,name='not-found'),
    path('<str:category>/',show_category,name='category-news'),
    path("news/<int:pk>/edit/",NewUpdateView.as_view(),name='edit-news'),
    path("news/<int:pk>/delete/",NewsDeleteView.as_view(),name='delete-news'),

]