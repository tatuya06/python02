import random
import math

data = [['見','貝'], ['土','士'], ['眠','眼']]
str_data = { 'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8 }
number_data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

level = 1
col = 5
row = 4

def start_message():
    print('違う漢字の番号(例:A1)を入力してください')

def section_message():
    print('レベル：' + str(level))

def view_question():
    choice_data = random.randint(0, 2)
    mistake = random.randint(0,col * row)
    question = data[choice_data]
    print('デバック：choice = ' + str(mistake))
    print(question)
    a = 0
    pr_str = ''
    pr_bar = '--'
    while a < col:
        pr_str += number_data[a]
        pr_bar += '--'
        a += 1
    print('/|'+pr_str)
    print(pr_bar)
    i = 0
    j = 0
    k = 1
    while i < row:
        print(str(k)+'|',end='')
        while j < col:
            if mistake == i * col + j:
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
    view_number = col_number  + row_number * row
    return view_number

def is_correct_number(mistake_number, input_number):
  if mistake_number == input_number:
    return True
  else:
    return False

def viwe_result(is_correct,mis_nb):
    if is_correct == True:
        print('正解！！')
    else:
        print('不正解')
        change_string(mis_nb)
    
def change_string(number):
    #数値から文字を表示する配列
    q = number // col
    mod = math.floor(number % col) +1
    print('正解は'+number_data[q]+str(mod))

def play():
    start_message()
    section_message()
    mis = view_question()
    choice = input('(例:A1)')
    print('デバック：choice = ' + choice)
    vn = change_input_number(choice)
    print('デバック：input_number = ' + str(vn))
    correct = is_correct_number(mis,vn)
    viwe_result(correct,mis)
    

play()
