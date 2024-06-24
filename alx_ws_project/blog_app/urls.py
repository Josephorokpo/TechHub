from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("article/<slug:slug>/", views.detail, name="detail"),
    path("about/", views.about, name="about"),
    path("contact_us/", views.contact_us, name="contact_us"),
    path("create_article/", views.create_article, name="create-article"),
    path('article/<slug:slug>/edit/', views.update_article, name='update-article'),
    path('article/<slug:slug>/delete/', views.delete_article, name='delete-article'),
    path('comment/reply/<int:comment_id>/', views.reply_comment, name='reply-comment'),
    path('search/', views.search_results, name='search'),
    path('category/<int:category_id>/', views.category_articles, name='category-articles'),
]