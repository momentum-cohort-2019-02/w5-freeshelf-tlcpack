from django.urls import path, include
from . import views

urlpatterns =[
    # path('accounts/', include('registration.backends.simple.urls')),
    path('',views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('categories/<int:pk>', views.CategoryListView.as_view(), name='category-list'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'), # this is working when clicked on from book details
    path('book/<int:book_pk>/favorite/', views.book_favorite_view, name="book_favorite"),
]

# don't think I need CategoryDetailView. Not really using the details of languages for this exercise