import csv
from datetime import datetime
from model.note import Note


class NoteManager:
    def __init__(self):
        self.notes = []
        self.load_from_file()

    def load_from_file(self):
        self.notes = []
        try:
            with open("notes.csv", newline="") as file:
                reader = csv.reader(file, delimiter=";")
                next(reader)
                for row in reader:
                    id, title, body, created_at = row
                    self.notes.append(Note(id, title, body, created_at))
        except FileNotFoundError:
            self.create_empty_file()

    def create_empty_file(self):
        with open("notes.csv", "w", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(["ID", "Title", "Body", "Created At"])

    def create_note(self, title, body):
        id = self.generate_unique_id()
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note = Note(id, title, body, created_at)
        self.notes.append(note)
        self.save_to_file()
        self.load_from_file()

    def generate_unique_id(self):
        if not self.notes:
            return 1
        else:
            return int(self.notes[-1].id) + 1


    def read_notes(self):
        separator_line = "-" * 30
        sorted_notes = sorted(self.notes, key=lambda x: x.created_at, reverse=True)
        for note in sorted_notes:
            print(separator_line)
            print(note)
            print(separator_line)
            print()

    def update_note(self, id, new_title=None, new_body=None):
        note_found = False
        for note in self.notes:
            if note.id == id:
                note_found = True
                if new_title is not None:
                    note.title = new_title
                if new_body is not None:
                    note.body = new_body
                note.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_to_file()
                print("Заметка успешно отредактирована.")
                break

        if not note_found:
            print("ОШИБКА: Заметка с указанным ID не найдена. Пожалуйста, введите другой ID.")

    def delete_note(self, id):
        note_exists = False
        for note in self.notes:
            if note.id == id:
                self.notes.remove(note)
                note_exists = True
                break

        if not note_exists:
            print("ОШИБКА: Заметка с указанным ID не найдена. Пожалуйста, введите другой ID.")
            return

        self.save_to_file()
        print("Заметка успешно удалена.")

    def save_to_file(self):
        with open("notes.csv", "w", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(["ID", "Title", "Body", "Created At"])
            for note in self.notes:
                writer.writerow([note.id, note.title, note.body, note.created_at])

    def read_notes_by_date(self, start_date, end_date):
        self.load_from_file()

        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

        separator_line = "-" * 30
        filtered_notes = []

        for note in self.notes:
            note_created_at = datetime.strptime(note.created_at, "%Y-%m-%d %H:%M:%S")
            if start_date <= note_created_at <= end_date:
                filtered_notes.append(note)

        if filtered_notes:
            for note in filtered_notes:
                print(separator_line)
                print(note)
                print(separator_line)
                print()
        else:
            print("Нет заметок в указанном диапазоне дат.")
    def read_note_by_id(self, id):
        separator_line = "-" * 30
        note = next((note for note in self.notes if note.id == id), None)
        if note:
            print("Заметка найдена:")
            print(separator_line)
            print(note)
            print(separator_line)
            print()
        else:
            print("Заметка с указанным ID не найдена.")