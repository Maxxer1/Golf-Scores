# Golf Scores

## Uruchomienie

### Wersja produkcyjna

`docker-compose up -d mysql`  
`docker-compose up -d server`

### Development

1. Klonujemy repozytorium
2. Tworzymy python virtual enviroment  
   `python -m venv venv`
3. Aktywujemy venv  
   `source venv/bin/activate`
4. Instalujemy zaleznosci  
   `pip install -r requirements.txt`

Uruchamiamy baze danych MySQL  
`docker-compose up -d mysql`

Migracje bazy danych  
`python manage.py migrate`

Załadowanie testowych danych  
`db_fixtures.json` - plik z testowymi danymi gotowymi do załadowania  
`python manage.py loaddata db_fixtures.json`  

Uruchomienie serwera  
`python manage.py runserver 0.0.0.0:8000`

Panel administratora do bazy danych
`http://localhost:8000/admin`
Login: `admin`
Hasło: `adminadmin`