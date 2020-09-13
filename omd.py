'''
Kryazheva Daria
'''
import random
from time import sleep


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
        if option == 'да':
            print('''Утка добралась до бара и не промокла. В баре звери решили развлечься и сыграть в увлекательную игру. 

Правила игры: 4 зверя играют в игру. Трое из них знают загаданное место, они - граждане, один зверь не знает загаданного места, он - шпион. 
Все игроки по очереди задают другу тематические вопросы и отвечают на них да или нет в зависимости от того, подходит ли заданный вопрос к загаданному месту.
Задача граждан вычислить шпиона по тому, как он отвечает на вопросы, задача шпиона по вопросам определить загаданное место''')
        else:
            print('''Утка промокла, но в баре ей любезно предложили теплый плед. Звери решили развлечься и сыграть в увлекательную игру. 

Правила игры: 4 зверя играют в игру. Трое из них знают загаданное место, они - граждане, один зверь не знает загаданного места, он - шпион. 
Все игроки по очереди задают другу тематические вопросы и отвечают на них да или нет в зависимости от того, подходит ли заданный вопрос к загаданному месту.
Задача граждан вычислить шпиона по тому, как он отвечает на вопросы, задача шпиона по вопросам определить загаданное место.''')
    sleep(20)
PREVIEW = '''Игра начинается, ваша роль: {}.'''

PREVIEW_PLACE = '''ВНИМАНИЕ!!! Вы находитесь в месте под названием: {}.'''

PREVIEW_PLACE_SPY = '''Возможные места, в которых могут находится граждане: \n{}\n'''

LOSE = [
    '''К сожалению, Вы неправильно выбрали шпиона. Попробуйте быть внимательнее к деталям. Шпионом был: {}''',
    '''К сожалению, другие игроки нашли шпиона в отличие от Вас. Попробуйте быть внимательнее к деталям. Шпионом был: {}''',
    '''К сожалению, Вас обнаружили!!! Вы неправильно ответили на вопрос :)''',
    '''К сожалению, Вы неправильно выбрали место. Попробуйте быть внимательнее к деталям.'''
]

WINE = [
    '''Поздравляем, вы нашли шпиона!''',
    '''Поздравляем, вы правильно определили место!''',
]

PERSONS = [
    '''Лиса-визажист''',
    '''Заяц-бариста''',
    '''Лев-дизайнер''',
]

QUESTION_SUDO = [
    '''{} задает вопрос: {}, {}''',
]

ANSWER_SUDO = [
    '''{} отвечает: {}.'''
]

ANSWER_YOUR = '''Ответьте на вопрос (да/нет): '''

VOTE_PREVIEW = '''Вы готовы выбрать шпиона?'''

VOTE_YES = '''Назовите подозреваемого: '''

VOTE_NO = '''Хорошо, продолжаем игру :)'''

PLACE_PREVIEW = '''Вы готовы выбрать место?'''

PLACE_YES = '''Назовите место: '''

PLACE_NO = '''Хорошо, продолжаем игру :)'''

PLACE_QUESTIONS = {
    'Парк': [
        '''Часто ли вы встречаете здесь детей?''',
        '''Можно ли там найти ларек с мороженым?''',
        '''Можно там искупаться в фонтане?''',
        '''Есть ли там аттракционы''',
        '''Поедем туда кататься на роликах?''',
    ],
    'Рыбалка': [
        '''Будешь брать с собой снаряжение?''',
        '''Мечтал поймать золотую рыбку?''',
        '''Пригодятся высокие сапожки?''',
        '''Возьмешь с собой палатку?''',
        '''Берем с собой корм?''',
    ],
    'Спортивный зал': [
        '''Возьмешь парочку килограмм?''',
        '''Часто измеряешь талию?''',
        '''Одолжишь резинки?''',
        '''Считаешь калории?''',
    ],
}

PLACES = ['Парк', 'Рыбалка', 'Спортивный зал', 'Концертный зал', 'Аквапарк', 'Цирк', 'Каток', 'Лес', 'Горы', 'Больница',
          'Аптека', 'Рынок']

ROLES = ['Шпион', 'Гражданин']


class GameSpy:
    def __init__(self, role):
        self.role = role
        self.bots = PERSONS
        self.init_game_()
        self.step_num = 0
        self.good_places = list(PLACE_QUESTIONS.keys())
        self.game_flag = True

    def init_game_(self):
        random.shuffle(self.bots)
        if self.role == 'Шпион':
            self.spy = 'Утка-маляр'
            self.persons = self.bots
        else:
            self.spy = self.bots[0]
            self.persons = self.bots[1:] + ['Утка-маляр']
        self.chain = [(_, False) for _ in self.persons] + [(self.spy, True)]
        random.shuffle(self.chain)

        self.place = random.choice(list(PLACE_QUESTIONS.keys()))

        if self.role == 'Гражданин':
            print(PREVIEW_PLACE.format(self.place))
        else:
            print(PREVIEW_PLACE_SPY.format(', '.join(PLACES)))
        sleep(4)

    def start(self):
        while True:
            self.step_()
            if self.role == 'Гражданин':
                if self.voite_spy_():
                    print('Пока')
                    return
                if not self.game_flag:
                    print(LOSE[1].format(self.spy))
                    return
                continue
            else:
                if self.voite_place_():
                    print('Пока')
                    return
                if self.game_flag:
                    continue
                else:
                    print(LOSE[2])
                    return

    def step_(self):
        for q_number in range(len(self.chain)):
            person1 = self.chain[q_number % len(self.chain)]
            person2 = self.chain[(q_number + 1) % len(self.chain)]
            place = random.choice(self.good_places)

            question = random.choice(PLACE_QUESTIONS[place])
            question_text = random.choice(QUESTION_SUDO)
            print(question_text.format(person1[0], person2[0], question))

            if person2[0] == 'Утка-маляр':
                print(ANSWER_YOUR)
                answer = input()
            else:
                if person2[1]:
                    answer = random.choice(['да', 'нет'])
                else:
                    answer = 'да' if self.place == place else 'нет'
            flag = True
            if answer == 'да' and not self.place == place or answer == 'нет' and self.place == place:
                flag = False
            self_flag = self.role == 'Гражданин' and not person2 == 'Утка-маляр'
            self.game_flag = True if self.game_flag and flag else False
            self.game_flag = self_flag or self.game_flag
            print(random.choice(ANSWER_SUDO).format(person2[0], answer))
            print('----------------------------------')
            sleep(4)

    def voite_spy_(self):
        print(VOTE_PREVIEW)
        answer = input()
        if answer == 'да':
            print(VOTE_YES)
            answer = input()
            if self.spy == answer:
                print(WINE[0])
            else:
                print(LOSE[0].format(self.spy))
            return True
        else:
            print(VOTE_NO)
            return False

    def voite_place_(self):
        print(PLACE_PREVIEW)
        answer = input()
        if answer == 'да':
            print(PLACE_YES)
            answer = input()
            if self.place.lower() == answer.lower():
                print(WINE[1])
            else:
                print(LOSE[3])
            return True
        else:
            print(VOTE_NO)
            return False


if __name__ == '__main__':
    step1()
    while True:
        role = random.choice(ROLES)
        print(PREVIEW.format(role))
        game = GameSpy(role)
        game.start()
        print('''Вы хотите начать заново?''')
        answer = input()
        if answer == 'да':
            print(chr(27) + "[2J")
            continue
        break
