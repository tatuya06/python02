import random

data = [['見','貝'], ['土','士'], ['眠','眼']]
level = 1

def start_message():
  print('違う漢字の番号(例:A1)を入力してください')

def section_message():
  print('レベル:' + str(level))

def view_question():
    choice_data = random.randint(0, 2)
    question = data[choice_data]
    print(question)
    i = 1
    j = 1
    while i < 4:
        while j < 4:
            print(question[0], end="")
            j = j + 1
        print(end='\n')
        i = i + 1
        j = 1  # 内部ループ終了時に j をリセット

def play():
  section_message()
  view_question()
  choice = input('(例:A1)')
  print('デバッグ:choice = ' + choice)

start_message()
play()