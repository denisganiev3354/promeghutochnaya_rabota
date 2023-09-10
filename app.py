from colorama import Fore, Style
def run():
    c = Controller(ModelJSON("notes.json"), View())
    while True:
        command = input(Fore.BLUE +
            '1 - создать заметку\n'
            '2 - прочитать заметку \n'
            '3 - обновить заметку \n'
            '4 - удалить заметку \n'
            '5 - удалить все заметки \n'
            '6 - прочитать все заметки \n'
            '7 - выход \n'
            'Сделайте Ваш выбор: '
            + Style.RESET_ALL)
        if command == '7':
            break

        if command == '1':
            print(Fore.GREEN + '\nсоздать заметку:' + Style.RESET_ALL)
            c.create_note(get_note_data())
        
        elif command == '2':
            print(Fore.GREEN + '\nпрочитать заметку:' + Style.RESET_ALL)
            if c.notes_exist():
                c.show_note(int(get_number()))
        elif