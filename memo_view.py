import json
import os
import sys
from datetime import datetime as dt
from memo_note import Note
from memo_model import NoteJson

# number_note, name_note, text_notes, date_note

def run():
    path_json = "notes_save.json"
    c = NoteJson(path_json)
    
    while True:
        # clear()
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
            # print(get_add_note())
        elif user_choice == 2:
            get_read_note()
        elif user_choice == 3:
            update_note()
        elif user_choice == 4:
            del_note()
        elif user_choice == 5:
            del_all_notes()
        elif user_choice == 6:
            notes = c.read_notes()
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
    date_note = dt.now()
    name_note = input('Введите заголовок заметки: ')
    text_notes = input('Введите тело заметки: ')
    return Note(number_note, name_note, text_notes, date_note)


def get_read_note():

    pass

def update_note():
    pass

def del_note():
    pass

def del_all_notes():
    pass

def read_all_notes(notes):
    for item in notes:
        print(item)

def end_of_program():
    clear()
    # if input('Are you sure? Press "y" for exit and "n" for return to main menu.\n') == 'y':
    #     clear()
    sys.exit()
