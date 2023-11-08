from django.urls import path
from django.views.generic import TemplateView
from template_view.views import Sample2View

app_name = 'website'

urlpatterns = [
    # extra_context Attribute from ContentMixin - keyword argument for as_view()
    path('sample1', TemplateView.as_view(template_name="template_view/sample1.html",
                                         extra_context={'title': 'Custom Title'})),
    path('sample2', Sample2View.as_view(), name='sample2'),
]
