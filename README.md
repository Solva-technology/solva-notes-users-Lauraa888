# Note App (Django + Docker)

Учебное Django-приложение для работы с заметками с поддержкой пользователей, авторизации и разграничения прав доступа.

## Возможности

- Регистрация пользователя
- Авторизация и выход
- Восстановление пароля (стандартные Django views)
- Создание, просмотр, редактирование и удаление заметок
- Ограничение прав:
  - редактировать и удалять заметку может только автор или администратор
- Раздел «Мои заметки» (заметки текущего пользователя)
- Запуск проекта в Docker с PostgreSQL

---

## Технологии

- Python 3.10
- Django 5.0
- PostgreSQL
- Docker / Docker Compose

---

## Установка и запуск

```bash
git clone <https://github.com/Solva-technology/solva-notes-users-Lauraa888.git>
cd solva-notes-users-Lauraa888
docker compose up --build
Приложение доступно по адресу:
http://localhost:8000/

Основные URL
Заметки
Главная (все заметки):
http://localhost:8000/

Создание заметки (только для авторизованных):
http://localhost:8000/notes/create/

Просмотр заметки:
http://localhost:8000/notes/<id>/

Пользователи
Регистрация:
http://localhost:8000/auth/register/

Вход:
http://localhost:8000/auth/login/

Выход:
http://localhost:8000/auth/logout/

Мои заметки (только для авторизованных):
http://localhost:8000/my/

Восстановление пароля
http://localhost:8000/auth/password_reset/

http://localhost:8000/auth/password_reset/done/

http://localhost:8000/auth/reset/<uidb64>/<token>/

http://localhost:8000/auth/reset/done/

Ограничение доступа
Создавать заметки могут только авторизованные пользователи

Редактировать и удалять заметку может только автор или администратор

