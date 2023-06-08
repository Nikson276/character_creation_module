from random import randint

from graphic_arts.start_game_banner import run_screensaver

# Global constant
DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80


class Character:
    name: str
    value_attack: int
    value_defence: int

    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'
    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)
    SPECIAL_BUFF = 15
    SPECIAL_SKILL = 'Удача'

    # Объявляем конструктор класса
    def __init__(self, name):
        self.name = name

    # Объявляем метод атаки
    def attack(self) -> str:
        # Вместо диапазона записана переменная класса.
        # Оператор * распаковывает передаваемый кортеж.
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный {value_attack}')

    # Объявляем метод защиты.
    def defence(self):
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона.')

    # Объявляем метод специального умения.
    def special(self):
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}"')

    def __str__(self):
        return (f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}')


class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита'


def start_training(character: Character) -> str:
    """Do the training process.
    Args:
        char_name (str): Name of character
        char_class (str): Class of character

    Returns:
        str: Message about character ability description.
        Message with commands for training process.
        All messages by comands.
    """
    # dict with commands
    commands = {
        'attack': character.attack,
        'defence': character.defence,
        'special': character.special,
    }
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: '
          'attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd = str.lower(input('Введи команду: '))
        if cmd in commands:
            # output in terminal result of cmd method
            print(commands[cmd]())
        else:
            print(f'{cmd} Такой команды нет')
    return 'Тренировка окончена.'


def choice_char_class(char_name) -> Character:
    """Do dialog with the player.

    Returns:
        str: Ask to input and aprove character name.
        Description of the choosen character.
    """
    approve_choice: str = ''
    # Словарь, в котором используется ввод пользователя и класс персонажа.
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}

    while approve_choice != 'y':
        selected_class = str.lower(input('Введи название персонажа, '
                                         'за которого хочешь играть: '
                                         'Воитель — warrior, '
                                         'Маг — mage, '
                                         'Лекарь — healer: '))
        if selected_class in game_classes:
            # Сreate object from class from dict
            char_class: Character = game_classes[selected_class](char_name)
        else:
            print(f'"{selected_class}" Такого персонажа нет в игре :/)')
            continue
        # output in terminal character description
        print(char_class)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: Character = choice_char_class(char_name)
    print(start_training(char_class))

