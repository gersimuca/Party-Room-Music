from django.db.models import F
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView

from form_view.forms import AddForm
from form_view.models import BooksFV


class IndexView(ListView):
    template_name = "form_view/home.html"
    model = BooksFV
    context_object_name = 'books'
    paginate_by = 4

    # queryset = Books.objects.all()[:2]

    def get_queryset(self):
        return BooksFV.objects.all()[:3]


class GenreView(ListView):
    model = BooksFV
    template_name = 'form_view/home.html'
    context_object_name = 'books'
    paginate_by = 2  # Pagination over-write

    def get_queryset(self, *args, **kwargs):
        return BooksFV.objects.filter(genre__icontains=self.kwargs.get('genre'))


class BookDetailView(DetailView):
    model = BooksFV
    template_name = 'form_view/book-detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = BooksFV.objects.filter(slug=self.kwargs.get('slug'))
        post.update(count=F('count') + 1)

        context['time'] = timezone.now()

        return context


class AddBookView(FormView):
    template_name = 'form_view/add.html'
    form_class = AddForm
    success_url = '/f/books/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
