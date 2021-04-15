from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="catalog-home"),
    path('books/', views.BookListView.as_view(), name="catalog-books"), #-> class based view
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]
