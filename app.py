from interface import display_page
from logic import add_entry, find_last_name, edit_entry, search_entries

ENTER_NEW_RECORD = (
    "Введите новую запись (в формате: фамилия, имя, отчество, название организации,"
    " телефон рабочий, телефон личный): "
)
ENTER_LAST_NAME = (
    "Введите фамилию для поиска записи (как уникальный идентификатор)"
    " или 0 для возврата в главное меню: "
)
ENTER_QUERY = "Введите строку для поиска: "
INVALID_CHOICE = "Неверный выбор. Попробуйте снова."
RECORD_NOT_FOUND = "Запись с указанной фамилией не найдена."
MULTIPLE_RECORDS_FOUND = "Найдено несколько записей с указанной фамилией. Уточните запрос."
RETURN_TO_MAIN_MENU = "Возврат в главное меню."
ENTER_PAGE_NUMBER = "Введите номер страницы: "
ENTER_ENTRIES_PER_PAGE = "Введите количество записей на странице: "
SELECT_ACTION = "Выберите действие: "

MENU_OPTIONS = {
    "1": "Вывод записей",
    "2": "Добавление записи",
    "3": "Редактирование записи",
    "4": "Поиск записей"
}


def main() -> None:
    """Главная функция для запуска телефонной книги."""
    with open("phonebook.txt", "r") as file:
        entries = [line.strip() for line in file.readlines()]

    while True:
        print("\nМеню:")
        for option_num, option_text in MENU_OPTIONS.items():
            print(f"{option_num}. {option_text}")
        choice = input(SELECT_ACTION)

        if choice == "1":
            page_num = int(input(ENTER_PAGE_NUMBER))
            if page_num == 0:
                continue
            entries_per_page = int(input(ENTER_ENTRIES_PER_PAGE))
            display_page(entries, page_num, entries_per_page)
        elif choice == "2":
            entry = input(ENTER_NEW_RECORD)
            add_entry(entries, entry)
        elif choice == "3":
            last_name = input(ENTER_LAST_NAME)
            if last_name == "0":
                continue
            found = find_last_name(entries, last_name)
            if not found:
                print(RECORD_NOT_FOUND)
                continue
            elif found == 1:
                print(MULTIPLE_RECORDS_FOUND)
                continue

            print(f"Найдена следующая запись: {found}")
            new_entry = input(ENTER_NEW_RECORD)
            if new_entry == "0":
                continue

            edit_entry(entries, found, new_entry)
        elif choice == "4":
            query = input(ENTER_QUERY)
            search_entries(entries, query)
        else:
            print(INVALID_CHOICE)


if __name__ == "__main__":
    main()
