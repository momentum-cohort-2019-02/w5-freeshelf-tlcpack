from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, get_object_or_404, redirect
from core.models import Book, Category
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    """View function home page of site"""

    # in case we want to count stuff
    all_books = Book.objects.all()
    all_categories = Category.objects.all()

    context = {
        'all_books': all_books,
        'all_categories': all_categories,
    }

    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 5

class BookDetailView(generic.DetailView):
    model = Book
    

class CategoryListView(generic.ListView):
    model = Category
    

class CategoryDetailView(generic.DetailView):
    model = Category
    
@require_http_methods(['POST'])
@login_required
def book_favorite_view(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)

    # Toggle whether or not book is favorited

    favorite, created = request.user.favorited_books.get_or_create(book=book)

    if created:
        messages.success(request, f"You have favorited {book.title}.")
    else:
        messages.info(request, f"You have unfavorited {book.title}.")
        favorite.delete()

    return redirect(book.get_absolute_url())

# def book_detail_view(request, slug):
#     book = get_object_or_404(Book, slug=slug)
#     return render(request, 'core/book_detail.html', {'book': book})

# def category_list_view(request, pk):
#     category = get_object_or_404(Category, pk=pk)
#     return render(request, 'core/category_list.html', {'category': category})