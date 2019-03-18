from django.urls import path, include
from . import views
from core import views as core_views

urlpatterns =[
    # path('accounts/', include('registration.backends.simple.urls')),
    path('',views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('book/<slug:slug>', views.BookDetailView.as_view(), name='book-detail'),
    path('categories/<slug:slug>', views.CategoryListView.as_view(), name='category-list'),
    path('category/<slug:slug>', views.CategoryDetailView.as_view(), name='category-detail'), # this is working when clicked on from book details
    path('book/<slug:slug>/favorite/', core_views.book_favorite_view, name="book_favorite"),
]

# don't think I need CategoryDetailView. Not really using the details of languages for this exercise