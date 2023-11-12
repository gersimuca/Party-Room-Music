from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from detail_view.models import BooksDV
from django.db.models import F
from django.utils import timezone


class IndexView(TemplateView):
    template_name = "detail_view/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = BooksDV.objects.all()
        return context


class BookDetailView(DetailView):
    model = BooksDV
    template_name = 'detail_view/book-detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = BooksDV.objects.filter(slug=self.kwargs.get('slug'))
        post.update(count=F('count') + 1)

        context['time'] = timezone.now()

        return context
