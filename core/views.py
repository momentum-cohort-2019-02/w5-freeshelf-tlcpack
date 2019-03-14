from django.shortcuts import render, get_object_or_404
from core.models import Book, Category
from django.views import generic

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
    paginate_by = 5

class CategoryDetailView(generic.DetailView):
    model = Category
    
# def book_detail_view(request, slug):
#     book = get_object_or_404(Book, slug=slug)
#     return render(request, 'core/book_detail.html', {'book': book})

# def category_list_view(request, pk):
#     category = get_object_or_404(Category, pk=pk)
#     return render(request, 'core/category_list.html', {'category': category})