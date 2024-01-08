import random

data = [['見','貝'], ['土','士'], ['眠','眼']]
level = 1

def start_message():
    print('違う漢字の番号(例:A1)を入力してください')

def section_message():
    print('レベル：' + str(level))

def view_question():
    choice_data = random.randint(0, 2)
    question = data[choice_data]
    print(question)
    i = 0
    j = 0
    while i < 3:
        while j < 3:
            print(question[0], end='')
            j += 1
        print()  
        i += 1
        j = 0 

def play():
    start_message()
    section_message()
    view_question()
    choice = input('(例:A1)')
    print('デバック：choice = ' + choice)

play()
