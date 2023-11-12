from django.db.models import F
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login

from update_view.forms import AddForm
from update_view.models import BooksUV


class IndexView(ListView):
    template_name = "update_view/home.html"
    model = BooksUV
    context_object_name = 'books'
    paginate_by = 4

    # queryset = Books.objects.all()[:2]

    def get_queryset(self):
        return BooksUV.objects.all()[:3]


class GenreView(ListView):
    model = BooksUV
    template_name = 'update_view/home.html'
    context_object_name = 'books'
    paginate_by = 2  # Pagination over-write

    def get_queryset(self, *args, **kwargs):
        return BooksUV.objects.filter(genre__icontains=self.kwargs.get('genre'))


class BookDetailView(DetailView):
    model = BooksUV
    template_name = 'update_view/book-detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = BooksUV.objects.filter(slug=self.kwargs.get('slug'))
        post.update(count=F('count') + 1)

        context['time'] = timezone.now()

        return context


class AddBookView(CreateView):
    model = BooksUV
    template_name = 'update_view/add.html'
    form_class = AddForm
    success_url = '/u/books/'


class UserAccessMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect_to_login(
                self.request.get_full_path(),
                self.get_login_url(),
                self.get_redirect_field_name()
            )
        if not self.has_permission():
            return redirect('/u/books/')
        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)


class BookEditView(UserAccessMixin, UpdateView):
    raise_exception = True
    permission_required = ('update_view.change_booksuv',)
    model = BooksUV
    template_name = 'update_view/add.html'
    form_class = AddForm
    success_url = '/u/books/'

