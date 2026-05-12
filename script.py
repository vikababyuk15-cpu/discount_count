import pandas as pd
import re

print("Загрузка файлов...")

# =========================
# Читаем файлы
# =========================

source_df = pd.read_excel("source.xlsx")
needed_df = pd.read_excel("needed.xlsx")

# =========================
# Функция очистки текста
# =========================

def clean_text(text):

    text = str(text).lower().strip()

    # заменяем спецсимволы пробелами
    text = re.sub(r'[:;,_\-\.\(\)]', ' ', text)

    # убираем лишние пробелы
    text = re.sub(r'\s+', ' ', text)

    return text.strip()

# =========================
# Очищаем данные
# =========================

source_df["clean_game"] = source_df["Game"].apply(clean_text)
needed_df["clean_game"] = needed_df["Game"].apply(clean_text)

source_df["clean_provider"] = source_df["Provider"].apply(clean_text)
needed_df["clean_provider"] = needed_df["Provider"].apply(clean_text)

# =========================
# Результаты
# =========================

result_rows = []

# =========================
# Основная логика
# =========================

for _, needed_row in needed_df.iterrows():

    needed_game = needed_row["clean_game"]
    needed_provider = needed_row["clean_provider"]

    # =========================
    # Ищем частичное совпадение игры
    # =========================

    game_matches = source_df[
        source_df["clean_game"].str.contains(needed_game, na=False)
    ]

    # Если ничего не нашли
    if len(game_matches) == 0:
        continue

    # Если только одно совпадение
    if len(game_matches) == 1:
        result_rows.append(game_matches.iloc[0])
        continue

    # =========================
    # Если дублей несколько —
    # уточняем по провайдеру
    # =========================

    provider_matches = game_matches[
        game_matches["clean_provider"] == needed_provider
    ]

    # Если нашли одно совпадение
    if len(provider_matches) == 1:
        result_rows.append(provider_matches.iloc[0])

    # Если всё ещё неоднозначно —
    # добавляем все варианты
    else:
        for _, row in game_matches.iterrows():
            result_rows.append(row)

# =========================
# Создаём итоговый файл
# =========================

if len(result_rows) > 0:

    result_df = pd.DataFrame(result_rows)

    # удаляем служебные колонки
    result_df = result_df.drop(
        columns=["clean_game", "clean_provider"],
        errors="ignore"
    )

    # убираем полные дубли
    result_df = result_df.drop_duplicates()

    # сохраняем
    result_df.to_excel("result.xlsx", index=False)

    print("Готово! Создан файл result.xlsx")

else:
    print("Совпадений не найдено.")