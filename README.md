#Сервис BTC

# Запуск

```bash 
sudo docker-compose build
sudo docker-compose run web python manage.py migrate
sudo docker-compose up -d
```
URL API
GET /api/ - Get last records
POST /api/update_btc - Manual update BTC info
