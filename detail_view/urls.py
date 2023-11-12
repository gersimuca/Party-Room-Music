from django.urls import path
from .views import IndexView, BookDetailView

app_name = 'dv-books'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('<slug:slug>/', BookDetailView.as_view(), name='book-detail'),
]