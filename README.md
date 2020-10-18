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

```
На вход был получен большой объем данных. Из-за нехватки мощности пришлось отделять небольшой датасет для обучения. Это было сделано с помощью функции фильтрующей и чистящей данные. Для получения геометок было создано подключения по API к Яндекс Картам, также были получены геометки по адресам заболевших граждан из excel файла.
По полученным данным были обучены две модели. Первая предсказывает количество человек на территории сектора, находящихся там продолжительное время, работающих и проживающих. А вторая, обученная на исторических данных, предсказывает количество заболевших исходя из данных, полученных в первой модели.
Для создания рассылок был найден канал, по которому можно делать email рассылки, после выбора нужного порта, были перекодированы сообщения (изначально отправлялись только на английском) и настроена фильтрация, чтоб не отправлялись в спам. SMS рассылка была подключена через API, для Телеграмм бота был настроен интуитивно понятный пользователю функционал, и настроена интеграция данных с основного сайта.
Сайт был написан на JavaScript, через Яндекс API была настроена карта, анимированная визуализация, подключение к модели обучения, настройка фильтрации по запросу пользователю,  считывание геоданных всех районов Москвы и нанесение их на карту. 
Были использованы библиотеки: pandas, sklearn.model_selection, warnings, statsmodels, datetime, Smtplib, email, mainsms, pytelegrambotapi, numpy, pandas, matplotlib, os, pickle
```
```
https://drive.google.com/drive/folders/1stouXjuR1PI647pi5EIyN24npcQjQCRC?usp=sharing
```
