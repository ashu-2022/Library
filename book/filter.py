import django_filters
from book.models import Book
from django_filters import CharFilter

class BookFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    author = CharFilter(field_name='author', lookup_expr='icontains')
    genre = CharFilter(field_name='genre', lookup_expr='icontains')
    language = CharFilter(field_name='language', lookup_expr='icontains')

    class Meta:
        model = Book
        # fields = '__all__'
        # exclude =['image','desc','date_posted']

        fields = ['name', 'author','genre','language']
    
        # fields = {
        #     'name':['icontains'],
        #     'author':['icontains'],
        #     'genre':['icontains'],
        #     'language':['icontains'],
        # }
