from django.shortcuts import render
from core.models import Book, Category
from django.views import generic

# Create your views here.
def index(request):
    """View function home page of site"""

    # in case we want to count stuff
    num_books = Book.objects.all().count()
    num_categories = Category.objects.all().count()

    context = {
        'num_books': num_books,
        'num_categories': num_categories,
    }

    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 5

class BookDetailView(generic.DetailView):
    model = Book

class CategoryListView(generic.ListView):
    model = Category
    paginate_by = 5

class CategoryDetailView(generic.DetailView):
    model = Category
