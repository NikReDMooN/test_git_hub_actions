# образ с Pythin
FROM python:latest

# рабочая директория
WORKDIR /app

# копируем наш код внутрь контейнера
COPY app.py .

# Запуск при старте контейнера
CMD ["python", "app.py"]