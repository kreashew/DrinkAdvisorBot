import json
import os
import sys

# Убедимся, что текущая папка в пути, чтобы импортировать db.py
sys.path.append(os.path.dirname(__file__))

import db  # наш модуль для работы с SQLite

def main():
    # 1) Инициализируем БД (таблица создаётся, если не существует)
    db.init_db()

    # 2) Загружаем JSON
    with open("drinks.json", encoding="utf-8") as f:
        drinks = json.load(f)

    # 3) Пишем каждый напиток в базу
    for name, data in drinks.items():
        db.add_drink(name, data["info"], data["recipe"])

    print(f"✅ Загружено напитков: {len(drinks)}")

if __name__ == "__main__":
    main()
