from django.test import TestCase
from book.models import Book,GENRE_CHOICES,LANGUAGE_CHOICES
# Create your tests here.
GENRE_MAP = { 'CS':'0','Non-CS':'1','Common':'2'}
LANGUAGE_MAP = { 'English':'0','Hindi':'1','German':'2','English(U.S.)':'3','English(India)':'4'}

def genre_pair(genre):
    return GENRE_MAP[genre]

def language_pair(language):
    return LANGUAGE_MAP[language]

class BookTestCase(TestCase):
    def setUp(self):
        Book.objects.create(name='Test1',author='Ashu',genre=genre_pair("CS"),language=language_pair('Hindi'))
    
    def test_book_test(self):
        obj2 = Book.objects.create(name='Test2',author='Ashu',genre=genre_pair("CS"),language=language_pair('Hindi'))
        self.assertEqual(obj2.name,'Test2')
        self.assertEqual(obj2.author,'Ashu')
        self.assertEqual(GENRE_CHOICES[int(obj2.genre)][1],'CS')
        self.assertEqual(LANGUAGE_CHOICES[int(obj2.language)][1],'Hindi')

    def create_book(self,name='Test',author='Ashutosh',genre=genre_pair("CS"),language=language_pair('Hindi')):
        return Book.objects.create(name=name,author=author,genre=genre,language=language)

    def test_book_qs(self):
        name = 'ReadingRoots'
        author1 = 'Xyz'
        author2 = 'Abc'
        object1=self.create_book(name=name)
        object2=self.create_book(name=name,author=author1)
        object3=self.create_book(name=name,author=author2)
        qs =  Book.objects.filter(name=name)
        self.assertAlmostEqual(qs.count(),3)










# Book.objects.create(name='Test1',author='Ashu',genre='Common',language='Hindi')
# obj1 = Book.objects.get(name='Test1',author='Ashu',genre='Common',language='Hindi')
# self.assertEqual(obj2.get_genre_display(),'CS')