from random import *

def is_bet_good(bet):
    return len(bet) == 3 and 100 <= bet[0] <= balance and bet[0] <= balance_bot and bet[1] in list_coef and bet[2] in list_bet

def quantity_trying(bet):
    if bet[2] == 100:
        if bet[1] == 2:
            return 6
        elif bet[1] == 4:
            return 5
        else:
            return 4
    elif bet[2] == 1000:
        if bet[1] == 2:
            return 9
        elif bet[1] == 4:
            return 8
        else:
            return 7
    else:
        if bet[1] == 2:
            return 13
        elif bet[1] == 4:
            return 12
        else:
            return 11 

        
def game():  
    
    global balance
    global balance_bot
    
    print('Ты готов обыграть меня и стать новым Ультрабанкиром? ')
    print('\nВ твоем активе:', balance, 'ультрадолларов')
    print('В моем активе:', balance_bot, 'ультрадолларов')
    print('Доступные коэффициенты:')
    print('коэф. 2, при ставке на: [1-100 - 6 попыток] [1-1000 - 9 попыток] [1-10000 - 13 попыток]')
    print('коэф. 4, при ставке на: [1-100 - 5 попыток] [1-1000 - 8 попыток] [1-10000 - 12 попыток]')
    print('Супер шанс: коэф. 10, при ставке на: [1-100 - 4 попыток] [1-1000 - 7 попыток] [1-10000 - 11 попыток]')
    
    print('Чтобы предложить цену покупки акции (твою ставку), введи через ПРОБЕЛЫ БЕЗ СКОБОК: [Cумма ставки (мин. 100 ультрадолларов)] [выбранный коэф.] [последнее число диапазона чисел] (к примеру: 500 4 10000)')
    bet = [int(i) for i in input().split()]
    while not is_bet_good(bet):
        bet = [int(i) for i in input('Неправильный формат! Формат должен быть: Сумма(не менее 100) Коэффициент(2, 4, 10) Ограничивающее_Число(1000, 10000 или 100000): ').split()]

    number = randint(1, bet[2])
    trying = quantity_trying(bet)
    balance -= bet[0]
    balance_bot += bet[0]
    print('Я готов продать акцию за сумму в диапазоне от 1 до', bet[2], '. Попробуй угадай! У тебя', trying, 'попыток.')

    while True:
        num = int(input())
        trying -= 1
        if trying < 0:
            print('К сожалению, твои попытки истекли. Ты проиграл свою ставку на бирже. Чемпион был готов продать свои акции за', number)
            break
        elif num > number:
            print('Я готов продать дешевле. У тебя осталось', trying, 'попыток. Попробуй еще раз.')
        elif num < number:
            print('Я готов продать дороже. У тебя осталось', trying, 'попыток')
        else:
            print('Ты был прав,', name.title(), '. Ты выкупил мои акции за', bet[0] * bet[1], '. Поздравляю, твои активы растут!.')
            balance += bet[0] * bet[1]
            balance_bot -= bet[0] * bet[1]
            break
            
    next = input('Чтобы продолжить играть на бирже, напиши "далее"\n')
    while next.lower() != 'далее':
        next = input('Чтобы продолжить играть на бирже, введи "Далее"')
        
    game()

    
 
print('Добро пожаловать в игру Ультрабанкир! Меня зовут бот Форбс! С моей помощью ты сможешь разобраться в правилах игры, обыграть текущего чемпиона и стать новым Ультрабанкиром! Заманчиво, ведь правда? Давай же приступим. Чтобы продолжить, введи "Гоу"')
next = input()
while next.lower() != 'гоу':
    next = input('Чтобы продолжить, введи "Гоу"')
   
print('\nНачинаем. У тебя есть актив в 1000 ультрадолларов. Чтобы опередить текущего Чемпиона Форбс и стать новым Ультрабанкиром и попасть на 1 место в списке бота Форбс, тебе необходимо выкупить у Чемпиона все имеющиеся у него акции компании по выгодной цене на общую сумму 9000 ультрадолларов, а также тебе нужно не потерять свои деньги. Это будет непросто, как и в бизнесе, но ты справишься, поверь мне! Тебе нужно угадать за какую сумму Чемпион готов продать свои акции, биржа поможет с выбором диапазона суммы и количеством попыток предложения цены. Чем меньше ты выберешь попыток, тем больше ультрадолларов ты сможешь заработать. Но будь осторожен: если ты проиграешь на бирже, твой актив уменьшится на величину ставки. Ты готов начать? Напиши "Да"')
next = input()
while next.lower() != 'да':
    next = input('Чтобы продолжить, введи "Да" ')

name = input('Пожалуйста, напиши как к тебе можно обращаться:)\n')
print('\n\nОчень рад познакомиться, я бот Форбс и я тоже готов к игре, ', name.title()) 
    
balance = 1000
balance_bot = 9000
list_coef, list_bet = [2, 4, 10], [100, 1000, 10000]
list_try2, list_try4, list_try10 = [6, 9, 13], [5, 8, 12], [4, 7, 11]

game()
