import re

with open("drinks.json", "r", encoding="utf-8") as f:
    content = f.read()

# Заменяем все одиночные \, не перед которыми n, t, r и т.п.
fixed_content = re.sub(r'\\(?![ntr"\\/bfu])', r'\\\\', content)

with open("drinks_fixed.json", "w", encoding="utf-8") as f:
    f.write(fixed_content)

print("✅ Файл исправлен и сохранён как drinks_fixed.json")
