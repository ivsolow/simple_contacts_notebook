from typing import List


def display_page(entries: List[str], page_num: int, entries_per_page: int) -> None:
    """
    Выводит запись в телефонной книге.

    Args:
        entries (List[str]): Список записей для отображения.
        page_num (int): Номер страницы.
        entries_per_page (int): Количество записей на странице.
    """
    start_idx = (page_num - 1) * entries_per_page
    end_idx = start_idx + entries_per_page
    for entry in entries[start_idx:end_idx]:
        print(entry)
