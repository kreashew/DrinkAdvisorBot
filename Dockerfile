# Используем официальный slim-образ Python
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем все файлы проекта
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Переменная окружения (можно переопределить при запуске)
ENV TELEGRAM_TOKEN=""

# Стартовая команда
CMD ["python", "bot/main.py"]
