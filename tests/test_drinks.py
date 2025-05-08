import unittest

# from drinks import get_info, get_recipe, search_drinks

# Для демонстрации — мок-данные и функции:
DRINKS = {
    "Мохито": {
        "info": "Классический безалкогольный мохито с лаймом и мятой.",
        "recipe": "Ингредиенты:\n- лайм, мята, лёд, спрайт"
    },
    "Чай с лимоном": {
        "info": "Освежающий чай с лимоном и мёдом.",
        "recipe": "Ингредиенты:\n- чёрный чай, лимон, мёд"
    }
}

def normalize_name(name: str) -> str:
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

def search_drinks(keyword: str) -> str:
    keyword = keyword.strip().lower()
    results = []
    for name, content in DRINKS.items():
        if keyword in name.lower() or keyword in content["info"].lower() or keyword in content["recipe"].lower():
            results.append(f"🔎 {name}")
    if results:
        return "Найдено:\n" + "\n".join(results)
    return f"❌ Ничего не найдено по запросу: '{keyword}'"


class TestDrinkFunctions(unittest.TestCase):

    def test_get_info_exact(self):
        self.assertIn("мохито", get_info("мохито").lower())

    def test_get_info_with_symbols(self):
        self.assertIn("мохито", get_info("<Мохито>").lower())

    def test_get_recipe_case_insensitive(self):
        self.assertIn("лайм", get_recipe("МОХИТО").lower())

    def test_get_recipe_not_found(self):
        self.assertIn("не найден", get_recipe("Неизвестный напиток"))

    def test_search_by_name(self):
        self.assertIn("Мохито", search_drinks("мохито"))

    def test_search_by_ingredient(self):
        self.assertIn("Чай с лимоном", search_drinks("лимон"))

    def test_search_nothing(self):
        self.assertIn("не найдено", search_drinks("манго"))


if __name__ == "__main__":
    unittest.main()
