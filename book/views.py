from django.shortcuts import render
from book.models import Book
from django.views.generic import ListView,DetailView,CreateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from book.filter import BookFilter
from django_filters.views import FilterView

# Create your views here.

class BookListView(ListView):
    model=Book
    template_name='book/home.html'
    context_object_name='books'
    ordering=['-date_posted']
    paginate_by=5
   
    filter = BookFilter()
    def get_context_data(self,  **kwargs):
        context= super().get_context_data(**kwargs)
        context['filter'] = BookFilter(self.request.GET, queryset=self.get_queryset())
        return context

class BookCreateView(LoginRequiredMixin,CreateView):
    model=Book
    fields=['name','author','desc','genre','language','image']

    def form_valid(self, form):
        return super().form_valid(form)

class BookDetailView(DetailView):
    model = Book
    
