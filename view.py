from colorama import Fore, Style

class View(object):
    @staticmethod
    def print_divider(symbol = "=", n = 80):
        return (symbol * n)
    
    @staticmethod
    def display_note_stored():
        print(Fore.YELLOW + '+++++++++++++++++++++++++++++++++++' + Style.RESET_ALL)
        print(Fore.GREEN + 'Заметка успешно добавлена!' + Style.RESET_ALL)
        print(Fore.YELLOW + '+++++++++++++++++++++++++++++++++++' + Style.RESET_ALL)
    
    @staticmethod
    def show_note(note):
        print(Fore.YELLOW + '+++++++++++++++++++++++++++++++++++' + Style.RESET_ALL)
        print(note)
        print(Fore.YELLOW + '+++++++++++++++++++++++++++++++++++' + Style.RESET_ALL)

    @staticmethod
    def display_note_id_not_exist(note_id):
        print(Fore.RED + '+++++++++++++++++++++++++++++++++++' + Style.RESET_ALL)
        print('Заметка с id:{} не найдена!'.format(note_id))
        print(Fore.RED + '+++++++++++++++++++++++++++++++++++'+ Style.RESET_ALL)
    