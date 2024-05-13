def process_row(row):
    un = row[0].split(';')[0]
    name = row[0].split(';')[1].split('/')[::-1]
    formatted_name = "/".join(name)
    status = "Выполнено" if row[1] == "Да" else "Не выполнено"
    second_word = un.split()[1]
    email = row[3].split('@')[0]
    return [formatted_name, status, second_word, email]


def main(input_table):
    seen_names = set()
    unique_rows = []
    for row in input_table:
        if all(row) and None not in row:
            name = row[0].split(';')[0]
            if name not in seen_names:
                unique_rows.append(process_row(row))
                seen_names.add(name)

    return unique_rows

# Пример использования
input_table = [
    ["Макар Каманов;00/01/24", "Да", "kamanov78@mail.ru", "kamanov78@mail.ru"],
    ["Макар Каманов;00/01/24", "Да", "kamanov78@mail.ru", "kamanov78@mail.ru"],
    ["Тихон Бидиди;02/01/19", "Да", "bididi88@gmail.com", "bididi88@gmail.com"],
    [None, None, None, None],
    ["Руслан Лобли;03/04/25", "Нет", "ruslan90@yandex.ru", "ruslan90@yandex.ru"],
    [None, None, None, None],
    ["Вадим Суфимянц;04/11/25", "Да", "sufimanz9@mail.ru", "sufimanz9@mail.ru"]
]

result_table = main(input_table)

# Вывод результата
for row in result_table:
    print('\t'.join(row))






'''
def cycle2(unique_rows):
    for row in unique_rows:
        un = row[0].split(';')[0]
        row[0] = row[0].split(';')[1] if ';' in row[0] else row[0]
        row[0] = "/".join(row[0].split('/')[::-1])
        row[1] = "Выполнено" if row[1] == "Да" else "Не выполнено"
        row[2] = un.split()[1]
        row[3] = row[3].split('@')[0]


def cycle1(input_table_copy, seen_rows, unique_rows):
    for row in input_table_copy:
        if tuple(row) not in seen_rows and all(row):
            unique_rows.append(row)
            seen_rows.add(tuple(row))


def main(input_table):
    # Копируем исходную таблицу, чтобы избежать изменений входных данных
    input_table_copy = [row[:] for row in input_table]

    unique_rows = []
    seen_rows = set()

    cycle1(input_table_copy, seen_rows, unique_rows)

    cycle2(unique_rows)

    return unique_rows

# Пример использования
input_table = [
    ["Макар Каманов;00/01/24", "Да", "kamanov78@mail.ru", "kamanov78@mail.ru"],
    ["Макар Каманов;00/01/24", "Да", "kamanov78@mail.ru", "kamanov78@mail.ru"],
    ["Тихон Бидиди;02/01/19", "Да", "bididi88@gmail.com", "bididi88@gmail.com"],
    [None, None, None, None],
    ["Руслан Лобли;03/04/25", "Нет", "ruslan90@yandex.ru", "ruslan90@yandex.ru"],
    [None, None, None, None],
    ["Вадим Суфимянц;04/11/25", "Да", "sufimanz9@mail.ru", "sufimanz9@mail.ru"]
]

result_table = main(input_table)

# Вывод результата
for row in result_table:
    print('\t'.join(row))
'''





'''
def main(input_table):
    # Удаление дублей среди столбцов
    unique_columns = [list(set(col)) for col in zip(*input_table)]

    # Удаление дублей среди строк
    seen_rows = set()
    unique_rows = [row for row in input_table
                   if tuple(row) not in
                   seen_rows and not seen_rows.add(tuple(row))]

    # Удаление пустых строк
    non_empty_rows = [row for row in unique_rows if all(row)]

    # Разбиение одного из столбцов по разделителю ";"
    for row in non_empty_rows:
        if ';' in row[0]:
            row[0] = row[0].split(';')[1]

    # Преобразование содержимого ячеек
    for row in non_empty_rows:
        date_parts = row[0].split('/')
        row[0] = "/".join([date_parts[2], date_parts[1], date_parts[0]])
        row[1] = "Выполнено" if row[1] == "Да" else "Не выполнено"
        if ' ' in row[2]:
            row[2] = row[2].split()[1]
        row[3] = row[3].split('@')[0]

    return non_empty_rows

# Пример использования
input_table = [
    ["Макар Каманов;00/01/24", "Да", "kamanov78@mail.ru", "kamanov78@mail.ru"],
    ["Макар Каманов;00/01/24", "Да", "kamanov78@mail.ru", "kamanov78@mail.ru"],
    ["Тихон Бидиди;02/01/19", "Да", "bididi88@gmail.com", "bididi88@gmail.com"],
    ["Руслан Лобли;03/04/25", "Нет", "ruslan90@yandex.ru", "ruslan90@yandex.ru"],
    ["Вадим Суфимянц;04/11/25", "Да", "sufimanz9@mail.ru", "sufimanz9@mail.ru"]
]

result_table = main(input_table)

# Вывод результата
for row in result_table:
    print('\t'.join(row))
'''










