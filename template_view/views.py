from django.views.generic.base import TemplateView
from template_view.models import PostTV


class Sample2View(TemplateView):
    template_name = "template_view/sample2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = PostTV.objects.get(id=1)
        context['data'] = "Context Data for Sample2"
        return context
