from django.urls import path
from django.views.generic import TemplateView
from tv.views import Sample2View

app_name = 'website'

urlpatterns = [
    # extra_context Attribute from ContentMixin - keyword argument for as_view()
    path('', TemplateView.as_view(template_name="tv/sample1.html",
                                         extra_context={
                                             'title': 'Custom Title or Testing TemplateView',
                                             'name': 'Gersi Muca'}
                                         )),
    path('sample2', Sample2View.as_view(), name='sample2'),
]