# InfectionPrevention

```git clone https://github.com/lleviy/InfectionPrevention.git```

Создать виртуальное окружение в папке с проектом: ```python -m venv venv```

Активировать его: ```venv\Scripts\activate```

```
pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

```

GET /api/districts/ - все районы
GET /api/districts/?district=66 - информация о районе с id=66 

POST api/accounts/auth/users/?email=example@example.com&username=example&password=example - регистрация
POST api/accounts/auth/token/login/?username=example&password=example - авторизация
GET api/accounts/auth/token/logout/ - выход (только с токеном)
GET, PUT api/accounts/profile - профиль пользователя (только с токеном)
