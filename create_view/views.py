from django.db.models import F
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from create_view.forms import AddForm
from create_view.models import BooksCV


class IndexView(ListView):
    template_name = "create_view/home.html"
    model = BooksCV
    context_object_name = 'books'
    paginate_by = 4

    # queryset = Books.objects.all()[:2]

    def get_queryset(self):
        return BooksCV.objects.all()[:3]


class GenreView(ListView):
    model = BooksCV
    template_name = 'create_view/home.html'
    context_object_name = 'books'
    paginate_by = 2  # Pagination over-write

    def get_queryset(self, *args, **kwargs):
        return BooksCV.objects.filter(genre__icontains=self.kwargs.get('genre'))


class BookDetailView(DetailView):
    model = BooksCV
    template_name = 'create_view/book-detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = BooksCV.objects.filter(slug=self.kwargs.get('slug'))
        post.update(count=F('count') + 1)

        context['time'] = timezone.now()

        return context


class AddBookView(CreateView):
    model = BooksCV
    template_name = 'create_view/add.html'
    form_class = AddForm
    success_url = '/c/books/'
