FROM python:3.13.7-slim

WORKDIR /app

COPY ["app.py", ""]

CMD ["python", "app.py"]
