from django.urls import path
from . import views

urlpatterns =[
    path('',views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('categories/<int:pk>', views.CategoryListView.as_view(), name='category-list'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),
]

# don't think I need CategoryDetailView. Not really using the details of languages for this exercise