import random

date = [['見','貝'],['土','士'],['眠','眼']]
level = 1

def start_message():
    print('違う漢字の番号(例:A1)を入力してください')

def section_message():
    print('レベル:'+str(level))

def view_question():
    question = random.randint(0,2)
    print(date[question])

def play():
    section_message()
    view_question()
    choice = input('(例:A1)')
    print('デバッグ:choice = ' + choice)


start_message()
play()