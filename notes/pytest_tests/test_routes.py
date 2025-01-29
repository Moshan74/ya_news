# test_routes.py
from http import HTTPStatus

from django.urls import reverse


# test_routes.py
@pytest.mark.parametrize(
    'name',  # Имя параметра функции.
    # Значения, которые будут передаваться в name.
    ('notes:home', 'users:login', 'users:logout', 'users:signup')
)
# Указываем имя изменяемого параметра в сигнатуре теста.
def test_pages_availability_for_anonymous_user(client, name):
    url = reverse(name)  # Получаем ссылку на нужный адрес.
    response = client.get(url)  # Выполняем запрос.
    assert response.status_code == HTTPStatus.OK


"""
Тестирование доступности страниц для авторизованного пользователя
Теперь проверим доступность страницы со списком заметок, страницы добавления новой записи и страницы успешного добавления записей. Для этих проверок сами заметки не нужны: важно проверить лишь доступность страниц.
В этом тесте можно было бы применить фикстуру admin_client — клиент, залогиненный с пользователем admin. 
"""
@pytest.mark.parametrize(
    'name',
    ('notes:list', 'notes:add', 'notes:success')
)
def test_pages_availability_for_auth_user(not_author_client, name):
    url = reverse(name)
    response = not_author_client.get(url)
    assert response.status_code == HTTPStatus.OK 


# Параметризуем тестирующую функцию:
@pytest.mark.parametrize(
    'name',
    ('notes:detail', 'notes:edit', 'notes:delete'),
)
def test_pages_availability_for_author(author_client, name, note):
    url = reverse(name, args=(note.slug,))
    response = author_client.get(url)
    assert response.status_code == HTTPStatus.OK 