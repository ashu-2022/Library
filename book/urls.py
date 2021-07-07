from django.urls import path
from .views import (BookListView,BookCreateView)#BookDetailView
urlpatterns = [
    path('', BookListView.as_view(),name='book-home'),
    # path('book/<int:pk>/', BookDetailView.as_view(),name='book-detail'),
    path('book/new/', BookCreateView.as_view(),name='book-create'),

]
