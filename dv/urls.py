from django.urls import path
from .views import IndexView

app_name = 'books'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('<slug:slug>/', BookDetailView.as_view(), name='book-detail'),
]

