import pytest

from main import BooksCollector


class TestBooksCollector:
    # 1. Добавляем две книги -------------------------------------------------------------------------------------------
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # 2. Название книги может содержать максимум 40 символов или без названия ------------------------------------------
    @pytest.mark.parametrize('name', ['', 'Жизнь, необыкновенные и удивительные приключения Робинзона Крузо'])
    def test_add_new_book_can_more_40symbols(self, collector, name):
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    # 3. Одну и ту же книгу можно добавить только один раз -------------------------------------------------------------
    def test_add_new_book_cant_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    # 4. Устанавливает жанр книги --------------------------------------------------------------------------------------
    def test_set_book_genre_set_genre(self, collector):
        collector.books_genre = {'Гордость и предубеждение и зомби': ''}
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.books_genre.get('Гордость и предубеждение и зомби') == 'Ужасы'

    # 5. Жанр у книги не устанавливается, если ее нет в book_genre -----------------------------------------------------
    def test_set_book_genre_cant_get_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Роман')
        assert collector.get_book_genre('Роман') is None

    # 6. Выводит жанр книги по её имени --------------------------------------------------------------------------------
    def test_get_book_genre_get_book_name(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    # 7. Выводит список книг с определённым жанром ---------------------------------------------------------------------
    def test_get_books_with_specific_genre(self, collector):
        collector.books_genre = {'Гарри Поттер и кубок огня': 'Фантастика', 'Трое в лодке': 'Комедии',
                                 'Дюна': 'Фантастика'}
        assert len(collector.get_books_with_specific_genre('Фантастика')) == 2

    # 8. Выводит текущий словарь ---------------------------------------------------------------------------------------
    def test_get_books_genre_books_genre(self, collector):
        books_genre = {'Гарри Поттер и кубок огня': 'Фантастика', 'Трое в лодке': 'Комедии',
                       'Что делать, если ваш кот хочет вас убить': 'Детективы',
                       'Дядя Федор, пес и кот': 'Мультфильмы',
                       'Гордость и предубеждение и зомби': 'Ужасы'}
        for name, genre in books_genre.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        assert collector.get_books_genre() == books_genre

    # 9. Возвращает книги, которые подходят детям ----------------------------------------------------------------------
    def test_get_books_for_children(self, collector):
        books_genre = {'Гордость и предубеждение и зомби': 'Ужасы',
                       'Что делать, если ваш кот хочет вас убить': 'Детективы',
                       'Дядя Федор, пес и кот': 'Мультфильмы'}
        for name, genre in books_genre.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        assert collector.get_books_for_children() == ['Дядя Федор, пес и кот']

    # 10. Добавляет книгу в избранное ----------------------------------------------------------------------------------
    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Дядя Федор, пес и кот')
        collector.add_book_in_favorites('Дядя Федор, пес и кот')
        assert len(collector.get_list_of_favorites_books()) == 1

    # 11. Повторно добавить книгу в избранное нельзя -------------------------------------------------------------------
    def test_add_book_in_favorites_cant_same_book_in_favorites(self, collector):
        collector.add_new_book('Дядя Федор, пес и кот')
        collector.add_book_in_favorites('Дядя Федор, пес и кот')
        collector.add_book_in_favorites('Дядя Федор, пес и кот')
        assert len(collector.get_list_of_favorites_books()) != 2

    # 12. Удаляет книгу из избранного, если она там есть ---------------------------------------------------------------
    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Дядя Федор, пес и кот')
        collector.add_book_in_favorites('Дядя Федор, пес и кот')
        collector.delete_book_from_favorites('Дядя Федор, пес и кот')
        assert len(collector.get_list_of_favorites_books()) == 0

    # 13. Получает список избранных книг -------------------------------------------------------------------------------
    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Дядя Федор, пес и кот')
        collector.add_book_in_favorites('Дядя Федор, пес и кот')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert collector.get_list_of_favorites_books() == ['Дядя Федор, пес и кот']
