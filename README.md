# web-meteo
Тестовое задание: Веб-приложение для прогноза погоды.

## Выполненные задачи:
- Написан полностью рабочий backend, который позволит frontend-разработчикам реализовать отображение прогноза погоды.
- Проект упакован в Docker контейнер.
- Реализовано API для получения данных об истории поиска и статистики поиска по городу.

## Использованные технологии:
- Django==5.0.7
- djangorestframework==3.15.2
- requests==2.32.3
- docker==27.0.3
- docker-compose==v2.17.3

## Как запустить:
1. Клонировать репозиторий.
2. Перейти в папку с проектом.
3. Создать в папке с проектом файл .meteorc по образцу meteorc и заполнить все пустые переменные.
4. Выполнить скрипт start.sh с флагами -d -f -r -b --migrate --createsuperuser.
5. Доступ к API по следующим адресам:
    - http://0.0.0.0:8000/api/v1/start_weather/
    - http://0.0.0.0:8000/api/v1/request_weather/
    - http://0.0.0.0:8000/api/v1/towns_statistic/
