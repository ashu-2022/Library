import django_filters
from book.models import Book
from django_filters import CharFilter,ChoiceFilter,MultipleChoiceFilter
from book.models import GENRE_CHOICES,LANGUAGE_CHOICES

class BookFilter(django_filters.FilterSet):
    name = CharFilter(label='Book Name',field_name='name', lookup_expr='icontains')
    author = CharFilter(label='Author Name',field_name='author', lookup_expr='icontains')
    genre = MultipleChoiceFilter(choices=GENRE_CHOICES)
    language = MultipleChoiceFilter(choices=LANGUAGE_CHOICES)
    class Meta:
        model = Book
        fields = ['name', 'author','genre','language']
        

        
 
# LANGUAGE_CHOICES = (
#     (0, 'English'),
#     (1, 'Hindi'),
#     (2, 'German'),
#     (3, 'English(U.S.)'),
#     (4, 'English(India)'),
# )

# GENRE_CHOICES = (
#     (0, 'CS'),
#     (1, 'Non-CS'),
#     (2, 'Common'),
# )

    # genre = ChoiceFilter
    # genre = ChoiceFilter(label='Select Genre',choices=STATUS_CHOICES)
    # genre = MultipleChoiceFilter(choices=STATUS_CHOICES,conjoined=True)
    # status = ChoiceFilter(choices=STATUS)
    # status = MultipleChoiceFilter(choices=STATUS)


    # stores as key:value pairs



        # fields = '__all__'
        # exclude =['image','desc','date_posted']

        # fields = {
        #     'name':['icontains'],
        #     'author':['icontains'],
        #     'genre':['icontains'],
        #     'language':['icontains'],
        # }
