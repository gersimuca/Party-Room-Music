from django.urls import path
from .views import IndexView, BookDetailView, GenreView, AddBookView, BookEditView

app_name = 'uv-books'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('add/', AddBookView.as_view(), name='add'),
    path('g/<str:genre>/', GenreView.as_view(), name='genre'),
    path('<slug:slug>/', BookDetailView.as_view(), name='book-detail'),
    path('<slug:slug>/edit', BookEditView.as_view(), name='edit-detail'),
]
