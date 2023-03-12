import json
from memo_note import Note


class NoteJson(object):

    def __init__(self, path_json):
        self.path_json = path_json
        self.notes = list()

    def create_note(self, note):
        self.notes = self.read_notes()
        max_id = 0
        for item in self.notes:
            if item.number_note > max_id:
                max_id = item.number_note
        number_note = max_id + 1
        note.number_note = number_note

        self.notes.append(note)
        self.write_json(self.notes)

    def read_one_note(self, search_id):
        self.notes = self.read_notes()
        for note in self.notes:
            if note.number_note == search_id:
                return note

    def update_note(self, update_note_number, note):
        self.notes = self.read_notes()
        for item in self.notes:
            if item.number_note == update_note_number:
                item.name_note = note.name_note
                item.text_notes = note.text_notes
                item.date_note = note.date_note

        self.write_json(self.notes)

    def read_notes(self):
        return self.read_json()

    def del_one_notes(self, num_note):
        self.notes = self.read_notes()
        for index, note in enumerate(self.notes):
            if note.number_note == num_note:
                del self.notes[index]

        self.write_json(self.notes)

    def del_all_notes(self):
        self.notes = self.read_notes()
        self.notes.clear()
        self.write_json(self.notes)

    def file_null(self):
        notes_len = self.read_notes()
        if len(notes_len) == 0:
            return False
        else:
            return True

    def write_json(self, notes):
        json_strings_list = list()
        for note in notes:
            json_strings_list.append(
                {'id': note.number_note, 'title': note.name_note, 'text': note.text_notes, 'date': note.date_note})
        notes_json = json.dumps(
            json_strings_list, indent=4, ensure_ascii=False, sort_keys=False, default=str)
        with open(self.path_json, "w", encoding='utf-8') as my_file:
            my_file.write(notes_json)

    def read_json(self):
        notes_list1 = list()
        try:
            with open(self.path_json, "r", encoding='utf-8') as my_file:
                notes_json = my_file.read()
            data = json.loads(notes_json)
            data.sort(key=lambda x: x['date'])
            for item in data:
                notes_list1.append(
                    Note(item['id'], item['title'], item['text'], item['date']))
            return notes_list1
        except ValueError:
            return self.notes
