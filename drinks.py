import json
import random
import os

# Загружаем drinks.json
BASE_PATH = os.path.dirname(__file__)
JSON_PATH = os.path.join(BASE_PATH, "drinks.json")

with open(JSON_PATH, "r", encoding="utf-8") as f:
    DRINKS = json.load(f)


def normalize_name(name: str) -> str:
    """Нормализует название: убирает скобки, лишние пробелы и приводит к нижнему регистру"""
    return name.strip().lower().replace("<", "").replace(">", "").replace("«", "").replace("»", "")

def get_info(name: str) -> str:
    key = normalize_name(name)
    for drink in DRINKS:
        if normalize_name(drink) == key:
            return DRINKS[drink]["info"]
    return f"Информация для '{name}' не найдена."

def get_recipe(name: str) -> str:
    key = normalize_name(name)
    for drink in DRINKS:
        if normalize_name(drink) == key:
            return DRINKS[drink]["recipe"]
    return f"Рецепт для '{name}' не найден."


def get_by_ingredient(ingredient: str) -> str:
    ingredient = ingredient.lower()
    results = []
    for name, data in DRINKS.items():
        if ingredient in data["recipe"].lower():
            results.append(name.title())
    if results:
        return "Коктейли с этим ингредиентом:\n" + "\n".join(results)
    return f"Не найдено коктейлей с ингредиентом '{ingredient}'."


def get_random() -> str:
    name = random.choice(list(DRINKS.keys()))
    return f"{name.title()} — {DRINKS[name]['info']}"

def get_all_drinks() -> str:
    drink_list = sorted([name for name in DRINKS.keys()])
    lines = ["📋 Доступные напитки:\n"]
    for name in drink_list:
        emoji = "🍹" if "коктейль" in name.lower() else (
            "🍵" if "чай" in name.lower() else (
                "🍋" if "лимонад" in name.lower() or "цитрусовый" in name.lower() else (
                    "🥤" if "напиток" in name.lower() or "смузи" in name.lower() else "🧊"
                )
            )
        )
        lines.append(f"{emoji} {name}")
    return "\n".join(lines)
