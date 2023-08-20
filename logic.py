from typing import List, Union


INVALID_FORMAT = "Ошибка: неверный формат записи."
RECORD_ADDED = "Запись успешно добавлена."
RECORD_EDITED = "Запись успешно отредактирована."


def validate_entry(entry: str) -> bool:
    """
    Проверяет корректность формата записи.
    Новая запись должна содержать поля:
    фамилия, имя, отчество, название организации,
    телефон рабочий, телефон личный, то есть состоять
    из 6 элементов, перечисленных через запятую

    Args:
        entry (str): Запись для проверки.

    Returns:
        bool: True, если формат записи корректен, иначе False.
    """
    parts = entry.split(", ")
    if len(parts) != 6:
        print(INVALID_FORMAT)
        return False
    return True


def add_entry(entries: List[str], entry: str) -> None:
    """
    Добавляет новую запись в телефонную книгу.

    Args:
        entries (List[str]): Список текущих записей.
        entry (str): Новая запись для добавления.
    """
    if entry == "0":
        return
    if validate_entry(entry):
        entries.append(entry)
        save_entries(entries)
        print(RECORD_ADDED)


def find_last_name(entries: List[str], last_name: str) -> Union[int, str]:
    """
    Находит запись в файле по фамилии.

    Args:
        entries (List[str]): Список записей для поиска.
        last_name (str): Фамилия для поиска.

    Returns:
        Union[int, str]: 0, если запись не найдена,
        1, если найдено несколько записей, или
        найденная запись, если найдена только одна.
    """
    matching_entries = get_matching_entries(entries, last_name)
    if not matching_entries:
        return 0
    if len(matching_entries) > 1:
        return 1
    return matching_entries[0]


def edit_entry(entries: List[str], existing_entry: str, new_entry: str) -> None:
    """
    Редактирует существующую запись в телефонной книге.

    Args:
        entries (List[str]): Список текущих записей.
        existing_entry (str): Существующая запись для редактирования.
        new_entry (str): Новая запись для замены существующей.
    """
    if validate_entry(new_entry):
        entry_index = entries.index(existing_entry)
        entries[entry_index] = new_entry
        save_entries(entries)
        print(RECORD_EDITED)


def get_matching_entries(entries: List[str], query: str) -> List[str]:
    """
    Возвращает список записей, соответствующих запросу.

    Args:
        entries (List[str]): Список записей для поиска.
        query (str): Строка запроса.

    Returns:
        List[str]: Список записей, соответствующих запросу.
    """
    matching_entries = [entry for entry in entries if query.lower() in entry.lower()]
    return matching_entries


def search_entries(entries: List[str], query: str) -> None:
    """
    Поиск и вывод записей по запросу.

    Args:
        entries (List[str]): Список записей для поиска.
        query (str): Строка запроса.
    """
    if query == "0":
        return
    for entry in get_matching_entries(entries, query):
        print(entry)


def save_entries(entries: List[str]) -> None:
    """
    Сохраняет записи в файл.

    Args:
        entries (List[str]): Список записей для сохранения.
    """
    with open("phonebook.txt", "w") as file:
        for entry in entries:
            file.write(entry + "\n")

