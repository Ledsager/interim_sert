import json
# import copy
from datetime import datetime as dt
import pathlib
from memo_note import Note

# number_note, name_note, text_notes, date_note


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

    def read_note(self, search_id):
        self.notes = self.read_notes()
        for note in self.notes:
            if note.number_note == search_id:
                return note
        else:
            print("not notes")

    def read_notes(self):
        return self.read_json()

    def write_json(self, notes):
        json_strings_list = list()
        for note in notes:
            json_strings_list.append(
                {'id': note.number_note, 'date': note.date_note, 'title': note.name_note, 'text': note.text_notes})

        notes_json = json.dumps(
            json_strings_list, indent=4, ensure_ascii=False, sort_keys=False, default=str)

        with open(self.path_json, "w", encoding='utf-8') as my_file:
            my_file.write(notes_json)

    def read_json(self):
        notes_list1 = list()
        path = pathlib.Path(self.path_json)
        if path.exists():
            action_file = "r"
        else:
            action_file = "a"
#        try:
        with open(self.path_json, action_file, encoding='utf-8') as my_file:
            notes_json = my_file.read()
            data = json.loads(notes_json)
            data.sort(key=lambda x: x['date'])
            for item in data:
                notes_list1.append(
                    Note(item['id'], item['date'], item['title'], item['text']))
                # print(item)
            return notes_list1
#        except ValueError:
#            return self.notes

# NoteJson.write_json(path_json, st)
