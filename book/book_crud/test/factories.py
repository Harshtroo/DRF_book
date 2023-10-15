
from book_crud.models import Book,Author
import factory
from factory import Faker


class AuthorFactory(factory.django.DjangoModelFactory):
    name = Faker("author1")


class BookFactory(factory.django.DjangoModelFactory):
    # Author.objects.create(name="David Beazley")
    # Author.objects.create(name="Wes Mckinney")
    class Meta:
        model = Book

    name = Faker("Book1,Book2")
    author = factory.SubFactory(AuthorFactory)
    image = Faker([
                open("/home/ashishv/Djanog DRF bulk create/DRF_book/book/media/images/51j89lmxnpL._SX377_BO1204203200_.jpg","rb"),
                open("/home/ashishv/Djanog DRF bulk create/DRF_book/book/media/images/51j89lmxnpL._SX377_BO1204203200_.jpg","rb")
            ])

