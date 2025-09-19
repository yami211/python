# Базовий образ Linux з Python 
FROM python:3.10-slim

# Створюємо папку в корні контейнера
RUN mkdir /Skrypnyk

# Встановлюємо потрібну версію googletrans
RUN pip install googletrans==3.1.0a0


# Копіюємо програму у створену папку
COPY lab2_2.py /Skrypnyk/lab2_2.py

# Встановлюємо робочу директорію
WORKDIR /Skrypnyk

# Команда за замовчуванням для запуску контейнера
CMD ["python", "lab2_2.py"]
