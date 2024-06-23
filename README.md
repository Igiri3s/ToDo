Instrukcja odpalenia aplikacji:
1) Na początku należy zainstalować wymagane biliboteki uzywając komendy:


pip install -r requirements.txt
2) Następnie trzeba ustawić dane swojego serwera PostgeSQL w pliku settings.py
w moim przypadku jest to:

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'projektMGA',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

3) Następnie należy utworzyć migracje uzywając py manage.py migrate
4) Na tym etapie warto stworzyć super usera komendą python manage.py createsuperuser, tylko on ma możliwośc usuwania Tasków
5) Można teraz uruchomić serwer komendą python manage.py runserver

Uwagi:
1) Każdy endpoint wymaga abyśmy byli zalogowani, najprościej to zrobic logująć sie odrazu na super usera utworzonego przed chwilą
2) W pliku Zadanie MGA.postman_collection znajduje sie kolekcja Postmana z dostępnymi endpointami prostymi opisami oraz  przykładowymi danymi których mozemy uzyć