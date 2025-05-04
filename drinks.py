import json
import random
import os

# Загружаем drinks.json
BASE_PATH = os.path.dirname(__file__)
JSON_PATH = os.path.join(BASE_PATH, "drinks.json")

with open(JSON_PATH, "r", encoding="utf-8") as f:
    DRINKS = json.load(f)


def get_info(name: str) -> str:
    key = name.lower()
    if key in DRINKS:
        return DRINKS[key]["info"]
    return f"Напиток '{name}' не найден."


def get_recipe(name: str) -> str:
    key = name.lower()
    if key in DRINKS:
        return DRINKS[key]["recipe"]
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
    names = sorted([name.title() for name in DRINKS.keys()])
    return "Доступные напитки:\n" + "\n".join(names)