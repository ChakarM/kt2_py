import warnings
import random

warnings.filterwarnings("ignore")
words = ['параллелепипед', 'лампа', 'чашка', 'сахар', 'родственник', 'заварка', 'капитал']
choice = words[random.randint(0, len(words)-1)]
word_list = [i.lower() for i in choice]

def print_hang(count):
    if count == 0:
        print('''
  _______
  |/
  |
  |
  |
  |
  |
  |
  |
__|________
|         |
        ''')
        return True
    elif count == 1:
        print('''
  _______
  |/    |
  |
  |
  |
  |
  |
  |
  |
__|________
|         |
        ''')
        return True
    elif count == 2:
        print('''
  _______
  |/    |
  |    (_)
  |
  |
  |
  |
  |
  |
__|________
|         |
        ''')
        return True
    elif count == 3:
        print('''
  _______
  |/    |
  |    (_)
  |    \|/
  |
  |
  |
  |
  |
__|________
|         |
        ''')
        return True
    elif count == 4:
        print('''
  _______
  |/    |
  |    (_)
  |    \|/
  |     |
  |
  |
  |
  |
__|________
|         |
        ''')
        return True
    elif count == 5:
        print('''
  _______
  |/    |
  |    (_)
  |    \|/
  |     |
  |    / \\
  |
  |
  |
__|________
|         |
        ''')
        print("Вас повесили")
        return False

def get_input():
    usr_input = input("Введите букву или слово целиком: ")
    return usr_input

flag = True
attempts_failed = 0;
user_guessed = [' _ ' for _ in range(len(word_list))]
print("Добро пожаловать на Виселицу в поле чудес ^^")
print('Букв в слове: ', ''.join(user_guessed))
print_hang(attempts_failed)
while flag:
    if user_guessed == word_list:
        print("Вы победили")
        break
    usr_input = get_input().lower()
    print(''.join(user_guessed))
    usr_input_to_list = [i for i in usr_input]

    if len(usr_input_to_list) == 1:
        letter = usr_input_to_list[0]
        if letter in word_list:
            for i in range(len(word_list)):
                if word_list[i] == letter:
                    user_guessed[i] = letter
            print("Вы угадали букву")
            print(''.join(user_guessed))
                   
        else:
            attempts_failed+=1
            print("Неверно")
            flag = print_hang(attempts_failed)
            
    elif usr_input_to_list == word_list:
        print("Вы победили")
        break
    else:
        attempts_failed+=1
        print("Неверно")
        flag = print_hang(attempts_failed)
        
