from manager.note_manager import NoteManager
from datetime import datetime

def main():
    note_manager = NoteManager()

    while True:
        print()
        print("Выберите действие:")
        print("1. Создать заметку")
        print("2. Показать все заметки")
        print("3. Найти заметки по дате")
        print("4. Найти заметки по id")
        print("5. Редактировать заметку")
        print("6. Удалить заметку")
        print("7. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            note_manager.create_note(title, body)
        elif choice == "2":
                note_manager.read_notes()
        elif choice == "3":
            while True:
                start_date = input("Введите начальную дату (ГГГГ-ММ-ДД): ")
                try:
                    datetime.strptime(start_date, "%Y-%m-%d")
                    break
                except ValueError:
                    print("ОШИБКА: Неправильный формат даты. Пожалуйста, введите дату в формате ГГГГ-ММ-ДД.")

            while True:
                end_date = input("Введите конечную дату (ГГГГ-ММ-ДД): ")
                try:
                    datetime.strptime(end_date, "%Y-%m-%d")
                    break
                except ValueError:
                    print("ОШИБКА: Неправильный формат даты. Пожалуйста, введите дату в формате ГГГГ-ММ-ДД.")

            note_manager.read_notes_by_date(start_date, end_date)
        elif choice == "4":
            id = input("Введите ID заметки для поиска: ")
            note_manager.read_note_by_id(id)
        elif choice == "5":
            id = input("Введите ID заметки для редактирования: ")
            note_to_update = next((note for note in note_manager.notes if note.id == id), None)
            if note_to_update:
                new_title = input("Введите новый заголовок заметки: ")
                new_body = input("Введите новый текст заметки: ")
                note_manager.update_note(id, new_title, new_body)
            else:
                print("ОШИБКА: Заметка с указанным ID не найдена. Пожалуйста, введите другой ID.")
        elif choice == "6":
            id = input("Введите ID заметки для удаления: ")
            note_manager.delete_note(id)
        elif choice == "7":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите правильный номер действия.")

if __name__ == "__main__":
    main()