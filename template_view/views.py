from django.views.generic.base import TemplateView, RedirectView
from template_view.models import Post
from django.shortcuts import get_object_or_404
from django.db.models import F


class Sample2View(TemplateView):
    template_name = "template_view/sample2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.get(id=1)
        context['data'] = "Context Data for Sample2"
        return context


class PostPreLoadTaskView(RedirectView):
    # url = 'http://youtube.com/'
    pattern_name = 'sample2:singlepost'

    # permanent = HTTP status code return (True = 301, False = 302, Default = False)

    def get_redirect_url(self, *args, **kwargs):
        # post = get_object_or_404(Post, pk=kwargs['pk'])
        # post.count = F('count') + 1
        # post.save()
        post = Post.objects.filter(pk=kwargs['pk'])
        post.update(count=F('count') + 1)

        return super().get_redirect_url(*args, **kwargs)
