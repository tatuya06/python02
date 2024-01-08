import random

data = [['見','貝'], ['土','士'], ['眠','眼']]
level = 1

def start_message():
    print('違う漢字の番号(例:A1)を入力してください')

def section_message():
    print('レベル：' + str(level))

def view_question():
    choice_data = random.randint(0, 2)
    mistake = random.randint(0,8)
    question = data[choice_data]
    print('デバック：choice = ' + str(mistake))
    print(question)
    print('/|ABC')
    print('--------')
    i = 0
    j = 0
    k = 1
    while i < 3:
        print(str(k)+'|',end='')
        while j < 3:
            if mistake == i * 3 + j:
                print(question[1], end='')
            else:
                print(question[0], end='')
            j += 1
        print()  
        i += 1
        k += 1
        j = 0 

def play():
    start_message()
    section_message()
    view_question()
    choice = input('(例:A1)')
    print('デバック：choice = ' + choice)

play()
