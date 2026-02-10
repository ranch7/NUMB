import re

def evaluate_expression(expr: str):
    expr = expr.lower().replace("от", "of").replace(",", ".").replace(" ", "")

    percent_matches = re.findall(r"(\d+(?:\.\d+)?)%of(\d+(?:\.\d+)?)", expr)
    for percent, number in percent_matches:
        result = (float(percent) / 100) * float(number)
        expr = expr.replace(f"{percent}%of{number}", str(result))

    expr = re.sub(r'(?<=[\d\)])(\d+(?:\.\d+)?)%', r'*\1/100', expr)

    expr = re.sub(r'^(\d+(?:\.\d+)?)%', r'(\1/100)', expr)

    if not re.fullmatch(r"[0-9\.\+\-\*/\(\)]+", expr):
        return "Ошибка: недопустимое выражение."

    try:
        result = eval(expr)
        return round(result, 4)
    except Exception as e:
        return f"Ошибка вычисления: {e}"

# Основной цикл
print("Калькулятор NUMB. Введите выражение")
while True:
    user_input = input("Введите выражение: ")
    if user_input.lower() in ['выход', 'exit', 'quit']:
        print("Выход из калькулятора.")
        break
    output = evaluate_expression(user_input)
    print("Результат:", output)
