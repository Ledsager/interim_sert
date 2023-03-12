import os
import sys
from datetime import datetime as dt
from memo_note import Note
from memo_model import NoteJson
from pathlib import Path


def run():
    path_json = "notes_save.json"
    c = NoteJson(path_json)
    path = Path(path_json)
    path.touch(exist_ok=True)

    while True:
        clear()
        print('Добро пожаловать на первую программу промежуточной аттестации!')
        user_choice = int(input('Выберите один из пунктов:\n'
                                '1 - создать заметку\n'
                                '2 - прочитать заметку\n'
                                '3 - обновить заметку\n'
                                '4 - удалить заметку\n'
                                '5 - удалить все заметки\n'
                                '6 - прочитать все заметки\n'
                                '7 - выход\n'))

        if user_choice == 1:
            c.create_note(get_add_note())
        elif user_choice == 2:
            if c.file_null:
                read_note = int(note_number())
                print(c.read_one_note(read_note))
            enter_in()
        elif user_choice == 3:
            if c.file_null:
                update_note_number = int(note_number())
                c.update_note(update_note_number, get_add_note())
            enter_in()
        elif user_choice == 4:
            if c.file_null:
                del_note = int(note_number())
                c.del_one_notes(del_note)
            enter_in()
        elif user_choice == 5:
            if c.file_null:
                c.del_all_notes()
            enter_in()
        elif user_choice == 6:
            if c.file_null:
                notes = c.read_json()
                read_all_notes(notes)
            enter_in()
        elif user_choice == 7:
            end_of_program()
        else:
            print('Неверно выбран пункт меню!')
            enter_in()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def enter_in():
    enter_inp = input('Нажмите любую клавишу')


def get_add_note():
    number_note = 0
    name_note = input('Введите заголовок заметки: ')
    text_notes = input('Введите тело заметки: ')
    date_note = dt.now()
    return Note(number_note, name_note, text_notes, date_note)


def read_all_notes(notes):
    for item in notes:
        print(item)


def note_number():
    while True:
        number_note = input('Введите id заметки: ')
        if number_note.isdigit() and int(number_note) > 0:
            return number_note
        else:
            print('Введите целое число(номер заметки)!')


def end_of_program():
    clear()
    # if input('Are you sure? Press "y" for exit and "n" for return to main menu.\n') == 'y':
    #     clear()
    sys.exit()
