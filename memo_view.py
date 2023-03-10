import os
import sys


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def add_note():
    pass


def read_note():
    pass


def update_note():
    pass


def del_note():
    pass


def del_all_notes():
    pass


def read_all_notes():
    pass


def end_of_program():
    clear()
    if input('Are you sure? Press "y" for exit and "n" for return to main menu.\n') == 'y':
        clear()
        sys.exit()


our_list = []

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
        add_note(our_list)
    elif user_choice == 2:
        read_note(our_list)
    elif user_choice == 3:
        update_note(our_list)
    elif user_choice == 4:
        del_note(our_list)
    elif user_choice == 5:
        del_all_notes(our_list)
    elif user_choice == 6:
        read_all_notes(our_list)
    elif user_choice == 7:
        end_of_program()
    else:
        enter_in = input('Неверно выбран пункт меню!')
