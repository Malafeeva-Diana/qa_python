# Проектная работа Sprint_4
 __Для покрытия тестами приложения BooksCollector были использованы методы:__


<details> <summary> add_new_book - добавляет новую книгу в словарь без указания жанра. Название книги может содержать максимум 40 символов. Одну и ту же книгу можно добавить только один раз. </summary>


    1. Добавляем две книги
        def test_add_new_book_add_two_books
        
    2. Название книги может содержать максимум 40 символов или без названия
        def test_add_new_book_can_more_40symbols
        
    3. Одну и ту же книгу можно добавить только один раз
        def test_add_new_book_cant_add_two_books
</details>

<details> <summary> set_book_genre — устанавливает жанр книги, если книга есть в books_genre и её жанр входит в список genre. </summary>

    4. Устанавливает жанр книги
        def test_set_book_genre_set_genre
    
    5. Жанр у книги не устанавливается, если ее нет в book_genre
        def test_set_book_genre_cant_get_genre
</details>

<details> <summary> get_book_genre — выводит жанр книги по её имени. </summary>

    6. Выводит жанр книги по её имени
        def test_get_book_genre_get_book_name
</details>

<details> <summary> get_books_with_specific_genre — выводит список книг с определённым жанром. </summary>

    7. Выводит список книг с определённым жанром
       def test_get_books_with_specific_genre
</details>

<details> <summary> get_books_genre — выводит текущий словарь books_genre. </summary>

    8. Выводит текущий словарь
       def test_get_books_genre_books_genre
</details>

<details> <summary> get_books_for_children — возвращает книги, которые подходят детям. У жанра книги не должно быть возрастного рейтинга. </summary>

    9. Возвращает книги, которые подходят детям
        def test_get_books_for_children
</details>

<details> <summary> add_book_in_favorites — добавляет книгу в избранное. Книга должна находиться в словаре books_genre. Повторно добавить книгу в избранное нельзя. </summary>

    10. Добавляет книгу в избранное
        def test_add_book_in_favorites

    11. Повторно добавить книгу в избранное нельзя
        def test_add_book_in_favorites_cant_same_book_in_favorites
</details>


<details> <summary> delete_book_from_favorites  — удаляет книгу из избранного, если она там есть. </summary>

    12. Удаляет книгу из избранного, если она там есть
        def test_delete_book_from_favorites
</details>

<details> <summary> get_list_of_favorites_books — получает список избранных книг. </summary>

    13. Получает список избранных книг
        def test_get_list_of_favorites_books
</details>