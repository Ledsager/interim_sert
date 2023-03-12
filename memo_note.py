class Note(object):

    def __init__(self, number_note, name_note, text_notes, date_note):
        self.number_note = number_note
        self.name_note = name_note
        self.text_notes = text_notes
        self.date_note = date_note

    @property
    def number_note(self):
        return self._number_note

    @number_note.setter
    def number_note(self, number_note):
        self._number_note = number_note

    @property
    def name_note(self):
        return self._name_note

    @name_note.setter
    def name_note(self, name_note):
        self._name_note = name_note

    @property
    def text_notes(self):
        return self._text_notes

    @text_notes.setter
    def text_notes(self, text_notes):
        self._text_notes = text_notes

    @property
    def date_note(self):
        return self._date_note

    @date_note.setter
    def date_note(self, date_note):
        self._date_note = date_note

    def __str__(self):
        return f'\n : {self._number_note}\n :' \
            f'{self._name_note}\n : {self._text_notes}\n : {self._date_note}\n '
