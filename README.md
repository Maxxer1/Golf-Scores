# Golf Scores


![Main screen](https://i.ibb.co/Lnr5HZ4/Screenshot-from-2019-07-15-08-30-52.png)

![Golf courses](https://i.ibb.co/x7MB06R/Screenshot-from-2019-07-15-08-31-15.png)

![Golf scores](https://i.ibb.co/R3DtZ1F/Screenshot-from-2019-07-15-08-31-24.png)

## Launching

### Production

`docker-compose up -d`  

### Development

1. Clone repo
2. Create python virtual environment  
   `python -m venv venv`
3. Activate venv  
   `source venv/bin/activate`
4. Install dependencies  
   `pip install -r requirements.txt`

Run MySQL 
`docker-compose up -d mysql`

DB migrations  
`python manage.py migrate`

Load test data  
`db_fixtures.json` - database fixtures 
`python manage.py loaddata db_fixtures.json`  

Launch server  
`python manage.py runserver 0.0.0.0:8000`