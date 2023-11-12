from django.db.models import F
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from list_view.models import BooksLV


class IndexView(ListView):
    template_name = "list_view/home.html"
    model = BooksLV
    context_object_name = 'books'
    paginate_by = 4

    # queryset = Books.objects.all()[:2]

    def get_queryset(self):
        return BooksLV.objects.all()[:3]


class GenreView(ListView):
    model = BooksLV
    template_name = 'list_view/home.html'
    context_object_name = 'books'
    paginate_by = 2  # Pagination over-write

    def get_queryset(self, *args, **kwargs):
        return BooksLV.objects.filter(genre__icontains=self.kwargs.get('genre'))


class BookDetailView(DetailView):
    model = BooksLV
    template_name = 'list_view/book-detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = BooksLV.objects.filter(slug=self.kwargs.get('slug'))
        post.update(count=F('count') + 1)

        context['time'] = timezone.now()

        return context
