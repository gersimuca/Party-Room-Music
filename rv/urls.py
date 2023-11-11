from django.urls import path
from django.views.generic import TemplateView, RedirectView
from rv.views import Sample2View, PostPreLoadTaskView, SinglePostView

app_name = 'rv'

urlpatterns = [
    # extra_context Attribute from ContentMixin - keyword argument for as_view()
    path('', TemplateView.as_view(template_name="rv/sample1.html",
                                  extra_context={
                                      'title': 'Custom Title or Testing TemplateView',
                                      'name': 'Gersi Muca'}
                                  )),
    path('sample2/', Sample2View.as_view(), name='sample2'),

    path('redirect', RedirectView.as_view(url='http://aol.com/'), name='go-to-aol-mail'),
    path('sample3/<int:pk>/', PostPreLoadTaskView.as_view(), name='redirect-task'),
    path('sample4/<int:pk>/', SinglePostView.as_view(), name='singlepost'),  # single post page
]