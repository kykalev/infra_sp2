# Проект «Проект YaMDb»
## Описание
Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).
Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»).
Добавлять произведения, категории и жанры может только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.
Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.
Платформа полностью готова к работе и может быть быстро развернута как на внутренних корпоративных ресурсах так и в публичном облаке.

Доступ к платформе осуществляется через REST API

## Использованные технологии
В проекте использованы технологии:

>requests 2.26.0  
django 2.2.16  
djangorestframework 3.12.4  
PyJWT 2.1.0  
pytest 6.2.4  
pytest-django 4.4.0  
pytest-pythonpath 0.7.3  
django-filter 21.1  
djangorestframework-simplejwt 5.2.2  
gunicorn==20.0.4  
psycopg2-binary==2.8.6  
asgiref==3.2.10  
pytz==2020.1  
sqlparse==0.3.1  


## Установка
Клонировать репозиторий и перейти в него в командной строке:

```commandline
git clone git@github.com:kykalev/infra_sp2.git
```

```commandline
cd infra_sp2/infra
```

Запустите docker-compose командой :

```commandline
docker-compose up
```
Выполните по очереди команды:

```commandline
docker-compose exec web python manage.py makemigrations  
docker-compose exec web python manage.py migrate  
docker-compose exec web python manage.py createsuperuser  
docker-compose exec web python manage.py collectstatic --no-input  
```

## Теперь проект доступен по адресу http://localhost/admin/

## Импорт данных из csv

В директории `infra_sp2/api_yamdb/static/data`, подготовлены несколько файлов в формате `csv` с контентом для ресурсов
`Users, Titles, Categories, Genres, Reviews и Comments`.
После выполненых миграций перенести данные в базу данных можно командой
```commandline
python manage.py addcsv
```

## Шаблон наполнения env-файла, который находится в папке infra

```commandline
SECRET_KEY=your_secret_code # Секретный ключ установки Django
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql  
DB_NAME=postgres # имя базы данных  
POSTGRES_USER=postgres # логин для подключения к базе данных  
POSTGRES_PASSWORD=your_password # пароль для подключения к БД (установите свой)  
DB_HOST=db # название сервиса (контейнера)  
DB_PORT=5432 # порт для подключения к БД  
```


## Описание API

**Подробное описание API проекта доступно по адресу:** `http://localhost/redoc/`  
Или в формате **OpenAPI** в папке проекта:  
`infra_sp2/api_yamdb/static/redoc.yaml`  


### API версия 1 _(текущая)_

#### Доступные эндпоинты:

##### Регистрация пользователей и выдача токенов:

`/api/v1/auth/signup/` - Регистрация нового пользователя.  
`/api/v1/auth/token/` - Получение JWT-токена в обмен на username и confirmation code.  

Доступные методы:
- POST - Создание пользователя.  

##### Категории (типы) произведений:

`/api/v1/categories/` Управление категориями.

Доступные методы:

- GET - Получение списка всех категорий.
- POST - Добавление новой категории.
- DEL - Удаление категории по `{slug}`. 

##### Категории жанров:

`/api/v1/genres/` Управление жанрами.

Доступные методы:

- GET - Получение списка всех жанров.
- POST - Добавление нового жанра.
- DEL - Удаление жанра по `{slug}`.

##### Произведения, к которым пишут отзывы (определённый фильм, книга или песенка):

`/api/v1/titles/` Управление Произведениями.

Доступные методы:

- GET - Получение списка или одного произведения по `{titles_id}`.
- POST - Добавление произведения.
- PATH - Частичное обновление информации о произведении по `{titles_id}`.
- DEL - Удаление произведения по `{titles_id}`.

##### Отзывы:

`/api/v1/titles/{title_id}/reviews/` Управление Отзывами.

Доступные методы:

- GET - Получение списка или одного отзыва по `{review_id}`.
- POST - Добавление нового отзыва.
- PATH - Частичное обновление отзыва по `{review_id}`.
- DEL - Удаление отзыва по `{review_id}`.

##### Комментарии к отзывам:

`/api/v1/titles/{title_id}/reviews/` Управление комментариями.

Доступные методы:

- GET - Получение списка всех комментариев (или одного) к отзыву по `{comment_id}`.
- POST - Добавление комментария к отзыву.
- PATH - Частичное обновление комментария к отзыву по `{comment_id}`.
- DEL - Удаление комментария к отзыву по `{comment_id}`.

##### Пользователи:

`/api/v1/users/` Управление пользователями.  
`/api/v1/users/me/` Изменение данных своей учетной записи.

Доступные методы:

- GET - Получение списка всех пользователей. Или одного пользователя по `{username}`.
- POST - Добавление пользователя.
- PATH - Изменение данных пользователя по `{username}`.
- DEL - Удаление пользователя по `{username}`.

#### Права доступа и безопасность

Управление пользователями осуществляется через web интерфейс администратора:  

`http://localhost/admin/` 

#### Примеры запросов:

- Получить список всех категорий.  

```http request
GET http://localhost/api/v1/categories/
```

- Добавить жанр (Поле `slug` каждого жанра должно быть уникальным).  
 
```http request
POST http://localhost/api/v1/genres/
```
```
{
  "name": "string",
  "slug": "string"
}
```
--------------------------------------------------------------------------
## Авторы:

**Андрей Смирнов**   
**Сергей Барсуков**  
**Максим Кукалев**  
Студенты Яндекс Практикум 
