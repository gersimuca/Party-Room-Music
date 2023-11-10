from django.urls import path
from django.views.generic import TemplateView, RedirectView
from template_view.views import Sample2View, PostPreLoadTaskView

app_name = 'website'

urlpatterns = [
    # extra_context Attribute from ContentMixin - keyword argument for as_view()
    path('sample1', TemplateView.as_view(template_name="template_view/sample1.html",
                                         extra_context={'title': 'Custom Title or Testing TemplateView'})),
    path('sample2', Sample2View.as_view(), name='sample2'),
    path('riderect', RedirectView.as_view(url = 'http://youtube.com/'), name = 'go-to-youtube'),
    path('sample3/<int:pk>/', PostPreLoadTaskView.as_view(), name = 'redirect-task'),
    # path('sample4/<int:pk>/', SinglePostView.as_view(), name = 'singlepost')
]
