import random

data = [['見','貝'], ['土','士'], ['眠','眼']]
level = 1

def start_message():
  print('違う漢字の番号(例:A1)を入力してください')

def section_message():
  print('レベル:' + str(level))

def view_question():
    choice_data = random.randint(0, 2)
    mistake_number = random.randint(0, 8)
    question = data[choice_data]
    print('デバック:mistake_number = '+ str(mistake_number))
    print(question)
    print('/|A B C')
    print('--------')
    i = 0
    j = 0
    k = 0
    while i < 3:
        k_number = k + 1
        print(str(k_number) + '|',end="")
        while j < 3: 
            if i * 3 + j == mistake_number:
               print(question[1],end="")
            else:
                print(question[0], end="")
            j = j + 1
        print(end='\n')
        i = i + 1
        k = k + 1
        j = 0  # 内部ループ終了時に j をリセット

def play():
  section_message()
  view_question()
  choice = input('(例:A1)')
  print('デバッグ:choice = ' + choice)

start_message()
play()