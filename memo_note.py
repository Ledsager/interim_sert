class Note(object):

    def __init__(self, id_note, name_note, text_notes, date_note) -> None:
        self.id_note = id_note
        self.name_note = name_note
        self.text_notes = text_notes
        self.date_note = date_note

    @id_note.setter
    def id_note(self, id_note):
        self._id_note = id_note

    @property
    def id_note(self):
        return self._id_note

    @name_note.setter
    def name_note(self, name_note):
        self._name_note = name_note

    @property
    def name_note(self):
        return self._name_note

    @text_notes.setter
    def text_notes(self, text_notes):
        self._text_notes = text_notes

    @property
    def text_notes(self):
        return self._text_notes

    @date_note.setter
    def date_note(self, date_note):
        self._date_note = date_note

    @property
    def date_note(self):
        return self._date_note

    def __str__(self):
        return f'\nЗаметка: {self._note_id}\nДата создания(редактирования):' \
               f' {self._date}\nЗаголовок: {self._title}\nТело: {self._text}\n '
    