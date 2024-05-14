# Проектная работа Sprint_4

Для покрытия тестами приложения BooksCollector были использованы методы:

1. add_new_book_ — добавляет новую книгу в словарь без указания жанра. Название книги может содержать максимум 40 символов. Одну и ту же книгу можно добавить только один раз.
2. set_book_genre  — устанавливает жанр книги, если книга есть в books_genre и её жанр входит в список genre.
3. get_book_genre_ — выводит жанр книги по её имени.
4. get_books_with_specific_genre_ — выводит список книг с определённым жанром.
5. get_books_genre_ — выводит текущий словарь books_genre.
6. get_books_for_children_ — возвращает книги, которые подходят детям. У жанра книги не должно быть возрастного рейтинга.
7. add_book_in_favorites_ — добавляет книгу в избранное. Книга должна находиться в словаре books_genre. Повторно добавить книгу в избранное нельзя.
8. delete_book_from_favorites_ — удаляет книгу из избранного, если она там есть.
9. get_list_of_favorites_books_ — получает список избранных книг.


1. Добавляем две книги

    def test_add_new_book_add_two_books(self):

2. Название книги может содержать максимум 40 символов или без названия

    def test_add_new_book_can_more_40symbols

3. Одну и ту же книгу можно добавить только один раз

    def test_add_new_book_cant_add_two_books

4. Устанавливает жанр книги

    def test_set_book_genre_set_genre

5. Жанр у книги не устанавливается, если ее нет в book_genre

    def test_set_book_genre_cant_get_genre

6. Выводит жанр книги по её имени

    def test_get_book_genre_get_book_name

7. Выводит список книг с определённым жанром

    def test_get_books_with_specific_genre

8. Выводит текущий словарь

    def test_get_books_genre_books_genre

9. Возвращает книги, которые подходят детям

    def test_get_books_for_children

10. Добавляет книгу в избранное

    def test_add_book_in_favorites

11. Повторно добавить книгу в избранное нельзя

    def test_add_book_in_favorites_cant_same_book_in_favorites

12. Удаляет книгу из избранного, если она там есть

    def test_delete_book_from_favorites

13. Получает список избранных книг

    def test_get_list_of_favorites_books
