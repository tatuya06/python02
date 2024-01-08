import random

data = [['見','貝'], ['土','士'], ['眠','眼']]
str_data = { 'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8 }

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
    print('/|A B C')
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
    return mistake

def change_input_number(input_str):
    input_str_list = list(input_str)
    #横の番号
    col_number = int(str_data[input_str_list[0]])
    #縦の番号
    row_number = int(input_str_list[1]) -1
    #入力した番号を数値変換する
    view_number = col_number  + row_number * 3
    return view_number

def is_correct_number(mistake_number, input_number):
  if mistake_number == input_number:
    return True
  else:
    return False

def viwe_result(is_correct):
    if is_correct == True:
        print('正解！！')
    else:
        print('不正解')


def play():
    start_message()
    section_message()
    mis = view_question()
    choice = input('(例:A1)')
    print('デバック：choice = ' + choice)
    vn = change_input_number(choice)
    print('デバック：input_number = ' + str(vn))
    correct = is_correct_number(mis,vn)
    viwe_result(correct)
    

play()
