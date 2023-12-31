# ToDoer

### Описание:

**ToDoer** - это простое приложение для управления задачами. Пользователи могут зарегистрироваться, создавать задачи,
устанавливать им сроки выполнения, отмечать как выполненные и удалять.

### Основные функции:

1. ✅ Регистрация и аутентификация пользователей: Пользователи могут создавать аккаунты и входить в систему.
2. ✅ Создание, просмотр, редактирование и удаление задач: Задачи могут содержать название, описание, срок выполнения и
   статус (выполнена/не выполнена).
3. ✅ Фильтрация и сортировка задач: Пользователи могут фильтровать задачи по различным критериям (например, по статусу
   выполнения или сроку выполнения).
4. Уведомления о задачах: Оповещения о приближающемся сроке выполнения задачи.
5. ✅ Аутентификация через API токен: Позволяет пользователям использовать API для взаимодействия с приложением.
6. ✅ Административная панель: Доступ к административной панели Django для управления пользователями и задачами.
7. ✅ Документация API: Используя Django Rest Framework's built-in поддержку Swagger или Redoc, предоставьте понятную
   документацию для API.
8. ✅ Тесты: Напишите автоматические тесты для проверки функционала приложения.

## Как подключить проект?
1. Клонируем репозиторий - `git clone git@github.com:lowfie/ToDoer.git`
2. Заполняем `.env` и `config.yaml` файлы (примеры файлов в проекте)
3. Переходим в директорию с проектом и пишем команду `sudo make up`

## Make команды  
`up` - билд и запуск проекта в докер контейнере  
`down` - остановка и удаления контейнера  
`logs`- последние 1000 логов в *web* контейнере  
`migrations` - создание файлов миграции в Django ORM   
`migrate` - миграция в базу данных  
`createadmin` - создание админ-пользователя  

---------  
### Запуск модульных тестов
Также вы можете использовать команды тестирования модулей  
`test_users` - users модуль  
`test_tasks` - tasks модуль   

---------  

## Технологии
 - Django, drf
 - Marshmello
 - Swagger (drf-yasg)
 - Poetry
 - Docker, Docker-compose
 - Makefile
 - Git
 - gunicorn
