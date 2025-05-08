import json
import random
import os

BASE_PATH = os.path.dirname(__file__)
JSON_PATH = os.path.join(BASE_PATH, "drinks.json")

with open(JSON_PATH, "r", encoding="utf-8") as f:
    DRINKS = json.load(f)


def normalize_name(name: str) -> str:
    return name.strip().lower().replace("<", "").replace(">", "").replace("«", "").replace("»", "")


def get_emoji(name: str) -> str:
    lname = name.lower()
    if "чай" in lname:
        return "🍵"
    elif "коктейль" in lname:
        return "🍹"
    elif "смузи" in lname:
        return "🥤"
    elif "лимонад" in lname or "цитрусовый" in lname:
        return "🍋"
    elif "напиток" in lname or "компот" in lname:
        return "🧃"
    elif "молоко" in lname or "молочный" in lname:
        return "🥛"
    else:
        return "🧊"


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
    keyword = ingredient.lower()
    results = []
    for name, data in DRINKS.items():
        recipe_text = data.get("recipe", "").lower()
        if keyword in recipe_text:
            emoji = get_emoji(name)
            results.append(f"{emoji} {name}")
    if results:
        return "Напитки с этим ингредиентом:\n" + "\n".join(results)
    return f"Не найдено напитков с ингредиентом '{ingredient}'."


def get_random() -> str:
    name = random.choice(list(DRINKS.keys()))
    return f"{get_emoji(name)} {name} — {DRINKS[name]['info']}"


def get_all_drinks() -> str:
    drink_list = sorted(DRINKS.keys())
    lines = ["📋 Доступные напитки:\n"]
    for name in drink_list:
        emoji = get_emoji(name)
        lines.append(f"{emoji} {name}")
    return "\n".join(lines)
