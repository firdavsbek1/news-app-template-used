from django.urls import path
from .views import (show_category, contact_page, about_page, not_found_page,admin_page,
                    NewsDetailView,HomePageView,NewUpdateView,NewsDeleteView,NewsCreateView,NewsSearchView)

urlpatterns = [
    path("news/create/",NewsCreateView.as_view(),name='create-news'),
    path('news/<slug:slug>/',NewsDetailView.as_view(),name='news-detail'),
    # path('news/<slug:slug>/',news_detail,name='news-detail'),
    path('',HomePageView.as_view(),name='home-page'),
    path('about/',about_page,name='about-page'),
    path('contact/',contact_page,name='contact-page'),
    path('not-found/',not_found_page,name='not-found'),
    path('category/<str:category>/',show_category,name='category-news'),
    path("news/<int:pk>/edit/",NewUpdateView.as_view(),name='edit-news'),
    path("news/<int:pk>/delete/",NewsDeleteView.as_view(),name='delete-news'),
    path('admin-page/',admin_page,name='admin-page'),
    path('search-view/',NewsSearchView.as_view(),name='search-news'),

]